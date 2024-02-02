# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from Uputt.helpers.basic import edit_or_reply
from Uputt.helpers.PyroHelpers import ReplyCheck

from .help import *


@Client.on_message(filters.command("p", cmd) & filters.me)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Anak Anjing Lu Belom Beli Bot Di @Revans505",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("pe", cmd) & filters.me)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Warahmatullahi Wabarakatuh Beli Bot PC ke @Revans505",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("l", cmd) & filters.me)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Kaum Sodara Atheis",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("el", cmd) & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh Beli Bot PC @Revans505",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("a", cmd) & filters.me)
async def salken(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Haii Salken Saya {client.me.first_name} Orang Terkaya Di Telegram**")
    await asyncio.sleep(2)
    await xx.edit("Assalamualaikum Sayangku Mau Ga Jadi Pacar Aku")


@Client.on_message(filters.command("ass", cmd) & filters.me)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Biar Sopan")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")


@Client.on_message(filters.command("j", cmd) & filters.me)
async def jakasem(client: Client, message: Message):
    xx = await edit_or_reply(message, "**JAKA SEMBUNG BAWA GOLOK**")
    await asyncio.sleep(3)
    await xx.edit("**NIMBRUNG GOBLOKK!!!🔥 Beli Bot PC @Revans505**")


@Client.on_message(filters.command("k", cmd) & filters.me)
async def ngegas(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Hallo KIMAAKK SAYA {client.me.first_name} Orang Tajir**")
    await asyncio.sleep(2)
    await xx.edit("**LU SEMUA PETINGGI NGENTOT 🔥**")


add_command_help(
    "salam",
    [
        ["p", "Assalamualaikum."],
        ["pe", "Assalamualaikum Warahmatullahi Wabarakatuh."],
        ["l", "Wa'alaikumsalam."],
        ["ass", "Assalamualaikum Bahas arab."],
        ["a", "Salam Kenal dan salam."],
        ["l", "Wa'alaikumsalam."],
        ["el", "Wa'alaikumsalam Warahmatullahi Wabarakatuh."],
    ],
)
