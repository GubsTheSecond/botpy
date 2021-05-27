import discord
from discord.ext import commands

client=commands.Bot(command_prefix='$')
@client.event
async def on_ready():
    print("Bumbumbumbumbabumbumbabum")

@client.event
async def on_member_join(member):
    print("We would be honored, if you would join us,",member,".")

@client.event
async def on_member_remove(member):
    print("I find your lack of faith disturbing, ",member,".")

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency*1000)}ms.")

client.run('ODI1MDcyNjIyMzY1OTY2MzM4.YF4mwg.0oydGKRtwR9XLouxkMXjN-YHuy0')   #Place token between the ''
