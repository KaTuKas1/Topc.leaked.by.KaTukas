import os
import requests
import websocket
import json
import time
import discord
from discord.ext import commands

headers = {'Content-Type': 'application/json'}

session = requests.Session()

def send_message(token, channel_id, content):
    headers['Authorization'] = token
    payload = {'content': content}
    response = session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)
    if response.status_code != 200:
        pass

def create_channel(token, guild_id, name):
    headers['Authorization'] = token
    payload = {'name': name, 'type': 0}  
    response = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json=payload)
    if response.status_code != 201:
        pass

def handle_event(ws, token, event):
    if ws.connected:  
        if event['t'] == 'READY':
            pass
        elif event['t'] == 'MESSAGE_CREATE':
            message_data = event['d']
            if 'content' in message_data:
                content = message_data['content']
                channel_id = message_data['channel_id']
                if content.startswith('!make'):
                    guild_id = message_data['guild_id']
                    for i in range(10):
                        create_channel(token, guild_id, f'topc_{i}')
                elif content.startswith('whoistopc'):
                    send_message(token, channel_id, 'Topc is a network of bots like this self bot this user is using join us today .gg / ixnf')
                elif content.startswith('help'):
                    send_message(token, channel_id, 'need help? say whoistopc to show people who made this !spam (message) (amount) spam custom messages  !make this will make channesl in server make sure u have perms . gg/ ixnf da best ')
                elif content.startswith('!spam'):
                    args = content.split()[1:]  
                    if len(args) == 2:
                        message = args[0]
                        amount = int(args[1])
                        for _ in range(amount):
                            send_message(token, channel_id, message)
                            time.sleep(1)  
                        send_message(token, channel_id, f"Success {amount}")
    else:
        connect_to_gateway(token)

def connect_to_gateway(token):
    while True:
        try:
            ws = websocket.create_connection('wss://gateway.discord.gg/?v=9&encoding=json')
            ws.send(json.dumps({
                'op': 2,
                'd': {
                    'token': token,
                    'intents': 513,
                    'properties': {
                        '$os': 'windows',
                        '$browser': 'my_library',
                        '$device': 'my_library'
                    }
                }
            }))

            while True:
                try:
                    event = json.loads(ws.recv())
                    handle_event(ws, token, event)
                except json.JSONDecodeError as e:
                    continue
                except Exception as e:
                    print("Connection lost. Reconnecting...")
                    ws.close()
                    connect_to_gateway(token)
                    break

                if not ws.connected:
                    print("Connection lost. Reconnecting...")
                    ws.close()
                    connect_to_gateway(token)
                    break

                time.sleep(0.1)

        except Exception as e:
            print("Failed to connect. Retrying in 5 seconds...")
            time.sleep(5)

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
            await ctx.send("Token is valid. Connecting to Discord gateway... type help to see if working")
        
            connect_to_gateway(token)
        else:
            await ctx.send("Invalid token")

    except TimeoutError:
        pass

bot.run('MTIxMjg0OTYyMjM4OTYyNDkxNg.GJst85.wHuYx-p-XrFOpz5SFRkH-Ay0JwQ-YCDTYpKimM')
