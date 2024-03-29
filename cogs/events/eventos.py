import discord
from discord.ext import commands
import requests as req
import os
import asyncio
from random import randint
import re
from discord.ext import tasks
from utils.mongoconnect import mongoConnect

cluster = mongoConnect()
db = cluster['discord']
conta = db['conta']

premio = []

class Eventos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def criar_conta(self, mem_id):
        if mem_id != 851618408965079070:
            try:    
                conta.insert_one({"_id":mem_id, "saldo":0, "stars":[], "wallet":{}, "warnings":[], 'xp':0, "level":0, "descricao":"Use .descricao para alterar a sua descrição"})
            except:
                pass


    @commands.Cog.listener()
    async def on_message(self, message):
        id = message.author.id
        await self.criar_conta(id)

        if not message.author.bot:
            if not id in premio:
                premio.append(id)
            lvl = 0
            stats = conta.find_one({'_id':id})
            xp = stats['xp']
            while True:
                if xp < ((50*(lvl**2))+(50*lvl)):
                    break
                lvl += 1
            xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
            if xp in range(0,25) and lvl > 1:
                next_level = int(200*((1/2)*lvl))
                nivel = int((next_level / 100)-1)
                up = False
                for i in levelnum:
                    if nivel == i:
                        id_cargo = levelnum[i]
                        bonus = 50*i
                        conta.update_one({'_id':id}, {'$inc':{'saldo':bonus}})
                        cmds = self.bot.get_channel(760531609261834250)
                        await cmds.send(f'⭐ | Parabéns {message.author.mention}, você upou para o **Level {nivel}**!',embed=embed)
                        up = True
                        conta.update_one({'_id':id}, {'$inc':{'xp':26}})
                if up == False:
                    cmds = self.bot.get_channel(jsl.get_channel('comandos'))
                    await cmds.send(f'⭐ | Parabéns {message.author.mention}, você passou para o **Level {nivel}**!')
                    conta.update_one({'_id':id}, {'$inc':{'xp':26}})
        
        if message.author.id == 302050872383242240:
            try:
                for i in message.embeds:
                    print(i.description)
                    if ':thumbsup:' in i.description:
                        id = re.sub('[^0-9]', '', i.description[0:30])
                        if id != '':
                            await message.channel.send(f'<@{str(id)}>')
                            await message.channel.send(embed = discord.Embed(title='Recompensa pelo bump', description = f'**Parabéns <@{str(id)}>, você ganhou 40 reais por ter dado Bump no server.**\nVolte daqui 2 horas para poder bumpar novamente', color=0x1CFEFE))
                            conta.find_one_and_update({'_id':int(id)}, {'$inc':{'saldo':40}})
                        else:
                            await message.channel.send('Houve um problema com o bot do bump, portanto, não podemos recompensar o autor do comando')
                            staff = self.bot.get_channel(853715980516982804)
                            await staff.send('Houve um problema com o bot do bump, portanto, não podemos recompensar o autor do comando')
            except:
                if ':thumbsup:' in message.content:
                    id = re.sub('[^0-9]', '', i.description[0:30])
                    if id != '':
                        await message.channel.send(f'<@{str(id)}>')
                        await message.channel.send(embed = discord.Embed(title='Recompensa pelo bump', description = f'**Parabéns <@{str(id)}>, você ganhou 40 reais por ter dado Bump no server.**\nVolte daqui 2 horas para poder bumpar novamente', color=0x1CFEFE))
                        conta.find_one_and_update({'_id':int(id)}, {'$inc':{'saldo':40}})
                    else:
                        await message.channel.send('Houve um problema com o bot do bump, portanto, não podemos recompensar o autor do comando')
                        staff = self.bot.get_channel(853715980516982804)
                        await staff.send('Houve um problema com o bot do bump, portanto, não podemos recompensar o autor do comando')


    @tasks.loop(minutes=1)
    async def add_xp():
        premio_temp = tuple(premio)
        print ('premio1:',premio)
        print ('temp1:',premio_temp)
        if len(premio) >= 1:
            r_xp = randint(15, 25)
            premio.clear()
            conta.update_many({'_id':{'$in':premio_temp}}, {'$inc': {'xp': r_xp}})
            print ('premio2:',premio)
            print ('temp2:',premio_temp)
    add_xp.start()

def setup(bot):
    bot.add_cog(Eventos(bot))