import discord
from discord.ext import commands
#from main import Bolsadevalores.verify_channel
#from main import criar_conta
import requests as req
#from main import valor_acoes
import re
import os
from dotenv import load_dotenv, find_dotenv
#from main import add_fisrt_command_bonus

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
    if mem_id not in [830574674706432010, 838820527204204635, 838824492645875742, 838778634349182976]:
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

load_dotenv(find_dotenv())
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')

from pymongo import MongoClient
cluster = MongoClient(f'mongodb+srv://{user}:{password}{host}')
db = cluster['discord']
banco = db['banco']
conta = db['conta']
server = db['server']
membros = db['membros']

empresas = {"xpg":"XPGZX","amd":"AMD","nvidia":"NVDA","msi":"MSI","corsair":"CRSR","logitech":"LOGI","intel":"INTC","apple":"AAPL","google":"GOOG","tesla":"TSLA","netflix":"NFLX","ibm":"IBM"}
empresas_inverso = {"XPGZX":"xpg","AMD":"amd","NVDA":"nvidia","MSI":"msi","CRSR":"corsair","LOGI":"logitech","INTC":"intel","AAPL":"apple","GOOG":"google","TSLA":"tesla","NFLX":"netflix","IBM":"ibm"}


class Bolsadevalores(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    async def verify_channel(self, id, channels : None, msg: None):
        if id == 733851707800289340:
            await self.bot.get_channel(id).send('**Não é permitido o uso de comandos no chat <#733851707800289340>**')
            return False
        if id not in channels and len(channels) > 0:
            await self.bot.get_channel(id).send(msg)
            return False
        return True


    #===================================================
    #                   SISTEMA STOCKS                 =
    #===================================================

    @commands.command(aliases=['bolsa', 'bolsadevalores', 'mercado'])
    async def stocks(self, ctx):
        id = ctx.author.id
        if not await Bolsadevalores.verify_channel(self, ctx.channel.id, [842371888750657546, 828119245707411527, 830941514830053436], 'Você deve usar este comando no canal <#828119245707411527>'): return
        await add_fisrt_command_bonus(id)
        await ctx.send('coletando dados das empresas...', delete_after=1)
        first = conta.find_one({'_id':id})['firststockcommand']
        saldo = banco.find_one({'_id':id})['flerpoints']
        secure = False
        print(first)
        if first == 'True':
            await ctx.send(embed = discord.Embed(description = f'**Como essa foi sua primeira consulta, ela será gratuita. A partir da próxima, iremos cobrar uma taxa de 50 Flerpoints.**', color=0x018797))
            secure = True
        else:
            if saldo >= 50:
                banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':-50}})
                secure = True
            else:
                await ctx.channel.send(embed = discord.Embed(description = f'Você não tem flerpoints o suficientes para verificar a bolsa de valores', color=0xff0000))

        if secure == True:
            print('remove 50 flerpoints')
            embed = discord.Embed(title='BOLSA DE VALORES', description='Use f!comprar para comprar uma Ação, e f!vender para vender uma Ação\n\n', color=0x018797)
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/824275240623669251/828378765188792360/image-removebg-preview_11.png')
            embed.set_footer(text='Dica: Comprar Ações em baixa e vende-las quando estiverem em alta irá gerar lucro', icon_url='https://media.discordapp.net/attachments/824275240623669251/828381422779629608/image-removebg-preview_13.png')
            for i in empresas:
                empresa = valor_acoes(empresas[i])
                embed.add_field(name = f'<:btn:831216216571248730> {str(i).capitalize()} ({empresas[i]})', value = f'1 Ação = {empresa} FlerPoints', inline=True)
            await ctx.send(embed=embed)


    @commands.command()
    async def comprar(self, ctx, empresa = None, quant = None):       
        if not await Bolsadevalores.verify_channel(self, ctx.channel.id, [842371888750657546, 828119245707411527, 830941514830053436], 'Você deve usar este comando no canal <#828119245707411527>'): return
        id = ctx.author.id
        criar_conta(id)
        if empresa == None:
            await ctx.send("**Você precisa informar a ação que deseja comprar.\nEx: `f!comprar AMD 1`**")
        elif quant == None:
            await ctx.send("**Você precisa informar a quantidade de ações que deseja comprar \nEx: `f!comprar AMD 1`**")
        else:
            if not '-' in str(quant) and quant != 0:
                quant = int(quant)
                empresas_code = []
                for i in empresas:
                    empresas_code.append(empresas[i])
                if empresa not in empresas_code:
                    await ctx.send("**Você precisa informar qual ação deseja comprar corretamente.\nCopie e cole o código para garantir que está certo\n**")
                else:
                    valor = valor_acoes(empresa) 
                    if banco.find_one({"_id":id})['flerpoints'] >= valor * quant:
                        await ctx.channel.send(f'**Você comprou {quant} aç{"ão" if quant == 1 else "ões"} da empresa {empresas_inverso[empresa]}**')
                        banco.find_one_and_update({"_id":id}, {'$inc':{'flerpoints':(valor * quant) * -1}})
                        conta.find_one_and_update({"_id":id}, {'$inc':{'investido':valor * quant}})
                        
                        for i in range(0, quant):
                            conta.find_one_and_update({'_id':id}, {"$push":{"acoes":{f'{empresas_inverso[empresa]}' : f'**{empresas_inverso[empresa]} ({empresa})** - comprada por `{valor}` flerpoints', 'valor':valor, 'empresa':empresas_inverso[empresa]}}})
                    else:
                        await ctx.send("**Você não possui dinheiro o suficiente para comprar estas ações.**")
            else:
                await ctx.channel.send('**Como você vai comprar um valor negativo ou nulo?\nInforme um valor correto da próxima vez!**')


    @commands.command()
    async def vender(self, ctx, empresa = None, quant : int = None):
        if not await Bolsadevalores.verify_channel(self, ctx.channel.id, [842371888750657546, 828119245707411527, 830941514830053436], 'Você deve usar este comando no canal <#828119245707411527>'): return
        id = ctx.author.id
        criar_conta(id)
        if empresa == None:
            await ctx.send("**Você precisa informar a ação que deseja vender.\nEx: `f!vender AMD 1`**")
        elif quant == None:
            await ctx.send("**Você precisa informar a quantidade de ações que deseja vender \nEx: `f!vender AMD 1`**")
        else:
            if not '-' in str(quant) and quant != 0:
                quant = int(quant)
                empresas_code = []
                for i in empresas:
                    empresas_code.append(empresas[i])
                if empresa not in empresas_code:
                    await ctx.send("**Você precisa informar qual ação deseja vender corretamente.\nCopie e cole o código para garantir que está certo\n**")
                else:
                    valor = valor_acoes(empresa)
                    acoes_total = conta.find_one({'_id':id})['acoes']
                    safe = False
                    real_quant = 0
                    for i in range(0, len(acoes_total)):
                        if empresas_inverso[empresa] in acoes_total[i]:
                            safe = True
                            real_quant += 1
                    if safe == True:
                        if real_quant >= quant:
                            await ctx.channel.send(f'**Você vendeu {quant} aç{"ão" if quant == 1 else "ões"} da empresa {empresas_inverso[empresa]}**')
                            banco.find_one_and_update({"_id":id}, {"$inc":{'flerpoints':valor * quant}})
                            banco.find_one_and_update({'_id':id}, {"$inc":{'investido':(valor * quant) * -1}})
                            for e in range(0, quant):
                                index = None
                                for e in acoes_total:
                                    try:
                                        if empresas_inverso[empresa] in e[empresas_inverso[empresa]]:
                                            index = acoes_total.index(e)
                                            break
                                    except:
                                        pass
                                acoes_total.pop(index)
                                conta.find_one_and_update({'_id':id}, {'$set':{'acoes':acoes_total}})

                        else:   
                            await ctx.send("**Você não possui esta quantidade de ações. Compre mais para depois poder vende-las**")
                    else:
                        await ctx.send("**Você ainda não comprou está ação. Compre-a para depois poder vende-la**")
            else:
                await ctx.channel.send('**Como você vai vender um valor negativo ou nulo?\nInforme um valor correto da próxima vez!**')


    @commands.command(aliases=['ações'])
    async def acoes(self, ctx, member:discord.Member = None):
        if not await Bolsadevalores.verify_channel(self, ctx.channel.id, [842371888750657546, 828119245707411527, 830941514830053436], 'Você deve usar este comando no canal <#828119245707411527>'): return
        if member == None:
            id = ctx.author.id
        else:
            id = member.id
        criar_conta(id)
        user_acoes = conta.find_one({'_id':id})['acoes']
        print(user_acoes)
        apenas_acoes = []
        acoes_txt = ''
        jafoi = []

        #coleta somente a descrição das ações
        for i in user_acoes:
            empresa = i['empresa']
            apenas_acoes.append(i[empresa])
        
        #conta todas as ações e remove elas da lista em seguida
        for i in apenas_acoes:
            if i not in jafoi:
                jafoi.append(i)
                quant = apenas_acoes.count(i)
                plural_singular = 'ação' if quant == 1 else 'ações'
                print(i)
                i = f"`{quant}` {plural_singular} da empresa {i}"
                #adiciona as ações já agrupadas a um txt para enviar
                acoes_txt += f'{i}\n'

        import asyncio
        await asyncio.sleep(0.5)
        if acoes_txt == '':
            await ctx.channel.send('**Você ainda não possui nenhuma ação. Use f!stocks para poder olhar a bolsa de valores**')
        else:
            await ctx.channel.send(embed = discord.Embed(title = f'AÇÕES DE {str(ctx.author.name).upper()}', description = acoes_txt, color=0xFECD00))



def setup(bot):
    bot.add_cog(Bolsadevalores(bot))