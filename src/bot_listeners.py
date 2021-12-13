
async def on_ready():
    print(f"Logged in successfully!")

async def on_message(message):
    content = message.content if message.content else "(Not printable)."
    print(f"Message from {message.author}: {content}")