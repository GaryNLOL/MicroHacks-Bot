from discord.ext import commands
from discord.utils import get
from utils import create_embed
from bot_settings import assignable_roles, role_codes, server_id

@commands.command(brief="Get your ping.")
async def ping(ctx):
    ping_in_ms = round(ctx.bot.latency,1)
    ping_content = f"Your ping is {ping_in_ms} ms."
    embed = create_embed(title="Ping",fields=[{'name': "Your ping",'value': ping_content}])
    await ctx.channel.send(embed=embed)

@commands.command(brief="Get bot information.")
async def about(ctx):
    about_content = "Created by **Gary Hilares**.\nLicensed under **MIT License**.\nContact: **dev.garynlol@gmail.com**."
    embed = create_embed(title="About",fields=[{'name': "Bot information", 'value': about_content}])
    await ctx.channel.send(embed=embed)

@commands.command(brief="Get role.")
async def role(ctx, *args):
    member = ctx.message.author
    role_name = ' '.join(args)
    role = get(member.guild.roles,name=role_name)
    if role and role_name in assignable_roles:
        await member.add_roles(role)
        await ctx.send(f"Assigned {role_name} to {ctx.author}.")
    else:
        await ctx.send(f"Couldn't assign {role_name} to {ctx.author}.")

@commands.command(brief="Get role from code.")
async def role_from_code(ctx, *args):
    server = ctx.bot.get_guild(server_id)
    member = server.get_member(ctx.message.author.id)
    if len(args) != 1:
        await ctx.send("This command requires exactly 1 argument.")
    else:
        code = args[0]
        if code in role_codes:
            role = get(server.roles,id=role_codes[code])
            await member.add_roles(role)
            await ctx.send(f"Assigned role to {ctx.author}.")
        else:
            await ctx.send("Code not found.")

@commands.command(brief="Shows this message.")
async def help(ctx):
    embed = create_embed(title="Help",fields=[])
    commands = ctx.bot.commands.copy()
    commands_sorted_alphabetically = sorted(commands, key=lambda x: x.name,reverse=False)
    commands_sorted_by_length_followed_by_alphabetically = sorted(commands_sorted_alphabetically, key=lambda x: len(x.name))
    command_strings = [f"**{command.name}:** {command.brief}" for command in commands_sorted_by_length_followed_by_alphabetically]
    help_content = '\n'.join(command_strings)
    embed.add_field(name="Commands",value=help_content,inline=False)
    await ctx.channel.send(embed=embed)