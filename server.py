import os

import discord

from utils.dice_tools import exec_command

DISCORD_ACCESS_TOKEN = os.environ['DISCORD_ACCESS_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('Login.')

@client.event
async def on_message(message):

    if message.author.bot:
        return

    prefix = message.content.split()[0]
    command = message.content.split()[1]

    if prefix == '/dice':
        result = exec_command(command = command)
        
        reply_message = f'{message.author.mention}\n{result}'
        await message.channel.send(reply_message)

def main():
    client.run(DISCORD_ACCESS_TOKEN)

if __name__ == '__main__':
    main()
