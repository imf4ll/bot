import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
import requests as req
import datetime

load_dotenv(find_dotenv())
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')

from pymongo import MongoClient
cluster = MongoClient(f'mongodb+srv://{user}:{password}{host}')
#cluster = MongoClient('mongodb+srv://jv:1234@cluster0.cprce.mongodb.net/discord?retryWrites=true&w=majority')
db = cluster['discord']
banco = db['banco']
conta = db['conta']
server = db['server']
membros = db['membros']

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=[os.getenv('prefixo1'),os.getenv('prefixo2')], case_insensitive=True, intents=intents)
bot.remove_command('help')

async def verify_channel(id, channels : None, msg: None):
    if id == 733851707800289340:
        await bot.get_channel(id).send('**Não é permitido o uso de comandos no chat <#733851707800289340>**')
        return False
    if id not in channels and len(channels) > 0:
        await bot.get_channel(id).send(msg)
        return False
    return True

def valor_acoes(empresaa):
    '''
    empresa = stockquotes.Stock(empresaa)
    empresa = empresa.current_price
    empresa = int(empresa)
    '''
    url = f"https://yahoo-finance-low-latency.p.rapidapi.com/v11/finance/quoteSummary/{empresaa}"
    querystring = {"modules":"price"}

    headers = {
        'x-rapidapi-key': "b8ca806180msh9819c3532b69915p109b67jsn604f85fa74f8",
        'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
        }
    empresa = req.request("GET", url, headers=headers, params=querystring)
    empresa = empresa.json()['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw'] * 10
    return int(empresa)


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


async def add_fisrt_command_bonus(mem_id):
    try:
        frst_cmd = conta.find_one({'_id':mem_id})['firststockcommand']
    except:
        conta.find_one_and_update({'_id':mem_id}, {'$set':{'firststockcommand':'True'}})



@bot.event
async def on_ready():

    print('@================@')
    print('     BOT ONLINE   ')
    print('@================@')

    dlz = bot.get_channel(816164215932715028)
    #await dlz.send('<@401549060487774208> dlz seu delicia, usa esses comandos aqui:\nf!setup1\nf!setup2\nf!setup3\nf!setup4\nf!setup5')
    for i in os.listdir('./cogs'):
        for e in os.listdir(f'./cogs/{i}'):
            if str(e).startswith('__py'):
                pass
            else:
                print('loaded ', e)
                bot.load_extension(f'cogs.{i}.{e[:-3]}')


    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Feito por jv#2121 | Beta 1.1.22", type=3))
        hr1 = datetime.datetime.now()
        hr = hr1.strftime("%H%M")
        hr_precisa = hr1.strftime("%H%M%S")
        if str(hr) == '1402' or str(hr) == '1404' or str(hr) == '2202' or str(hr) == '2204':
            print('falei entrei')
            canal = bot.get_channel(827689497806372904)
            voice = await canal.connect() 
            voice.play(discord.FFmpegPCMAudio(f'inicio_mineracao.mp3'), after=lambda e: a)
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1.0
            await asyncio.sleep(35)                #tempo do audio
            await voice.disconnect()
            await asyncio.sleep(61)
        elif str(hr) == '1559' or str(hr) == '2359':
            print('falei sai')
            canal = bot.get_channel(827689497806372904)
            try:
                voice = await canal.connect() 
                voice.play(discord.FFmpegPCMAudio(f'fim_mineracao.mp3'), after=lambda e: a)
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 1.0
                await asyncio.sleep(9)                #tempo do audio
                await voice.disconnect()
                members = canal.members
                for mem in members:
                    await mem.edit(voice_channel=None)
                await asyncio.sleep(61)
            except:
                members = canal.members
                for mem in members:
                    await mem.edit(voice_channel=None)
                await asyncio.sleep(61)

        dia = datetime.date.today()
        if int(dia.day) == 1 and str(hr_precisa) == '030100':
            for i in conta.find({}):
                #só irá resetar os logins das pessoas que já possuem mais de 1 login, para consumir menos recursos
                if i['logins'] != 0:
                    conta.find_one_and_update({'_id':i['_id']}, {'$set':{'logins':0}})
                    await asyncio.sleep(1)

        server.find_one_and_update({'_id':0}, {'$set':{'ultimo_ping':hr1}})
        await asyncio.sleep(5)

        

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