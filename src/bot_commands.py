from discord.ext import commands
from utils import render_template, create_embed

@commands.command(brief="Get your ping.")
async def ping(ctx):
    ping_in_ms = round(ctx.bot.latency,1)
    ping_content = render_template('ping.txt',ping_in_ms=ping_in_ms)
    embed = create_embed(title="Ping",fields=[{'name': "Your ping",'value': ping_content}])
    await ctx.channel.send(embed=embed)

@commands.command(brief="Get bot information.")
async def about(ctx):
    about_content = render_template('about.txt')
    embed = create_embed(title="About",fields=[{'name': "Bot information", 'value': about_content}])
    await ctx.channel.send(embed=embed)