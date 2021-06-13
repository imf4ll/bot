import discord
from discord.ext import commands
import os
import dotenv
import asyncio

load_dotenv(find_dotenv())

from pymongo import MongoClient
cluster = MongoClient(f'')
db = cluster['codify']
conta = db['conta']

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='.', case_insensitive=True, intents=intents)
bot.remove_command('help')

async def verify_channel(id, channels : None, msg: None):
    if id == 733851707800289340:
        await bot.get_channel(id).send('**Não é permitido o uso de comandos no chat <#733851707800289340>**')
        return False
    if id not in channels and len(channels) > 0:
        await bot.get_channel(id).send(msg)
        return False
    return True

def criar_conta(mem_id):
    if mem_id != 830574674706432010:
        try:
            banco.insert_one({"_id":mem_id, "flercoins":0, "flerpoints":0})
        except:
            pass
        try:    
            conta.insert_one({"_id":mem_id, "descricao":"Use f!descricao para alterar a sua descrição", "warnings":[], 'xp':0, "level":0, "acoes":[],"investido":0, "voice":{"t_entrou":0, "t_saiu":0}, "logins":0, "ultimoslotmachine":1101, "bonus":"False", 'ultimologin':1101, "totalinvites":0,"invites":0})
        except:
            pass
        try:
            server.insert_one({"_id":0, "bump":"False", "ids":[]})
        except:
            pass


@bot.event
async def on_ready():

    print('@================@')
    print('     BOT ONLINE   ')
    print('@================@')

    for i in os.listdir('./cogs'):
        for e in os.listdir(f'./cogs/{i}'):
            if str(e).startswith('__py'):
                pass
            else:
                print('loaded ', e)
                bot.load_extension(f'cogs.{i}.{e[:-3]}')


    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Codify Community", type=3))
        await asyncio.sleep(30)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=".help | discord.gg/codify", type=3))
        await asyncio.sleep(30)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Beta 0.0.1", type=3))


def _reload():
    for i in os.listdir('./cogs'):
        for e in os.listdir(f'./cogs/{i}'):
            if str(e).startswith('__py'):
                pass
            else:
                bot.unload_extension(f'cogs.{i}.{e[:-3]}')
                bot.load_extension(f'cogs.{i}.{e[:-3]}')
                print('reloaded ', e)

@bot.command()
async def reload(ctx):
    _reload()

bot.run(os.getenv('token'))