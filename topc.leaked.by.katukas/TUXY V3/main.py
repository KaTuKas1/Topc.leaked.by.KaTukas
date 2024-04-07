import os
import requests
import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command()
async def set_token(ctx):
    if not isinstance(ctx.channel, discord.DMChannel):
        return

    await ctx.send("Please send your account token https://www.youtube.com/watch?v=YEgFvgg7ZPI&t=14s")

    def check(msg):
        return msg.author == ctx.author and isinstance(msg.channel, discord.DMChannel)

    try:
        token_msg = await bot.wait_for('message', check=check, timeout=60)
        token = token_msg.content.strip()

        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        session = requests.Session()
        session.headers.update(headers)

        url = 'https://discord.com/api/v9/users/@me'
        response = session.get(url)

        if response.status_code == 200:
            with open('self.txt', 'r+') as file:
                saved_tokens = file.readlines()
                if token not in saved_tokens:
                    await ctx.send("Token is being addd to the host it may take 1 minute up to 5 minutes to add make a new server on the account aod !help or !uptime in a new server to see if our host is connected")

                    file.write(token + '\n')
                else:
                    await ctx.send("Token is already saved.")

        else:
            await ctx.send("Invalid token")

    except:
        pass
bot.run('MTIxNTA3OTE5ODc4ODU1MDY2Nw.GTb7dz.wQ2inKwUhJdbBHyUZ34RKy9wb4kL_6jK9YC74k')
