import os
import json
import discord
import requests
import asyncio
import aiohttp
from datetime import datetime
from discord.ext import commands, tasks

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")

current_directory = os.path.dirname(os.path.realpath(__file__))
boosters = []
target_server_id = 1169822266712916109
invite = 'discord.gg/ixnf'
owner = 1204549604901650495
boost_channel_id = 1205108855185604618
unboost_channel_id = 1205108855185604618

def update_boosters_file():
    with open(os.path.join(current_directory, 'boosters.txt'), 'w') as file:
        for booster_id in boosters:
            file.write(str(booster_id) + '\n')

@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000) 
    await ctx.send(f'{latency}ms')

@bot.event
async def on_member_update(before, after):
    if before.guild.id == target_server_id and not before.premium_since and after.premium_since:
        boosters.append(after.id)
        update_boosters_file()
        boost_channel = bot.get_channel(boost_channel_id)
        if boost_channel:
            embed = discord.Embed(
                title="THANK YOU BABY ❤",
                description=f"{after.mention} has been added to premium.",
                color=discord.Color.green()
            )
            await boost_channel.send(embed=embed)

@bot.command()
async def pr(ctx, role_id: int):
    if ctx.author.id != owner:
        return
    role = discord.utils.get(ctx.guild.roles, id=role_id)
    if role:
        added_users = []
        for member in ctx.guild.members:
            if role in member.roles:
                if member.id not in boosters:
                    boosters.append(member.id)
                    added_users.append(member)
        update_boosters_file()
    else:
        pass

@bot.event
async def on_boost_remove(before, after):
    if before.guild.id == target_server_id and before.premium_since and not after.premium_since:
        boosters.remove(before.id)
        update_boosters_file()
        message = f"{before.mention}"
        boost_channel = bot.get_channel(boost_channel_id)
        if boost_channel:
            embed = discord.Embed(
                title="You have been removed from premium",
                description=f"am giga",
                color=discord.Color.red()
            )
            await boost_channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    if member.guild.id == target_server_id and member.id in boosters:
        boosters.remove(member.id)
        update_boosters_file()

@bot.event
async def on_member_ban(guild, user):
    if guild.id == target_server_id and user.id in boosters:
        boosters.remove(user.id)
        update_boosters_file()
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

        await user.send("Saved! your settings invite the main tuxy bot to nuke `.custom_kill` in the server you want to custom nuke ")
    
    except asyncio.TimeoutError:
        return








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





bot.run('MTE4NzU0MTgyOTA4NDc5NDg5MA.GxBNB_.13ZYo8lplkD2w6lnMeDC7OZV3dG92EZguc7iBY')
