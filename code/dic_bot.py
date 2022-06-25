
import discord
from config import bot_token, channel_id
from trel import Trwork

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    notif = Trwork()
    channel = client.get_channel(id=channel_id) # replace with channel_id
    while not client.is_closed():
        message = notif.get_message()
        if message is not None:
            await channel.send(message)
         # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())
client.run(bot_token)

