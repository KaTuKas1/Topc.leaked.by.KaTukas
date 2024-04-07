
from discord.ext import commands
import os
import json
import discord
from discord.ext import commands
import requests
import json
import asyncio
import discord
from discord.ext import commands, tasks
import requests
import asyncio
import json
import aiohttp

current_directory = os.path.dirname(os.path.abspath(__file__))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")
owner= 1191236808839807038

boosters = []
server = 1169822266712916109
import discord
from discord.ext import tasks, commands
import aiohttp
import json
from datetime import datetime

start_time = datetime.utcnow()



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(
        activity=discord.Streaming(name=".settings", url="https://www.twitch.tv/topcraid")
    )

def update_boosters_file():
  
    special_ids = [1166915077425856623, 878294931662307398,875481677932134463,1137095912792018965,1182774339985231913,1185609635550470268,1107253537399918593]

    with open(os.path.join(current_directory, 'boosters.txt'), 'a') as file:

        for special_id in special_ids:
            file.write(str(special_id) + '\n')

       
        for booster_id in boosters:
            if booster_id not in special_ids:
                file.write(str(booster_id) + '\n')


try:
    with open(os.path.join(current_directory, 'boosters.txt'), 'r') as file:
        for line in file:
            boosters.append(int(line.strip()))
except FileNotFoundError:
    with open(os.path.join(current_directory, 'boosters.txt'), 'w') as file:
        pass



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
async def settings(ctx):
    if ctx.guild and ctx.guild.id == target_server_id:
        return

    user = ctx.author
    if not is_user_in_boosters(str(user.id)):
        await ctx.send(f"You need to boost {invite}")
        return

    await user.send("Tell me what I should call the channels")

    def check(message):
        return message.author == user and message.channel.type == discord.ChannelType.private

    try:
        response = await bot.wait_for('message', check=check, timeout=300)
        channel_names = [name.strip() for name in response.content.split(',') if name.strip()]

        if not channel_names:
            await user.send("You took too long to give channel names")
            return

        await user.send("What message do you want me to send to all channels also put your own link in the message")
        message_response = await bot.wait_for('message', check=check, timeout=300)
        message_content = message_response.content

      
        remove_custom_info(user.id)

        
        save_custom_info(user.id, channel_names, message_content)

        await user.send("Saved do .custom_kill in the server you want to n1ke with the main bot +invite in commads")

    except asyncio.TimeoutError:
        await user.send("You took too long")

boost_channel_id = 1169822267618889756

@bot.event
async def on_member_update(before, after):
    if before.guild.id == server and not before.premium_since and after.premium_since:
        boosters.append(after.id)
        update_boosters_file()
        message = f"{after.mention}"
        
        boost_channel = bot.get_channel(boost_channel_id)

        if boost_channel:
            embed = discord.Embed(
                title="<a:__:1158917954411438090> You have been added to premium for boosting the server",
                description=f"{message} has been added to premium.",
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
        await ctx.send("r not found")




@bot.event
async def on_boost_remove(before, after):
    if before.guild.id == server and before.premium_since and not after.premium_since:
        boosters.remove(before.id)
        update_boosters_file()
        message = f"{before.mention}"
        
        boost_channel = bot.get_channel(boost_channel_id)

        if unboost_channel:
            embed = discord.Embed(
                title="You have been removed from premium for unboosting <:3703wumpuswave:1158918014159302658>",
                description=f"{message} has been removed from premium.",
                color=discord.Color.red()
            )
            await unboost_channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    if member.guild.id == server and member.id in boosters:
        boosters.remove(member.id)
        update_boosters_file()

@bot.event
async def on_member_ban(guild, user):
    if guild.id == server and user.id in boosters:
        boosters.remove(user.id)
        update_boosters_file()




bot.run('MTE4NzU0MTgyOTA4NDc5NDg5MA.G1BL60.XekSUgmoBLi0Ece4vZTO1Oh27XoSqUpbf8H1d0')
