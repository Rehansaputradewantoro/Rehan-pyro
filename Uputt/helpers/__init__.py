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
        await client.join_chat("ZoneDangerSex")
        await client.join_chat("Revanstoreya")
        await client.join_chat("abcdump02")
        await client.join_chat("Geninstore")
    except BaseException:
        pass
