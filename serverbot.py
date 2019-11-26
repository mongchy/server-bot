import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
            await message.channel.send("그 대는 정말로 안녕이라고 말하였기 때문에 평민 등급을 주지")
                                       
                                    
access_token = os.enviorn["BOT_TOKEN"]
client.run(access_token)
