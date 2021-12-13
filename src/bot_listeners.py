from bot_settings import welcome_channel_id, default_role
import logging

async def on_ready(client):
    logging.getLogger('BotEvents').debug(f"Logged in successfully as {client.user}!")

async def on_message(client,message):
    content = message.content if message.content else "(Not printable)"
    logging.getLogger('BotEvents').debug(f"Message from {message.author}: {content}.")

async def on_member_join(client,member):
    if default_role:
        await member.add_roles(default_role)
    await client.get_channel(welcome_channel_id).send(f"{member.name} has joined.")