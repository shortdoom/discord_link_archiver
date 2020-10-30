import discord
import time
import json

client = discord.Client()

async def save_to_file(file, start):

    '''Matching URLS inside of a string is a cumbersome job. Following returns whole message containing URL. Process later '''

    pattern = 'https'
    msg_list = [(msg.content, msg.channel, msg.created_at) for msg in file for msg in msg]
    msg_list = [msg for msg in msg_list if pattern in msg[0]]

    msg_json = [{"link": msg[0], "channel": str(msg[1]), "created_at": msg[2].strftime("%d/%m/%Y, %H:%M:%S")} for msg in msg_list]

    end = time.time()
    print('took', end - start, 'for', len(msg_list), 'messages')

    with open('/output.json', 'w') as f:
        json.dump(msg_json, f)

async def all_channels():
    channel_list = []

    for guild in client.guilds:
        for channel in guild.text_channels:
            channel_list.append(channel.id)

    return channel_list

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    start = time.time()

    '''Change to False if you supply your own channel.id list. Otherwise we are looking inside of all channels.'''

    iterate_all = True

    '''To get channel.id you can post \#channel_name command inside your discord channel'''

    if iterate_all == True:
        channel_list = await all_channels()
    else:
        channel_list = []

    '''Crawl all of channel history, else - change limit to N-int'''

    channel_msg = []
    for channel in channel_list:
        current_channel = client.get_channel(channel)
        messages = await current_channel.history(limit=None, oldest_first=True).flatten()
        channel_msg.append(messages)

    await save_to_file(channel_msg, start)

client.run('API-KEY')