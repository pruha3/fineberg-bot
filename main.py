import discord
from discord.ext import commands
from loguru import logger

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#1125820992304984064

@client.event
async def on_ready():
    logger.info("The bot is working now")
    logger.info("-------------------------------------------")


@client.event
async def on_message(message):
    channel = client.get_channel(1125820992304984064)
    embed = discord.Embed(
        title='Кто отправил Что',
        description=" отправил: {} что: {}".format(message.author.name, message.content),
        color=discord.Color.from_rgb(255, 0, 100),
    )
    if not message.author.bot:
        await channel.send(embed=embed)
    logger.info(message.content)
    logger.info(message.author.name)

if __name__ == "__main__":
    client.run("MTEzMTYxMzQzMzE0NjY1MDc0NA.GiU296.gtwZwuf_H8uQk3__4Fog6dMNSBuAC4gEkIqz7A")