import os

import discord

from utils.dice.main import exec_command

DISCORD_ACCESS_TOKEN = os.environ['DISCORD_ACCESS_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('Login.')

@client.event
async def on_message(message):

    if message.author.bot:
        return

    if message.content.split()[0] == '/dice':
        command = message.content.split()[1]
        result = exec_command(command)
        reply_message = f'{message.author.mention}\n{result}'
        await message.channel.send(reply_message)

def main():
    client.run(DISCORD_ACCESS_TOKEN)

if __name__ == '__main__':
    main()
