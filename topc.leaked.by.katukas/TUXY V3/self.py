import threading
import websocket
import json
import random
import requests
import string as s
import base64
from googletrans import Translator
from collections import defaultdict
import time
cooldowns = {
    "!m": 60,
    "!w": 30,
    "!s": 20,
    "!j": 10,
    "!p": 3,
    "!uptime": 3
}

last_command_usage = defaultdict(lambda: 0)
token_start_time = defaultdict(lambda: 0) 

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
]





REQUESTS_PER_SECOND = 35

def extract_os_and_browser_from_user_agent(user_agent):
    os = "Windows"
    browser = "Chrome"
    return os, browser

def generate_random_headers():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'discord.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': random.choice(user_agents)
    }
    return headers

class Headers():
    @staticmethod
    def get_fingerprint(client):
        try:
            fingerprint = client.get("https://discord.com/api/v9/experiments", timeout=5).json()["fingerprint"]
            return fingerprint
        except Exception as e:
            pass

    @staticmethod
    def get_super_properties():
        properties = '''{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-GB","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36","browser_version":"95.0.4638.54","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":102113,"client_event_source":null}'''
        properties = base64.b64encode(properties.encode()).decode()
        return properties

    @staticmethod
    def get_cookies(client):
        r = client.get("https://discord.com/", timeout=5)
        dcf = r.cookies.get("__dcfduid")
        sdc = r.cookies.get("__sdcfduid")
        return f'__dcfduid={dcf}; __sdcfduid={sdc}'

    @staticmethod
    def get_headers(client, token) -> dict:
        cookies = Headers.get_cookies(client)
        fingerprint = Headers.get_fingerprint(client)
        super_properties = Headers.get_super_properties()
        headers = {
            'authority': 'discord.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US',
            'authorization': token,
            'cookie': cookies,
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-debug-options': 'bugReporterEnabled',
            'x-fingerprint': fingerprint,
            'x-super-properties': super_properties,
        }
        return headers

def send_request(method, url, token, data=None):
    headers = Headers.get_headers(requests, token)
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, json=data)
    return response

def send_message(token, channel_id, content):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    data = {'content': content}
    response = send_request('POST', url, token, data)
    if response.status_code != 200:
        pass

def create_channel(token, guild_id, name):
    url = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
    data = {'name': name, 'type': 0}
    response = send_request('POST', url, token, data)
    if response.status_code != 201:
        pass

def handle_event(ws, token, event):
    if ws.connected:
        if event['t'] == 'READY':
            token_start_time[token] = time.time()  
        elif event['t'] == 'MESSAGE_CREATE':
            message_data = event['d']
            if 'content' in message_data:
                content = message_data['content']
                channel_id = message_data['channel_id']
                if content.startswith('!m'):
                    handle_command_with_cooldown("!m", token, channel_id, message_data['guild_id'])
                elif content.startswith('!w'):
                    handle_command_with_cooldown("!w", token, channel_id)
                elif content.startswith('!h') or content.startswith('!help'):
                    handle_command_with_cooldown("!h", token, channel_id)
                elif content.startswith('!s'):
                    handle_command_with_cooldown("!s", token, channel_id, *content.split(maxsplit=1)[1:])
                elif content.startswith('!j'):
                    handle_command_with_cooldown("!j", token, channel_id)
                elif content.startswith('!p'):
                    handle_command_with_cooldown("!p", token, channel_id, *content.split(maxsplit=1)[1:])
                elif content.startswith('!uptime'):
                    handle_command_with_cooldown("!uptime", token, channel_id)
    else:
        connect_to_gateway(token)

def handle_command_with_cooldown(command, token, channel_id, *args):
    current_time = time.time()
    last_usage = last_command_usage.get(command, 0)
    cooldown = cooldowns.get(command, 0)
    if current_time - last_usage >= cooldown:
        last_command_usage[command] = current_time
        if command == "!m":
            guild_id = args[0]
            for i in range(10):
                create_channel(token, guild_id, f'topc')
        elif command == "!w":
            send_message(token, channel_id, 'Made By Topc join .gg/ixnf to use')
        elif command == "!h":
            send_message(token, channel_id, 'Hello thanks for useing made by .gg/ixnf '
                                             '\n'
                                             '1. !w - To see who made this \n'
                                             '2. !p (cryptocurrency coin) - Get the current price of a cryptocurrency.\n'
                                             '3. !j - Get a random joke from the joke file.\n'
                                             '4. !m - Make channels in the server (you need permissions).\n'
                                             '5. !s - !spam (message) this will spam bypass most anti raid bots\n'
                                             '6. !uptime - Check how long u been online for.')
        elif command == "!s":
            if len(args) >= 1:
                message = args[0]
                for _ in range(15):
                    random_string = ''.join(random.choices(s.ascii_lowercase, k=random.randint(1, 5)))
                    send_message(token, channel_id, f"{message} {random_string}  -__- .gg / ixnf")
            else:
                pass
        elif command == "!j":
            joke = get_random_joke_from_file()
            send_message(token, channel_id, joke)
        elif command == "!p":
            coin = args[0]
            price = get_coin_price(coin)
            send_message(token, channel_id, f"Current {coin.capitalize()} Price: ${price}")
        elif command == "!uptime":
            uptime = current_time - token_start_time[token]
            send_message(token, channel_id, f"Uptime: {uptime:.2f} seconds")

def connect_to_gateway(token):
    try:
        headers = Headers.get_headers(requests, token)
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            set_status(token, "dnd", ".gg/ixnf")
            while True:
                try:
                    user_agent = generate_random_headers()['User-Agent']
                    os, browser = extract_os_and_browser_from_user_agent(user_agent)
                    ws = websocket.create_connection('wss://gateway.discord.gg/?v=9&encoding=json', header={'User-Agent': user_agent})
                    ws.send(json.dumps({
                        'op': 2,
                        'd': {
                            'token': token,
                            'intents': 513,
                            'properties': {
                                '$os': os,
                                '$browser': browser,
                                '$device': 'desktop'
                            }
                        }
                    }))

                    while True:
                        try:
                            event = json.loads(ws.recv())
                            handle_event(ws, token, event)
                        except json.JSONDecodeError:
                            continue
                        except Exception:
                            break

                        if not ws.connected:
                            break

                        time.sleep(0.1)

                    ws.close()

                except Exception:
                    break

                time.sleep(5)
        else:
            pass
    except Exception as e:
        pass

def set_status(token, status, custom_status_text):
    headers = Headers.get_headers(requests, token)
    jsonData = {
        'status': status,
        'custom_status': {
            'text': custom_status_text
        }
    }
    response = requests.patch(url="https://discord.com/api/v10/users/@me/settings", headers=headers, json=jsonData)
    if response.status_code != 200:
        pass

def get_random_joke_from_file():
    with open("jokes.txt", "r") as f:
        jokes = f.readlines()
    return random.choice(jokes).strip()

def get_coin_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if coin in data:
            return data[coin]['usd']
    return "NOT A REAL COIN 😩"

def main():
    previous_tokens = set()
    while True:
        with open("self.txt", "r") as f:
            tokens = set(f.read().splitlines())

        new_tokens = tokens - previous_tokens
        for token in new_tokens:
            threading.Thread(target=connect_to_gateway, args=(token,)).start()

        previous_tokens = tokens
        time.sleep(2)

if __name__ == "__main__":
    main()
