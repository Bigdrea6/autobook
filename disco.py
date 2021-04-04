import discord
from discord.ext import tasks
import time
import datetime

import login

url="*****"
client = discord.Client()
token="******"

@client.event
async def on_ready():
    print("Login")
    print(client.user.name)
    print(client.user.id)
    print("-----")


@client.event
async def on_message(message):
    if message.content.startswith("1"):
        m="パターン : 月~木・土"
        await message.channel.send(m)
        while True:
            ready=hei()
            if ready:
                break
        for i in range(40):
            log=login.main()
            if log!=False:
                yotei1=""
                for i in range(0,13):
                    if i==0:
                        yotei1+=(log[i]+":")
                    elif i==6:
                        yotei1+=(log[i]+"/")
                    else:
                        yotei1+=(log[i]+" ")
                yotei2=""
                for i in range(13,26):
                    if i==13:
                        yotei2+=(log[i]+":")
                    elif i==19:
                        yotei2+=(log[i]+"/")
                    else:
                        yotei2+=(log[i]+" ")
                yotei3=""
                for i in range(26,39):
                    if i==26:
                        yotei3+=(log[i]+":")
                    elif i==32:
                        yotei3+=(log[i]+"/")
                    else:
                        yotei3+=(log[i]+" ")
                yotei4=""
                for i in range(39,52):
                    if i==39:
                        yotei4+=(log[i]+":")
                    elif i==45:
                        yotei4+=(log[i]+"/")
                    else:
                        yotei4+=(log[i]+" ")
                yotei5=""
                for i in range(52,65):
                    if i==52:
                        yotei5+=(log[i]+":")
                    elif i==58:
                        yotei5+=(log[i]+"/")
                    else:
                        yotei5+=(log[i]+" ")
                yotei6=""
                for i in range(65,78):
                    if i==65:
                        yotei6+=(log[i]+":")
                    elif i==71:
                        yotei6+=(log[i]+"/")
                    else:
                        yotei6+=(log[i]+" ")
                yotei7=""
                for i in range(78,90:
                    if i==78:
                        yotei7+=(log[i]+":")
                    elif i==84:
                        yotei7+=(log[i]+"/")
                    else:
                        yotei7+=(log[i]+" ")

                await message.channel.send(yotei1)
                await message.channel.send(yotei2)
                await message.channel.send(yotei3)
                await message.channel.send(yotei4)
                await message.channel.send(yotei5)
                await message.channel.send(yotei6)
                await message.channel.send(yotei7)
                await message.channel.send(url)
            time.sleep(170)

    elif client.user!=message.author:
        m="パターン : 日曜"
        await message.channel.send(m)
        while True:
            ready=kyuu()
            if ready:
                break
        for i in range(40):
            log=login.main()
            if log!=False:
                yotei1=""
                for i in range(0,13):
                    if i==0:
                        yotei1+=(log[i]+":")
                    elif i==6:
                        yotei1+=(log[i]+"/")
                    else:
                        yotei1+=(log[i]+" ")
                yotei2=""
                for i in range(13,26):
                    if i==13:
                        yotei2+=(log[i]+":")
                    elif i==19:
                        yotei2+=(log[i]+"/")
                    else:
                        yotei2+=(log[i]+" ")
                yotei3=""
                for i in range(26,39):
                    if i==26:
                        yotei3+=(log[i]+":")
                    elif i==32:
                        yotei3+=(log[i]+"/")
                    else:
                        yotei3+=(log[i]+" ")
                yotei4=""
                for i in range(39,52):
                    if i==39:
                        yotei4+=(log[i]+":")
                    elif i==45:
                        yotei4+=(log[i]+"/")
                    else:
                        yotei4+=(log[i]+" ")
                yotei5=""
                for i in range(52,65):
                    if i==52:
                        yotei5+=(log[i]+":")
                    elif i==58:
                        yotei5+=(log[i]+"/")
                    else:
                        yotei5+=(log[i]+" ")
                yotei6=""
                for i in range(65,78):
                    if i==65:
                        yotei6+=(log[i]+":")
                    elif i==71:
                        yotei6+=(log[i]+"/")
                    else:
                        yotei6+=(log[i]+" ")
                yotei7=""
                for i in range(78,90:
                    if i==78:
                        yotei7+=(log[i]+":")
                    elif i==84:
                        yotei7+=(log[i]+"/")
                    else:
                        yotei7+=(log[i]+" ")

                await message.channel.send(yotei1)
                await message.channel.send(yotei2)
                await message.channel.send(yotei3)
                await message.channel.send(yotei4)
                await message.channel.send(yotei5)
                await message.channel.send(yotei6)
                await message.channel.send(yotei7)
                await message.channel.send(url)
            time.sleep(170)

def hei():
    dt_now = datetime.datetime.now()
    s_1=10
    s_2=19
    h=dt_now.hour
    if s_1==h or s_2==h:
        return True
    else:
        return False
def kyuu():
    dt_now = datetime.datetime.now()
    s_1=10
    s_2=18
    h=dt_now.hour
    if s_1==h or s_2==h:
        return True
    else:
        return False

client.run(token)
