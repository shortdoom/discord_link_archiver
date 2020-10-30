# discord_link_archiver
Simple bot to grab all messages containing urls from specified discord channels.

## Prerequisites

Create and authorize bot account in your Discord server - [Instructions](https://discordpy.readthedocs.io/en/latest/discord.html#creating-a-bot-account)

## Usage

Specify channels you want to parse in ```channel_list```. Default behavior is to extract all channels and parse them in full (slow).

To specify channels you need to supply channel id in form of an ```int```. Get it by visiting channels on your discord server and executing ```\#channel_name``` command.

You can limit parsing to N-amount of messages. Check ```discord.py``` documentation - [Here](https://discordpy.readthedocs.io/en/latest/api.html?highlight=history#discord.TextChannel.history)

Run it in shell ```python archive.py```.

## Limitations

Script extracts full message containing any ```https://``` link. Remember to post-process your output if you want clean links.

Output is limited to link / channel / created_at. You can extend it with more attributes - [Here](https://discordpy.readthedocs.io/en/latest/api.html?highlight=history#discord.Message)
