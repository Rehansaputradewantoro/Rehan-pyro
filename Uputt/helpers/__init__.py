from .adminHelpers import *
from .basic import *
from .constants import *
from .expand import *
#from .misc import *
from .interval import *
from .msg_types import *
from .parser import *
from .PyroHelpers import *
from .tools import *
from .utility import *


import os
import sys
from pyrogram import Client


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Uputt"])

async def join(client):
    try:
        await client.join_chat("amneseey0u")
        await client.join_chat("UputtSupport")
        await client.join_chat("Flukosaa")
        await client.join_chat("kynansupport")
        await client.join_chat("https://t.me/askarasenjaaa")
        await client.join_chat("t.me/+f5Z212zv4gU0MTk1")
        await client.join_chat("https://t.me/sellerkeren")
        await client.join_chat("https://t.me/sellerkerensupport")
        await client.join_chat("https://t.me/+dCrinQCj-TdkZTA1")
    except BaseException:
        pass
