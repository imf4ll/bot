import discord
from discord.ext import commands
#from main import verify_channel
#from main import criar_conta
import requests as req
import datetime 
import os
import asyncio
from random import randint, choice
from dotenv import load_dotenv, find_dotenv

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


class Eventos(commands.Cog):
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
    #                     AVALIAÇÃO                    =
    #                                                  =
    #                       TICKET                     =
    #===================================================
    def check(self, author):
        def inner_check(message):
            return message.author == author
        return inner_check

    @commands.Cog.listener()
    async def on_message(self, message):
        id = message.author.id
        criar_conta(id)

        if message.channel.id == 627936554488299521 and message.author.id != self.bot.user.id:
            canal = self.bot.get_channel(627936554488299521)
            msg = message.content
            autor = message.author.name
            await message.channel.purge(limit=1)
            em = discord.Embed(title=f'SUGESTÃO DE: {autor}', description =f'\n**Sugestão:**\n{msg}\n\nPara enviar sua sugestão, apenas enscreva ela neste canal.', color=0xFECD00)
            sugest = await canal.send(embed=em)
            await sugest.add_reaction('✅')
            await sugest.add_reaction('⛔')

        if message.channel.id == 822928355929096232 and message.author.id != self.bot.user.id:
            canal = self.bot.get_channel(822928355929096232)
            msg = message.content
            autor = message.author.name
            await message.channel.purge(limit=1)
            em = discord.Embed(title=f'BUG REPORT DE: {autor}', description =f'\n**Bug:**{msg}\n\n[🔴] -> Bug em Correção! \n[🟢] -> Bug Corrigido!\n [🔵]-> Bug já Reportado!\n[⚪] -> Não é Bug!\nPara enviar seu bug report, apenas enscreva ele neste canal.', color=0xFECD00)
            em2 = discord.Embed(title=f'BUG REPORT DE: {autor}', description =f'\n**Bug:**{msg}\n\n[🟡] -> Prioridade Baixa \n[🟠] -> Prioridade Média \n[🔴] -> Prioridade Alta')
            sugest = await canal.send(embed=em)
            await sugest.add_reaction('🔴')
            global canal_bug, embed_bug_original, embed_bug, embed_bug1, embed_bug2, embed_bug3, msg_bug
            msg_bug = msg
            embed_bug_original = em
            embed_bug = em2
            canal_bug = self.bot.get_channel(838590913911062528)
            embed_bug1 = discord.Embed(title=f'BUG REPORT DE: {autor}', description =f'\n**Bug:**{msg}\n\n**Prioridade Baixa**\n\nReaja com ✅ para enviar para <#838584441836142683>', color=0x78B159)
            embed_bug2 = discord.Embed(title=f'BUG REPORT DE: {autor}', description =f'\n**Bug:**{msg}\n\n**Prioridade Média**\n\nReaja com ✅ para enviar para <#838584441836142683>', color=0xFDCB58)
            embed_bug3 = discord.Embed(title=f'BUG REPORT DE: {autor}', description =f'\n**Bug:**{msg}\n\n**Prioridade Alta**\n\nReaja com ✅ para enviar para <#838584441836142683>', color=0xDD2E44)



        if message.channel.id == 828403860333920277 or message.channel.id == 828403815770357800 or message.channel.id == 828403901585817600 or message.channel.id == 828408442011123743 and message.author.id != self.bot.user.id:
            canal = self.bot.get_channel(828781766781042699)
            msg = message.content
            await message.add_reaction('<a:verde:828431637763063829>')
            await message.add_reaction('<a:amarelo:828431636718419978>')
            await message.add_reaction('<a:vermelho:828431638135832616>')


        if message.channel.id == 820261179804483634:
            for i in ['🎟️','<:progamer:814957034096033792>','<:gamer:814957022318952459>','<:near:814957009932648459>','<:starter:814956993571192893>','🧱']:
                await message.add_reaction(i)

        if message.content.lower() != 'f!xp' and message.author.id != self.bot.user.id:
            criar_conta(id)
            conta.find_one_and_update({'_id':id}, {'$inc':{'xp':1}})
    
        if f"<@!{self.bot.user.id}>" in message.content and message.author.id !=self.bot.user.id:
            channel = message.channel
            em = discord.Embed(title='ME CHAMOU ?', description='Opa, tudo bem ? Eu sou o bot ofical da **Enifler!**.\n\nEstá precisando de ajuda? utilize: `f!help`', color=0xFECD00)
            em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')
            await channel.send(embed = em)
        '''
        if message.content.lower().startswith('f!avaliar') and message.author.id != self.bot.user.id:
            criar_conta(id)
            _save()
            channel = message.channel
            feedback = self.bot.get_channel(822928606283694130)

            await message.author.send('Titulo da avaliação: ')
            prod_msg = await self.bot.wait_for('message', check=Eventos.check(self, message.author), timeout=3600)
            prod = prod_msg.content

            await message.author.send('Quantas estrelas você daria(0 a 10): ')
            nota_msg = await self.bot.wait_for('message', check=Eventos.check(self, message.author), timeout=3600)
            nota = nota_msg.content

            await message.author.send('Comentário: ')
            comt_msg = await self.bot.wait_for('message', check=Eventos.check(self, message.author), timeout=3600)
            comt = comt_msg.content

            em = discord.Embed(title = f'AVALIACÃO DE {str(message.author).upper()}:', description = f'**Titulo: **{prod}\n\n**Estrelas: **{nota}/10\n\n**Comentário: **{comt}', footer = f'Bot feito por: jv#8472', color=0xFECD00)
            em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')
            await feedback.send(embed=em)
        '''
        if message.content.lower().startswith('f!comunidade') and message.author.id != self.bot.user.id:
            canal = self.bot.get_channel(822791876117659709)
            embed = discord.Embed(title = 'Sistema de forum da comunidade', description = 'Reaja com 📩 para criar um canal do forum da comunidade',color = 0xFECD00)
            embed.set_footer(text="Sistema de da comunidade - Enifler")
            msg = await canal.send(embed=embed)
            await msg.add_reaction("📩")

        if message.content.lower().startswith('f!ticket') and message.author.id != self.bot.user.id:
            canal = self.bot.get_channel(733881091919970374)
            embed = discord.Embed(title = 'Sistema de Suporte', description = 'Reaja com ✉️ para criar um canal de suporte',color = 0xFECD00)
            embed.set_footer(text="Sistema de suporte - Enifler")
            msg = await canal.send(embed=embed)
            await msg.add_reaction("✉️")

        
        if message.content.lower().startswith('f!denuncia') and message.author.id != self.bot.user.id:
            canal = self.bot.get_channel(733881048739610655)
            embed = discord.Embed(title = 'Sistema de Suporte', description = 'Reaja com ✍ para criar um canal de denuncias (privado)',color = 0xFECD00)
            embed.set_footer(text="Sistema de suporte - Enifler")
            msg = await canal.send(embed=embed)
            await msg.add_reaction("✍")
    

        #da as moedas por ranking
        if message.author.id != self.bot.user.id:
            canal = self.bot.get_channel(827710251649728592)
            xp = conta.find_one({'_id':id})['xp']
            if xp == 1000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':1}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 1 !')#\nComo recompensa, aqui estão 1000 flerpoints.')
                #banco[id]['flerpoints'] += 1000
            elif xp == 2000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':2}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 2 !')#\nComo recompensa, aqui estão 2000 flerpoints.')
                #banco[id]['flerpoints'] += 2000
            elif xp == 3000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':3}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 3 !')#\nComo recompensa, aqui estão 3000 flerpoints.')
                #banco[id]['flerpoints'] += 3000
            elif xp == 4000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':4}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 4 !')#\nComo recompensa, aqui estão 4000 flerpoints.')
                #banco[id]['flerpoints'] += 4000
            elif xp == 5000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':5}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 5 !')#\nComo recompensa, aqui estão 5000 flerpoints.')
                role = message.guild.get_role(816107551879987210)
                await message.author.add_roles(role)
                #banco[id]['flerpoints'] += 5000
            elif xp == 6000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':6}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 6 !')#\nComo recompensa, aqui estão 6000 flerpoints.')
                #banco[id]['flerpoints'] += 6000
            elif xp == 7000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':7}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 7 !')#\nComo recompensa, aqui estão 7000 flerpoints.')
                #banco[id]['flerpoints'] += 7000
            elif xp == 8000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':8}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 8 !')#\nComo recompensa, aqui estão 8000 flerpoints.')
                #banco[id]['flerpoints'] += 8000
            elif xp == 9000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':9}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 9 !')#\nComo recompensa, aqui estão 9000 flerpoints.')
                #banco[id]['flerpoints'] += 9000
            elif xp == 10000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':10}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 10 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
                role = message.guild.get_role(816107632905289728)
                await message.author.add_roles(role)
            elif xp == 11000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':11}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 11 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 12000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':12}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 12 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 13000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':13}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 13 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 14000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':14}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 14 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 15000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':15}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 15 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
                role = message.guild.get_role(826543521162199101)
                await message.author.add_roles(role)
            elif xp == 16000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':16}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 16 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 17000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':17}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 17 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 18000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':18}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 18 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 19000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':19}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 19 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 20000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':20}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 20 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
                role = message.guild.get_role(816107646959747094)
                await message.author.add_roles(role)
            elif xp == 21000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':21}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 21 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 22000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':22}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 22 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 23000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':23}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 23 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 24000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':24}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 24 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 25000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':25}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 25 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 26000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':26}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 26 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 27000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':27}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 27 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 28000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':28}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 28 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 29000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':29}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 29 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 30000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':30}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 30 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
                role = message.guild.get_role(816107677289676851)
                await message.author.add_roles(role)
            elif xp == 31000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':31}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 31 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 32000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':32}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 32 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 33000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':33}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 33 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 34000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':34}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 34 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 35000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':35}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 35 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 36000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':36}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 36 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 37000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':37}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 37 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 38000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':38}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 38 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 39000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':39}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 39 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
            elif xp == 40000:
                conta.find_one_and_update({'_id':id}, {'$set':{'level':40}})
                await canal.send(f'Parabéns, {message.author.mention} você passou para o nível 40 !')#\nComo recompensa, aqui estão 10000 flerpoints.')
                #banco[id]['flerpoints'] += 10000
                role = message.guild.get_role(828046112366657557)
                await message.author.add_roles(role)

        if message.content.lower() == '!d bump':
            hr = datetime.datetime.now()
            hr_bump = server.find_one({'_id':0})['bump']
            dif = datetime.datetime.now() - server.find_one({'_id':0})['bump']
            dif = str(dif)[:-7].replace(':', '')
            dif = int(dif)
            if dif > 20000:
                await message.channel.send(f'**Parabéns {message.author.mention}, você ganhou 80 flerpoints por ter dado Bump no server.**\nVolte daqui 2 horas para poder bumpar novamente')
                banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':80}})
                server.find_one_and_update({'_id':0}, {'$set':{'bump':datetime.datetime.now()}})
            else:
                await message.channel.send(f'{message.author.mention}, o servidor já foi bumpado\nEspere até que o cooldown do bot acabe para tentar novamente.')


        #   await self.bot.process_commands(message)


    #===================================================
    #                 MINERAR FLERPOINTS               =
    #===================================================

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after, self_deaf=True, self_mute=True):
        id = member.id
        criar_conta(id)
        minerando = self.bot.get_channel(828483579880538122)
        await asyncio.sleep(1)
        hr1 = datetime.datetime.now()
        hr = int(hr1.strftime('%H%M'))
        if (before.channel is None or before.channel is not None) and after.channel is not None:
            deaf = member.voice.self_deaf
            if deaf == True and after.channel.id == 827689497806372904:
                await minerando.send(f'**{member.mention}, você precisa habilitar o áudio para minerar. Clique no emoji de Headphone para poder ativa-lo novamente**')
                await member.edit(voice_channel=None)
                conta.find_one_and_update({'_id':id}, {'$set':{'deaf':'True'}})
            else:
                conta.find_one_and_update({'_id':id}, {'$set':{'deaf':'False'}})
            if after.channel.name == '💰・Minerando...':
                if hr >= 1400 and hr <= 1600 or hr >= 2200 and hr <= 2359:
                #if hr >= 1100 and hr <= 1600 or hr >= 1900 and hr <= 2200:
                    conta.find_one_and_update({'_id':id}, {"$set":{"voice.t_entrou":hr}})
                    server.find_one_and_update({'_id':0}, {"$set":{'h_falso':"False"}})
                else:
                    await minerando.send(embed=discord.Embed(description = f'**{member.mention} | O chat de voz `minerando` ainda não está aberto**\n**volte novamente das 11:00 até 13:00 ou das 19:00 até 21:00**', color=0xFECD00))
                    await member.edit(voice_channel=None)
                    server.find_one_and_update({'_id':0}, {"$set":{'h_falso':"True"}})

        if before.channel is not None and (after.channel is None or after.channel is not None):
            try:
                if before.channel.name == '💰・Minerando...' and conta.find_one({'_id':id})['deaf'] == 'False':
                    if server.find_one({'_id':0})['h_falso'] == "False":
                        hr1 = datetime.datetime.now()
                        conta.find_one_and_update({'_id':id}, {"$set":{"voice.t_saiu":hr}})
                        flerpoints_total = int(conta.find_one({'_id':id})['voice']['t_saiu']) - int(conta.find_one({'_id':id})['voice']['t_entrou'])
                        if flerpoints_total <= 2: 
                            await minerando.send(embed=discord.Embed(description = f'**{member.mention} | Você precisa ficar pelo menos 2 minutos minerando para poder ganhar FlerPoints**', color=0xFECD00))
                        else:
                            if conta.find_one({'_id':id})['deaf'] == 'False':
                                banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints': int(int(flerpoints_total) * 0.5)}})
                                em = discord.Embed(title='FARMING DE FLERPOINTS', description = f'{member.name} **conseguiu {int(int(flerpoints_total) * 0.5)} de FlerPoints** por **ter ficado {flerpoints_total} minutos em call**.\nAgora ele **está com {banco.find_one({"_id":id})["flerpoints"]} de FlerPoints**.', color = 0xFECD00)
                                em.set_thumbnail(url='https://cdn.discordapp.com/attachments/816402333117972480/825369922208137226/FlerPoints.png')
                                await minerando.send(member.mention)
                                await minerando.send(embed=em)
            except:
                pass
    


    #===================================================
    #                  REACTION TICKET                 =
    #                  TROCAR CONVITES                 =
    #===================================================
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)   
    async def login(self, ctx):
        id = ctx.author.id
        criar_conta(id)
        em = discord.Embed(title='LOGIN DIÁRIO', description='Reaja com 🎁 para fazer seu Check-in.\nVolte todos os dias para continuar resgatando!', color=0xFECD00)
        em.set_thumbnail(url='https://images-ext-1.discordapp.net/external/C9qJQJDu693i6B9Ii1aYgM5mvifMf9NsPhchO3txb6w/https/images.vexels.com/media/users/3/146457/isolated/preview/2bba99c4323c66745b5584ef7a1163a2-open-red-wrap-gift-box-by-vexels.png')
        
        lg = await ctx.channel.send(embed=em)
        await lg.add_reaction('🎁')

    emojis = ['🍇','🍉','🍊','🥧','🍺','💵','💰','🦠','❤️','🛑']

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)   
    async def slotmachine(self, ctx):
        id = ctx.author.id
        criar_conta(id)
        em = discord.Embed(title='SLOT MACHINE', description='Reaja com 🎰 para jogar. Se os 3 simbolos forem iguais, você ganha!\nVolte todos os dias para continuar resgatando!', color=0xFECD00)
        em.set_thumbnail(url='https://media.discordapp.net/attachments/816402333117972480/830857950666424321/slot_machine.png')
        
        sm = await ctx.channel.send(embed=em)
        await sm.add_reaction('🎰')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        id = user.id
        criar_conta(id)
        guild = reaction.message.guild
        msg = reaction.message
        global autor_react
        autor_react = user.id

        if user.id != self.bot.user.id and reaction.emoji == '💸':
            totalInvites = 0
            for i in await user.guild.invites():
                if i.inviter == user:
                    totalInvites += i.uses
            em = discord.Embed(title = 'RECOMPENAS POR INVITES', description = '**1 Invite = 100 flerpoints\n5 Invites = 200 flerpoints\n10 Invites = 300 flerpoints\n15 Invites = 400 flerpoints\n20 Invites = 500 flerpoints**\n\nReaja com 🆙 para resgatar seus flerpoints', color=0xFECD00)
            em.set_thumbnail(url='https://media.discordapp.net/attachments/824275240623669251/828458487028908072/flerpoints3.png')
            loja = await reaction.message.channel.send(embed=em)
            await loja.add_reaction('🆙')
        if user.id != self.bot.user.id and reaction.emoji == '🆙':
            totalInvites = 0
            for i in await user.guild.invites():
                if i.inviter == user:
                    totalInvites += i.uses
            if totalInvites >= 1 and totalInvites < 5 and conta.find_one({"_id":id})["invites"] < 1:
                banco.find_one_and_update({'_id':id}, {"$inc":{"flerpoints":100}})
                conta.find_one_and_update({'_id':id}, {"$set":{"invites":1}})
                await reaction.message.channel.send(f'**Parabéns {user.mention}. Você recebeu 100 FlerPoint{"s" if totalInvites > 1 else ""} por ter {totalInvites} invite{"s" if totalInvites > 1 else ""}. Convide mais amigos para continuar resgatando prêmios!**')
            elif totalInvites >= 5 and totalInvites < 10 and conta.find_one({"_id":id})["invites"] < 5:
                banco.find_one_and_update({'_id':id}, {"$inc":{"flerpoints":300}})
                conta.find_one_and_update({'_id':id}, {"$set":{"invites":5}})
                await reaction.message.channel.send(f'**Parabéns {user.mention}. Você recebeu 200 FlerPoint{"s" if totalInvites > 1 else ""} por ter {totalInvites} invite{"s" if totalInvites > 1 else ""}. Convide mais amigos para continuar resgatando prêmios!**')
            elif totalInvites >= 10 and totalInvites < 15 and conta.find_one({"_id":id})["invites"] < 10:
                banco.find_one_and_update({'_id':id}, {"$inc":{"flerpoints":600}})
                conta.find_one_and_update({'_id':id}, {"$set":{"invites":10}})
                await reaction.message.channel.send(f'**Parabéns {user.mention}. Você recebeu 300 FlerPoint{"s" if totalInvites > 1 else ""} por ter {totalInvites} invite{"s" if totalInvites > 1 else ""}. Convide mais amigos para continuar resgatando prêmios!**')
            elif totalInvites >= 15 and totalInvites < 20 and conta.find_one({"_id":id})["invites"] < 15:
                banco.find_one_and_update({'_id':id}, {"$inc":{"flerpoints":1000}})
                conta.find_one_and_update({'_id':id}, {"$set":{"invites":15}})
                await reaction.message.channel.send(f'**Parabéns {user.mention}. Você recebeu 400 FlerPoint{"s" if totalInvites > 1 else ""} por ter {totalInvites} invite{"s" if totalInvites > 1 else ""}. Convide mais amigos para continuar resgatando prêmios!**')
            elif totalInvites >= 20 and conta.find_one({"_id":id})["invites"] < 20:
                banco.find_one_and_update({'_id':id}, {"$inc":{"flerpoints":1500}})
                conta.find_one_and_update({'_id':id}, {"$set":{"invites":20}})
                await reaction.message.channel.send(f'**Parabéns {user.mention}. Você recebeu 500 FlerPoint{"s" if totalInvites > 1 else ""} por ter {totalInvites} invite{"s" if totalInvites > 1 else ""}. Convide mais amigos para continuar resgatando prêmios!**')



    #===================================================
    #                 CONVITES E RECEPÇÃO              =
    #===================================================
    @commands.command()
    async def invites(self, ctx, user = None):
        id = ctx.author.id
        criar_conta(id)
        if not await Eventos.verify_channel(self, ctx.channel.id, [], ''): return

        if user == None:
            total_invites = 0
            for i in await ctx.guild.invites():
                if i.inviter == ctx.author:
                    total_invites += i.uses
            em = discord.Embed(title='INVITES', description =f'Você possui {total_invites}  convite{"" if total_invites == 1 else "s"}!\n\nReaja com 💸 para poder trocar seus invites por flerpoints', color=0xFECD00)
            em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')
            loja = await ctx.send(embed=em)
            await loja.add_reaction('💸')
        else:
            total_invites = conta[str(user.id)]['totalinvites']
            em = discord.Embed(title='INVITES', description =f'{user.mention} possui {total_invites} convite{"" if total_invites == 1 else "s"}!\n\nReaja com 💸 para poder trocar seus invites por flerpoints', color=0xFECD00)
            em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')
            loja = await ctx.send(embed=em)
            await loja.add_reaction('💸')
        

    @commands.Cog.listener()
    async def on_member_join(self, member):
        em = discord.Embed(title='SEJA BEM VINDO', description=f'Seja bem vindo {member.name}!', color=0xFECD00)
        em.set_thumbnail(url=member.avatar_url)
        recepcao = self.bot.get_channel(733698208647086172)
        await recepcao.send(embed=em)
        '''
        id = member.id
        criar_conta(id)
        membros.find_one_and_update({'_id':0}, {'$push':{'ids':id}})
        for i in await member.guild.invites():
            for e in membros.find_one({}):
                if str(member.id) not in e:
                    conta.find_one_and_update({"_id":i.inviter.id}, {"$inc":{'totalinvites':1}})
        id = member.id
        criar_conta(id)
        user_name = member.name + '#' + member.discriminator
        url = req.get(member.avatar_url)
        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((311, 311))
        

        bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)
        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('./temp/avatar.png')
        avatar = Image.open('./temp/avatar.png')
        background = Image.open('./img/bem_vindo_background.png')
        background.paste(avatar, (50,48), avatar)   

        draw = ImageDraw.Draw(background)

        font = ImageFont.truetype('./fonts/LEMONMILK-Bold.otf', 38)
        font_s = ImageFont.truetype('./fonts/LEMONMILK-Light.otf', 30)

        #draw.text((25,375), user_name, font=font, fill='#fff')
        MAX_W, MAX_H = 420, 383
        para = textwrap.wrap(user_name, width=20)
        current_h, pad = 383, 10    
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill='white')
            current_h += h + pad

        background.save('temp/temp_bem_vindo.png', format='PNG')
        ft = discord.File(open('temp/temp_bem_vindo.png', 'rb'))
        recepcao = self.bot.get_channel(733698208647086172)
        await recepcao.send(member.mention, file=ft)
        '''

    @commands.command()
    async def getids(self, ctx):
        await ctx.send('coletando dados, aguarde...')
        users_ja_cadastrados = 0
        users_cadastrados = 0
        for member in self.bot.get_all_members():
            if str(member.id) not in membros['ids']:
                membros.find_one_and_update({'_id':0}, {'$push':{'ids':member.id}}) 
                users_cadastrados += 1
                await asyncio.sleep(randint(3,5))
            else:
                users_ja_cadastrados += 1
        await ctx.channel.send(f'cadastrei {users_cadastrados} novos usuários no banco de dados.{users_ja_cadastrados} deles já estavam cadastrados')


    #===================================================
    #                     REACTIONS                    =
    #===================================================
    @commands.command()
    async def registro(self, ctx):
        await ctx.channel.send("https://images-ext-2.discordapp.net/external/swYbcM_SAxWOTGB2nKAoI0ngeq-umq9CNVpIJXKt5u4/%3Fwidth%3D1455%26height%3D328/https/media.discordapp.net/attachments/816402333117972480/830163225869287424/registre-se.png")
        em = discord.Embed(title='▾ ━━━━━━ 🔹 Categorias  🔹 ━━━━━━ ▾', description='\n\n   **ESCOLHA A CATEGORIA QUE VOCÊ MAIS SE IDENTIFICA!\n\n[🖥️] <@&830136741285068801> -> Se você gosta de HARDWARE, e quer ser notificado com noticias de hardware e ainda ter privilégios no servidor?! Então esta categoria será perfeita para você!\n\n[🎮] <@&830136856137695260> -> Se você gosta de GAMES, e quer ser notificado com noticias de jogos da atualidade e sobre hardware que rode jogos e ter privilégios no servidor?! Então esta categoria será perfeita para você!\n\n[📂] <@&830136908843188294> -> Se você gosta de SOFTWARE , e quer ser notificado com noticias da área de Tecnologia, e ainda por cima, ter privilégios e acesso exclusivo no servidor?! Então esta categoria será perfeita para você!\n\n\n▾ ━━━━━━━ 🔹 Notificações 🔹 ━━━━━━━ ▾\n\n\n🔔 NUNCA PERCA NENHUMA NOVIDADE!\n\n[🔴] <@&830124900253171782> -> Para Receber todas as notificações do Canal Enifler!\n\n[🟠] <@&828275608458887218> -> Para Receber todas as notificações do Servidor!\n\n[🟣] <@&828274624001343559> -> Para Receber todas as notificações de Hardware e Promoções!\n\n[🔵] <@&828273763396354068> -> Para Receber todas as notificações sobre Jogos!\n\n[🟢] <@&828274625179287582> -> Para Receber todas as notificações sobre a área da Tecnologia!**\n\n▴ ━━━━━━━━━━ 🔹 ━━━━━━━━━━━ ▴', color=0xFECD00)
        em.set_image(url='https://images-ext-2.discordapp.net/external/swYbcM_SAxWOTGB2nKAoI0ngeq-umq9CNVpIJXKt5u4/%3Fwidth%3D1455%26height%3D328/https/media.discordapp.net/attachments/816402333117972480/830163225869287424/registre-se.png')
        msg = await ctx.channel.send(embed=em)
        for i in ['🖥️','🎮','📂','🔴','🟠','🟣','🔵','🟢']:
            await msg.add_reaction(i)
        em2 = discord.Embed(title='▾ ━━━━━━ 🔹 Finalizar Registro 🔹 ━━━━━━ ▾', description='**ATENÇÃO, ANTES DE FINALIZAR, CERTIFIQUE-SE QUE VOCÊ\nCONCORDA COM TODAS AS REGRAS E TERMOS!\n\nPara Ler as Regras e Termos, Acesse o Canal <#626946932690124801>!\n\nPara Finalizar seu Registro, Por Favor reaga com  [✅]  Para se\nTornar Oficialmente um <@&826548329411379280>  dessa incrível Comunidade!\n\n▴ ━━━━━━━━━━ 🔹  ━━━━━━━━━━━ ▴**', color=0xFECD00)
        msg2 = await ctx.channel.send(embed=em2)
        await msg2.add_reaction('✅')


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await message.guild.fetch_member(payload.user_id)
        guild = message.guild
        mem = self.bot.get_user(user.id)
        emoji = str(payload.emoji)
        id = user.id
        criar_conta(user.id)
        try:
            if emoji == '💎':
                await mem.send('💎')
                print('💎')
            elif emoji == '💰':
                await mem.send('💰')
                print('💰')
        except:
            pass

        if channel.id == 832974447530213386:
            if emoji == '<:verified_2:842553583081357362>':
                carg1 = message.guild.get_role(842005195357159434)
                await user.add_roles(carg1)

        if channel.id == 734069866037903440:
            if emoji == '🎮':
                carg1 = message.guild.get_role(830136856137695260)
                await user.add_roles(carg1)
            
            elif emoji == '🖥️':
                carg2 = message.guild.get_role(830136741285068801)
                await user.add_roles(carg2)
        
            elif emoji == '📂':
                carg3 = message.guild.get_role(830136908843188294)
                await user.add_roles(carg3)
            elif emoji == '✅':
                carg4 = message.guild.get_role(826548329411379280)
                criar_conta(user.id)
                if conta.find_one({'_id':id})['bonus'] == "False":
                    banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':100}})
                    conta.find_one_and_update({'_id':id}, {'$set':{'bonus':"True"}})
                    canal = self.bot.get_channel(828483579880538122)
                    await canal.send(embed=discord.Embed(description = f'**Parabéns <@{user.id}>, você ganhou um bônus de 100 FlerPoints por ter se registrado!**', color=0xFECD00))
                
                await user.add_roles(carg4)
            elif emoji == '🔴':
                carg5 = message.guild.get_role(830124900253171782)
                await user.add_roles(carg5)
            elif emoji == '🟠':
                carg6 = message.guild.get_role(828275608458887218)
                await user.add_roles(carg6)
            elif emoji == '🔵':
                carg7 = message.guild.get_role(828273763396354068)
                await user.add_roles(carg7)
            elif emoji == '🟣':
                carg8 = message.guild.get_role(828274624001343559)
                await user.add_roles(carg8)
            elif emoji == '🟢':
                carg9 = message.guild.get_role(828274625179287582)
                await user.add_roles(carg9)

        
        if user.id != self.bot.user.id:

            if emoji == '🎁' and user.id != self.bot.user.id:
                await message.clear_reaction('🎁')
                await message.add_reaction('🎁')
                data = datetime.date.today()
                dia = '0' + str(data.day) if len(str(data.day)) == 1 else '' + str(data.day)
                mes = '0' + str(data.month) if len(str(data.month)) == 1 else '' + str(data.month)
                data = str(dia) + str(mes)
                if conta.find_one({"_id":id})['ultimologin'] != data:
                    conta.find_one_and_update({'_id':id}, {'$inc':{'logins':1}})
                    server.find_one_and_update({'_id':0}, {'$push':{'logins':id}})
                    if conta.find_one({'_id':id})['logins'] == 5:
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':100}})
                        quant = 100
                        em = discord.Embed(title='LOGIN DIÁRIO', description =f'{user.mention}, Você recebeu {quant} flerpoints por ter feito seu {conta.find_one({"_id":id})["logins"]}º login diário.', color=0xFECD00)
                    elif conta.find_one({'_id':id})['logins'] == 10 :
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':250}})
                        quant = 250
                        em = discord.Embed(title='LOGIN DIÁRIO', description =f'{user.mention}, Você recebeu {quant} flerpoints por ter feito seu {conta.find_one({"_id":id})["logins"]}º login diário.', color=0xFECD00)
                    elif conta.find_one({'_id':id})['logins'] == 15:
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':400}})
                        quant = 400
                        em = discord.Embed(title='LOGIN DIÁRIO', description =f'{user.mention}, Você recebeu {quant} flerpoints por ter feito seu {conta.find_one({"_id":id})["logins"]}º login diário.', color=0xFECD00)
                    elif conta.find_one({'_id':id})['logins'] == 20:
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':550}})
                        quant = 550
                        em = discord.Embed(title='LOGIN DIÁRIO', description =f'{user.mention}, Você recebeu {quant} flerpoints por ter feito seu {conta.find_one({"_id":id})["logins"]}º login diário.', color=0xFECD00)
                    elif conta.find_one({'_id':id})['logins'] == 25:
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':700}})
                        quant = 700
                        em = discord.Embed(title='LOGIN DIÁRIO', description =f'{user.mention}, Você recebeu {quant} flerpoints por ter feito seu {conta.find_one({"_id":id})["logins"]}º login diário.', color=0xFECD00)
                    elif conta.find_one({'_id':id})['logins'] == 30:
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':800}})
                        quant = 800
                        em = discord.Embed(title='LOGIN DIÁRIO', description =f'{user.mention}, Você recebeu {quant} flerpoints por ter feito seu {conta.find_one({"_id":id})["logins"]}º login diário.', color=0xFECD00)
                    else:
                        em = discord.Embed(title='LOGIN DIÁRIO', description =f'{user.mention}, você ganhou +1 login! volte amanhã para logar novamente.\nVocê já possui {conta.find_one({"_id":id})["logins"]} logins.', color=0xFECD00)
                    em.set_thumbnail(url='https://media.discordapp.net/attachments/816402333117972480/825369890864496660/flerpoints3.png?width=670&height=670')
                    relatorios = self.bot.get_channel(828483579880538122)
                    await relatorios.send(embed = em)
                    await user.send(embed = em)
                    data = datetime.date.today()
                    dia = '0' + str(data.day) if len(str(data.day)) == 1 else '' + str(data.day)
                    mes = '0' + str(data.month) if len(str(data.month)) == 1 else '' + str(data.month)
                    data = str(dia) + str(mes)
                    conta.find_one_and_update({'_id':id}, {'$set':{'ultimologin':data}})
                else:
                    em = discord.Embed(title='LOGIN DIÁRIO', description =f'{user.mention}, você já fez seu login diário hoje.\nVolte amanhã para poder resgatar novamente.', color=0xFF0000)
                    em.set_thumbnail(url='https://media.discordapp.net/attachments/816402333117972480/825369890864496660/flerpoints3.png?width=670&height=670')

                    await user.send(embed=em)

            if emoji == '🎰' and user.id != self.bot.user.id:
                await message.clear_reaction('🎰')
                await message.add_reaction('🎰')
                data = datetime.date.today()
                dia = '0' + str(data.day) if len(str(data.day)) == 1 else '' + str(data.day)
                mes = '0' + str(data.month) if len(str(data.month)) == 1 else '' + str(data.month)
                data = str(dia) + str(mes)
                if conta.find_one({"_id":id})['ultimoslotmachine'] != data:
                    relatorios = self.bot.get_channel(828483579880538122)
                    emojis = ['🍇','🍉','🍊','🥧','🍺','💵','💰','🦠','❤️','🛑']
                    if randint(1,20) == 20:
                        r = choice(emojis)
                        emoji1, emoji2, emoji3 = r, r, r
                    else:
                        emoji1, emoji2, emoji3 = choice(emojis), choice(emojis), choice(emojis)

                    if emoji1 == emoji2 and emoji2 == emoji3 and emoji3 == emoji1:
                        await user.send(embed=discord.Embed(title='VOCÊ GANHOU 500 FLERPOINTS', description = f'{user.mention}, O resultado foi {emoji1, emoji2, emoji3}\nVolte amanhã para tentar novamente!', color=0xFECD00))
                        await relatorios.send(embed=discord.Embed(title = 'VOCÊ GANHOU 500 FLERPOINTS', description = f'{user.mention}, O resultado foi {emoji1, emoji2, emoji3}\nVolte amanhã para tentar novamente!', color=0xFECD00))
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':500}})
                    else:
                        await user.send(embed=discord.Embed(title='VOCÊ PERDEU.', description = f'{user.mention}, O resultado foi {emoji1, emoji2, emoji3}\nVolte amanhã para tentar novamente!', color=0xFECD00))
                        await relatorios.send(embed=discord.Embed(title='VOCÊ PERDEU.', description = f'{user.mention}, O resultado foi {emoji1, emoji2, emoji3}\nVolte amanhã para tentar novamente!', color=0xFECD00))
                        data = datetime.date.today()
                        dia = '0' + str(data.day) if len(str(data.day)) == 1 else '' + str(data.day)
                        mes = '0' + str(data.month) if len(str(data.month)) == 1 else '' + str(data.month)
                        data = str(dia) + str(mes)
                        conta.find_one_and_update({'_id':id}, {'$set':{'ultimoslotmachine':data}})
                else:
                    await user.send(embed=discord.Embed(title='JOAGADA DIÁRIA', description =f'{user.mention}, você já Fez sua jogada diária.\nVolte amanhã para poder tentar novamente.', color=0xFF0000))
                    await relatorios.send(embed=discord.Embed(title='JOAGADA DIÁRIA', description =f'{user.mention}, você já Fez sua jogada diária.\nVolte amanhã para poder tentar novamente.', color=0xFF0000))
            if user.bot == True:
                return

            if emoji == '📩':
                await message.clear_reaction('📩')
                await message.add_reaction('📩')
                await user.send(f'Olá {str(user.name).capitalize()}, vim aqui te ajudar.\nAntes de tudo, poderia **escolher um nome**(curto) para o seu canal de suporte? ')
                title_suporte = await self.bot.wait_for('message', check=Eventos.check(self, user), timeout=3600)
                title = title_suporte.content

                canal1 = await guild.create_text_channel(name = f'❓・{title}')
                canal = self.bot.get_channel(int(canal1.id))

                await user.send('Ok, agora preciso de uma pequena descrição para poder informar o pessoal que irá te atender. Poderia me falar um pouco sobre? ')
                desc_suporte = await self.bot.wait_for('message', check=Eventos.check(self, user), timeout=3600)
                desc = desc_suporte.content

                em = discord.Embed(title = f'FORUM DA COMUNIDADE ({str(user.name).upper()})', description = f'O problema que o {user.name} está tendo é:\n{desc}\n\nReaja com ❌ para fechar e deletar este canal', color=0xFECD00)
                em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')
                
                geral = self.bot.get_channel(733851707800289340)
                await geral.send(f'O usuário <@{user.id}> está precisando de ajuda no canal <#{canal1.id}>. Você pode ajuda-lo?')

                await canal.send(f'{user.mention}')
                embed = await canal.send(embed=em)
                await embed.add_reaction('❌')
            if emoji == '✉️':
                await message.clear_reaction('✉️')
                await message.add_reaction('✉️')
                await user.send(f'Olá {str(user.name).capitalize()}, vim aqui te ajudar.\nAntes de tudo, poderia **escolher um nome**(curto) para o seu canal de suporte? ')
                title_suporte = await self.bot.wait_for('message', check=Eventos.check(self, user), timeout=3600)
                title = title_suporte.content

                membros = guild.get_role(826548329411379280)
                staff = guild.get_role(627970236158574593)
                supervisor = guild.get_role(815747932208496660)
                ajudante = guild.get_role(815747507358531604)

                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    membros: discord.PermissionOverwrite(read_messages=False),
                    user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                    staff: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                    supervisor: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                    ajudante: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                    }
                print(overwrites)
                
                canal1 = await guild.create_text_channel(name = f'❓・{title}', overwrites = overwrites)
                await asyncio.sleep(0.5)
                canal = self.bot.get_channel(int(canal1.id))

                await user.send('Ok, agora preciso de uma pequena descrição para poder informar o pessoal que irá te atender. Poderia me falar um pouco sobre? ')
                desc_suporte = await self.bot.wait_for('message', check=Eventos.check(self, user), timeout=3600)
                desc = desc_suporte.content

                em = discord.Embed(title = f'Canal de suporte para {str(user.name).upper()}:', description = f'O problema que o {user.name} está tendo é:\n{desc}\n\nReaja com ❌ para fechar e deletar este canal', color=0xFECD00)
                em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')

                await canal.send(f'@here')
                embed = await canal.send(embed=em)
                await embed.add_reaction('❌')
            if emoji == '❌' and user.id == autor_react:
                #await guild.delete_text_channel(name = f'❓・{reaction.message.channel.id}')
                await channel.send('**ESTE CANAL SERÁ FECHADO EM 10 SEGUNDOS**')
                time.sleep(10)
                membros = guild.get_role(826548329411379280)
                staff = guild.get_role(627970236158574593)
                supervisor = guild.get_role(815747932208496660)
                ajudante = guild.get_role(815747507358531604)
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    membros: discord.PermissionOverwrite(read_messages=False),
                    user: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                    staff: discord.PermissionOverwrite(read_messages=True, send_messages=False),
                    supervisor: discord.PermissionOverwrite(read_messages=True, send_messages=False),
                    ajudante: discord.PermissionOverwrite(read_messages=True, send_messages=False)
                    }
                existing_channel = self.bot.get_channel(channel.id)
                await existing_channel.edit(overwrites=overwrites)
            if emoji == '✍':
                await message.clear_reaction('✍')
                await message.add_reaction('✍')
                await user.send(f'Olá {str(user.name).capitalize()}, vim aqui te ajudar.\nAntes de tudo, poderia **escolher um nome**(curto) para o seu canal de denuncias? ')
                title_suporte = await self.bot.wait_for('message', check=Eventos.check(self, user), timeout=3600)
                title = title_suporte.content

                membros = guild.get_role(826548329411379280)
                staff = guild.get_role(627970236158574593)
                supervisor = guild.get_role(815747932208496660)
                ajudante = guild.get_role(815747507358531604)

                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    membros: discord.PermissionOverwrite(read_messages=False),
                    guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                    staff: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                    supervisor: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                    ajudante: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                    }
                
                canal1 = await guild.create_text_channel(name = f'❓・{title}', overwrites = overwrites)
                await asyncio.sleep(0.5)
                canal = self.bot.get_channel(int(canal1.id))

                await user.send('Ok, agora preciso de uma pequena descrição para poder informar o pessoal que irá te atender. Poderia me falar um pouco sobre? ')
                desc_suporte = await self.bot.wait_for('message', check=Eventos.check(self, user), timeout=3600)
                desc = desc_suporte.content

                em = discord.Embed(title = f'Canal de suporte para {str(user.name).upper()}:', description = f'A denuncia de {user.name} é:\n{desc}\n\nReaja com ❌ para fechar e deletar este canal', color=0xFECD00)
                em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')

                await canal.send(f'@here')
                embed = await canal.send(embed=em)
                await embed.add_reaction('❌')

            if emoji == '🔴' and user.id in [693639831443734538, 401549060487774208]:
                global bug
                await canal_bug.send('<@718476589284851754>')
                bug = await canal_bug.send(embed=embed_bug)
                for i in ['🟡', '🟠', '🔴']:
                    await bug.add_reaction(i)

            if emoji == '🟡' and channel.id == 838590913911062528:
                await bug.edit(embed = embed_bug1)
                await bug.clear_reactions()
                await bug.add_reaction('✅')
            if emoji == '🟠' and channel.id == 838590913911062528:
                await bug.edit(embed = embed_bug2)
                await bug.clear_reactions()
                await bug.add_reaction('✅')
            if emoji == '🔴' and channel.id == 838590913911062528:
                await bug.edit(embed = embed_bug3)
                await bug.clear_reactions()
                await bug.add_reaction('✅')

            if emoji == '✅' and user.id in [693639831443734538, 401549060487774208, 718476589284851754] and channel.id == 838590913911062528:
                corrigido = self.bot.get_channel(838584441836142683)
                await corrigido.send('✅ ' + msg_bug)
                await bug.clear_reactions()
                await bug.edit(embed=discord.Embed(title='BUG CORRIGIDO', description='**bug enviado para o canal <#838584441836142683>!**', color=0x78B159))

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await message.guild.fetch_member(payload.user_id)
        mem = self.bot.get_user(user.id)
        emoji = str(payload.emoji)

        if channel.id == 734069866037903440:
            if emoji == '🎮':
                carg1 = message.guild.get_role(826548329411379280)
                await user.remove_roles(carg1)
            
            elif emoji == '🖥️':
                carg2 = message.guild.get_role(830136908843188294)
                await user.remove_roles(carg2)
        
            elif emoji == '📂':
                carg3 = message.guild.get_role(830136741285068801)
                await user.remove_roles(carg3)
            elif emoji == '🔴':
                carg5 = message.guild.get_role(830124900253171782)
                await user.remove_roles(carg5)
            elif emoji == '🟠':
                carg6 = message.guild.get_role(828275608458887218)
                await user.remove_roles(carg6)
            elif emoji == '🔵':
                carg7 = message.guild.get_role(828273763396354068)
                await user.remove_roles(carg7)
            elif emoji == '🟣':
                carg8 = message.guild.get_role(828274624001343559)
                await user.remove_roles(carg8)
            elif emoji == '🟢':
                carg9 = message.guild.get_role(828274625179287582)
                await user.remove_roles(carg9)





def setup(bot):
    bot.add_cog(Eventos(bot))