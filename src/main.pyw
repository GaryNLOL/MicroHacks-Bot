import logging
import discord
from discord.ext import commands
from bot_listeners import on_ready, on_message, on_member_join
from bot_commands import ping, about, role, role_from_code, help
from utils import get_text_from_file
from functools import partial as bind

# Logging setup
logging.basicConfig(format='[%(name)s] %(levelname)s: %(message)s')
logging.getLogger('BotEvents').setLevel(logging.DEBUG)

# Bot setup
intents = discord.Intents.default()
intents.members = True
MicrohacksClient = commands.Bot(command_prefix='hacks@',intents=intents,help_command=None)
MicrohacksClient.add_command(about)
MicrohacksClient.add_command(help)
MicrohacksClient.add_command(ping)
MicrohacksClient.add_command(role)
MicrohacksClient.add_command(role_from_code)
MicrohacksClient.add_listener(bind(on_ready,MicrohacksClient),name='on_ready')
MicrohacksClient.add_listener(bind(on_message,MicrohacksClient),name='on_message')
MicrohacksClient.add_listener(bind(on_member_join,MicrohacksClient),name='on_member_join')

def main():
    MicrohacksClient_token = get_text_from_file('token.txt')
    MicrohacksClient.run(MicrohacksClient_token)

if __name__ == '__main__':
    main()
