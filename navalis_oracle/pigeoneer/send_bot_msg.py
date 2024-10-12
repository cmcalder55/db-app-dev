from flask import Flask, request
import threading
import discord
from dotenv import load_dotenv
import os
import json
import requests

app = Flask(__name__)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
GUILD = int(os.getenv('DISCORD_GUILD'))
CHANNEL = int(os.getenv('DISCORD_CHANNEL'))
TERMINATE = os.getenv("TERMINATE")

intents = discord.Intents.default()
intents.message_content = True

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Forward the data to Discord webhook
    if data:
        # Format your message here
        message = "<@{0}>\n{1}".format(data.get("user"), data.get("message"))
        payload = {
            "content": message,
            "username": "PoE Watcher"
        }
        response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        
        # Check if the request was successful
        if response.status_code == 204:
            return "Message forwarded to Discord", 200
        else:
            return f"Failed to forward message: {response.status_code}", 500
    return 'No data received', 400

def run():
    app.run(port=5000)

def start_bot():
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')

    client.run(TOKEN)

if __name__ == '__main__':

    t = threading.Thread(target=run)
    t.start()
    start_bot()
