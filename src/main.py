from discord.ext import commands
from bot_listeners import on_ready, on_message
from bot_commands import ping, about
from utils import get_text_from_file

MicrohacksClient = commands.Bot(command_prefix='hacks@')
MicrohacksClient.add_command(ping)
MicrohacksClient.add_command(about)
MicrohacksClient.add_listener(on_ready)
MicrohacksClient.add_listener(on_message)

def main():
    MicrohacksClient_token = get_text_from_file('token.txt')
    MicrohacksClient.run(MicrohacksClient_token)

if __name__ == '__main__':
    main()
