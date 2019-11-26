import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
            await message.channel.send("그 대는 정말로 안녕이라고 말하였기 때문에 평민 등급을 주지")
                                       
                                    
client.run("NjA3MTQyNDAxODM2MDU2NTc5.Xdp-Aw.Rt_jPT6TcFjVNK9XSBlkUe_adrg")
