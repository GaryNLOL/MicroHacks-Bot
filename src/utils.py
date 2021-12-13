import discord

def get_text_from_file(filename):
    with open(filename,'r') as fp:
        return fp.read()

def create_embed(*args,**kwargs):
    embed = discord.Embed(title=kwargs['title'])
    for field in kwargs['fields']:
        embed.add_field(name=field['name'],value=field['value'], inline=True)
    return embed