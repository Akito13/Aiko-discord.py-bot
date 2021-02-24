import discord
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord import Intents
from calendar import isleap
from discord.ext.commands import CommandNotFound
fro
PREFIX = "="
OWNER_IDS = [445467804171239435]

class Aiko(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
        command_prefix = PREFIX,
        owner_ids = OWNER_IDS,
        intents = Intents.all(),
        )

    def run(self, version):
        self.VERSION = version

        with open("lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Setting up Aiko...Please be patient...")
        super().run(self.TOKEN, reconnect = True)

    async def on_connect(self):
        print("I\'m ready !")

    async def on_disconnect(self):
        print("I'm offline now.")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong. I can't execute it.")

        raise

    #async def on_command_error(self, ctx, exc):
    #    if isinstance(exc, C)
    async def on_ready(self):

        if not self.ready:
            self.ready = True
            print("Aiko is ready")

        else:
            print("Aiko is back.")


    async def on_message(self, message):
        pass

aiko = Aiko()
