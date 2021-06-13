import discord
from discord.ext import commands
#from main import verify_channel
#from main import criar_conta
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap
from io import BytesIO
import requests as req
from random import randint
import asyncio
import os
from dotenv import load_dotenv, find_dotenv
from discord.ext.commands.core import cooldown

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


class Economiaperfil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def formatar_tempo(self, seconds):
        total_segs = int(seconds)
        horas = total_segs // 3600
        dias = horas//86400
        segs_restantes = total_segs % 3600
        minutos = segs_restantes // 60
        segs_restantes_final = segs_restantes % 60
        if (horas >= 24): 
            dias = int(horas / 24)
            horas = int(horas % 24)
        
        if dias != 0:
            return f'{dias} dia(s)'
        elif horas != 0:
            return f'{horas} hora(s)'
        elif minutos != 0:
            return f'{minutos} minuto(s)'
        elif segs_restantes_final != 0:
            return f'{segs_restantes_final} segundo(s)'

    async def verify_channel(self, id, channels : None, msg: None):
        if id == 733851707800289340:
            await self.bot.get_channel(id).send('**Não é permitido o uso de comandos no chat <#733851707800289340>**')
            return False
        if id not in channels and len(channels) > 0:
            await self.bot.get_channel(id).send(msg)
            return False
        return True

    #===================================================
    #                     XP E PERFIL                  =
    #===================================================
    @commands.command(pass_context=True, aliases=['conta', 'atm', 'bal', 'balance', 'wallet', 'carteira'])
    async def saldo(self, ctx, member : discord.Member = None):
        if not await Economiaperfil.verify_channel(self, ctx.channel.id, [842371888750657546, 830941514830053436, 827693206900310066, 828119245707411527, 827681511234863124], 'Você deve usar este comando no canal <#827681511234863124>'):
            return
        criar_conta(ctx.author.id)
        if member == None:
            id = ctx.author.id
            await ctx.channel.send(embed = discord.Embed(title = f'SALDO DE {ctx.author.name.upper()}:', description = f'<:FlerPoints:829803555123626035> {banco.find_one({"_id":id})["flerpoints"]} FlerPoints\n<:FlerCoin:829803555325739079> {banco.find_one({"_id":id})["flercoins"]} FlerCoins', color=0xFECD00))
        else:
            criar_conta(member.id)
            id = member.id
            await ctx.channel.send(embed = discord.Embed(title = f'SALDO DE {member.name.upper()}:', description = f'<:FlerPoints:829803555123626035> {banco.find_one({"_id":id})["flerpoints"]} FlerPoints\n<:FlerCoin:829803555325739079> {banco.find_one({"_id":id})["flercoins"]} FlerCoins', color=0xFECD00))


    @commands.command(pass_context=True, aliases=['pagar', 'transf'])
    async def transferir(self, ctx, member : discord.Member = None, quant : int = None):
        if not await Economiaperfil.verify_channel(self, ctx.channel.id, [842371888750657546, 827681511234863124, 830941514830053436], 'Você deve usar este comando no canal <#827681511234863124>'): return
        if member == None or quant == None:
            id = ctx.author.id
            criar_conta(id)
            await ctx.channel.send(embed = discord.Embed(description = f'Você precisa informar para quem quer transferir e a quantidade de dinherio. Ex: f!transferir @jv 1000', color=0xFECD00))
        else:
            if not '-' in str(quant) and quant != 0:
                if member.id != ctx.author.id:
                    id = ctx.author.id
                    other_id = member.id
                    criar_conta(other_id)
                    if banco.find_one({'_id':id})['flerpoints'] >= quant:
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':-quant}})
                        banco.find_one_and_update({'_id':other_id}, {'$inc':{'flerpoints':quant}})
                        transacoes = self.bot.get_channel(828483579880538122)
                        await ctx.channel.send(embed = discord.Embed(title = f'{ctx.author.name.upper()} FEZ UMA TRANSFERENCIA PARA {member.name.upper()}:', description = f'{ctx.author.mention} transferiu <:FlerPoints:829803555123626035> {quant} flerpoints para {member.mention}', color=0xFECD00))
                        await transacoes.send(embed = discord.Embed(title = f'{ctx.author.name.upper()} FEZ UMA TRANSFERENCIA PARA {member.name.upper()}:', description = f'{ctx.author.mention} transferiu <:FlerPoints:829803555123626035> {quant} flerpoints para {member.mention}', color=0xFECD00))
                    else:
                        await ctx.channel.send(embed = discord.Embed(description = f'Você não tem flerpoints suficiente para concluir está transação', color=0xFECD00))
                else:
                    await ctx.channel.send('**Porquê você quer transferir um valor para você mesmo?\nInforme um membro válido da próxima vez!**')

            else:
                await ctx.channel.send('**Como você vai trasnferir um valor negativo ou nulo?\nInforme um valor correto da próxima vez!**')



    @commands.command(pass_context=True, aliases=['profile'])
    async def perfil(self, ctx, member : discord.Member = None):
        id = ctx.message.author.id
        criar_conta(id)
        if not await Economiaperfil.verify_channel(self, ctx.channel.id, [], ''): return

        if member == None:
            user_avatar = req.get(ctx.author.avatar_url)
        else:
            id = member.id
            criar_conta(id)
            user_avatar = req.get(member.avatar_url)

        url = user_avatar
        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((136, 136))

        background = Image.open('img/perfil.png')

        if member == None:
            user_name = ctx.author.name.lower()
            user_flerpoints = str(banco.find_one({'_id':id})['flerpoints'])
            user_descricao = str(conta.find_one({'_id':id})['descricao'])
            user_avatar = req.get(ctx.author.avatar_url)
            user_flercoins = str(banco.find_one({'_id':id})['flercoins'])
            user_xp = str(conta.find_one({'_id':id})['xp'])
            if ctx.author.id == 401549060487774208:
                coroa = Image.open('img/coroa.jpg')
                coroa = coroa.resize((25,25))
                background.paste(coroa, (265, 9))
            elif ctx.author.id == 693639831443734538:
                coroa = Image.open('img/dev.jpg')
                coroa = coroa.resize((35,30))
                background.paste(coroa, (255, 6))
        else:
            id = member.id
            criar_conta(id)
            user_name = str(member.name).lower()
            user_flerpoints = str(banco.find_one({'_id':id})['flerpoints'])
            user_descricao = str(conta.find_one({'_id':id})['descricao'])
            user_avatar = req.get(member.avatar_url)
            user_flercoins = str(banco.find_one({'_id':id})['flercoins'])
            user_xp = str(conta.find_one({'_id':id})['xp'])
            if id == 401549060487774208:
                coroa = Image.open('img/coroa.jpg')
                coroa = coroa.resize((25,25))
                background.paste(coroa, (265, 9))
            elif id == 693639831443734538:
                coroa = Image.open('img/dev.jpg')
                coroa = coroa.resize((35,30))
                background.paste(coroa, (255, 6))

        fonte_maior = ImageFont.truetype('fonts/LEMONMILK-Regular.otf', 25)
        fonte = ImageFont.truetype('fonts/LEMONMILK-Regular.otf', 18)
        fonte_menor = ImageFont.truetype('fonts/LEMONMILK-Regular.otf', 15)

        draw = ImageDraw.Draw(background)
        background.paste(avatar, (0, 0))

        if len(user_name) > 18:
            arg = list(user_name)
            lista = arg[0:18]
            arg = ''
            for i in lista:
                arg += i
            arg += '...'
            user_name = arg

        draw.text((200, 5), user_name.lower(), font=fonte, fill='white')
        draw.text((200, 50), 'FlerPoints: '+user_flerpoints, font=fonte, fill='white')
        draw.text((420, 5), 'FlerCoins: ' + user_flercoins, font=fonte, fill='white')
        draw.text((420, 50), 'Xp: ' + user_xp, font=fonte, fill='white')
        draw.text((5,392), 'Descrição: ', font=fonte_menor, fill='white')
        draw.text((5,435), user_descricao, font=fonte_menor, fill='white')
        background.save('temp/perfil-user.png', format='PNG')
        ft = discord.File(open('temp/perfil-user.png', 'rb'))
        await ctx.channel.send(ctx.author.mention, file=ft)


    @commands.command(pass_context=True, aliases=['desc', 'description'])
    async def descricao(self, ctx, *, arg = None):
        if not await Economiaperfil.verify_channel(self, ctx.channel.id, [], ''): return
        id = ctx.author.id
        criar_conta(id)
        if arg == None:
            await ctx.channel.send(embed = discord.Embed(description = f'Você precisa informar qual será a sua nova descrição. Ex: f!descricao minha nova descrição é essa!', color = 0xff0000))
        else:
            if len(arg) >= 65:
                arg = list(arg)
                lista = arg[0:57]
                arg = ''
                for i in lista:
                    arg += i
                arg += '...'
            conta.find_one_and_update({'_id':id}, {'$set':{'descricao':arg}})
            await ctx.channel.send(embed = discord.Embed(title='SUA DESCRIÇÃO FOI ALTERADA', description = f'{ctx.author.name}, sua descrição foi alterada para: "{arg}"', color = 0xffffff))
            

    @commands.command(pass_context=True, aliases=['exp', 'experience', 'level'])
    async def xp(self, ctx, member : discord.Member = None):
        if not await Economiaperfil.verify_channel(self, ctx.channel.id, [], ''): return
        id = ctx.author.id
        criar_conta(id)

        if member == None:
            embed = discord.Embed(title = f'XP DE {ctx.author.name.upper()}:', description = f'<:xp:829803555283664956> {ctx.author.name}, você tem {conta.find_one({"_id":id})["xp"]} de xp!', color=0x912488)
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/816402333117972480/829802755337486336/ExperiencePoints.png?width=672&height=672')
            await ctx.channel.send(embed = embed)
        else:
            id = member.id
            criar_conta(id)
            embed = discord.Embed(title = f'XP DE {member.name.upper()}:', description = f'{member.name}, você tem {conta.find_one({"_id":id})["xp"]} de xp!', color=0x912488)
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/816402333117972480/829802755337486336/ExperiencePoints.png?width=672&height=672')
            await ctx.channel.send(embed = embed)


    @commands.command(pass_context=True, aliases=['ranking', 'ranque', 'topflerpoints', 'flerpointsrank', 'rankflerpoints'])
    async def rank(self, ctx, mem : discord.Member = None):
        if not await Economiaperfil.verify_channel(self, ctx.channel.id, [], ''): return
        if mem == None:
            id = ctx.author.id
            criar_conta(id)
            user_name = ctx.author.name
            user_discrim = '#' + str(ctx.author.discriminator)
            url = req.get(ctx.author.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            avatar = avatar.resize((159, 159))
        else:
            id = mem.id
            criar_conta(id)
            user_name = mem.name
            user_discrim = '#' + mem.discriminator
            url = req.get(mem.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            avatar = avatar.resize((159, 159))
        xps = {}
        for i in conta.find({}):
            xps[i['_id']] = i['xp']
        rankss = {k: v for k, v in sorted(xps.items(), key=lambda item: item[1])}
        ranks = dict(reversed(list(rankss.items())))
        tamanho_fonte_nome = 40
        if len(user_name) >= 13 and len(user_name) < 16:
            tamanho_fonte_nome = 33
        elif len(user_name) >= 16 and len(user_name) < 21:
            tamanho_fonte_nome = 28


        user_rank = str(int(list(ranks).index(id)) + 1)
        user_level = str(conta.find_one({'_id':id})['level'])

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

        background = Image.open('./img/background.jpg')
        barra = Image.open('./img/barra.png')
        layout = Image.open('./img/layout.png')

        user_xp = conta.find_one({'_id':id})['xp']
        max = (conta.find_one({'_id':id})['level'] + 1 ) * 1000
        pos = (user_xp * 632) / max

        background.paste(barra, (-632 + int(pos), 0), barra)
        background.paste(avatar, (79,62), avatar)   
        background.paste(layout, (0,0), layout)

        draw = ImageDraw.Draw(background)

        font_nome = ImageFont.truetype('./fonts/LEMONMILK-Regular.otf', tamanho_fonte_nome)
        font = ImageFont.truetype('./fonts/LEMONMILK-Regular.otf', 40)
        font_s = ImageFont.truetype('./fonts/LEMONMILK-Regular.otf', 30)

        w, h = draw.textsize(user_name, font=font_nome)
        draw.text((265,80), user_name, font=font_nome, fill='#fff')
        draw.text((275 + w, 80), user_discrim, font=font_nome, fill='#bbb')

        w, h = draw.textsize(user_rank, font=font_s)
        draw.text((863 - w,25), user_rank, font=font_s, fill='#000')

        if len(str(user_level)) == 3:
            draw.text((860,218), '99+', font=font_s, fill='#000')
        else:
            w, h = draw.textsize(user_level, font=font_s)
            draw.text((892 - w,217), user_level, font=font_s, fill='#000')

        w, h = draw.textsize(f'{user_xp}/{str(max)}', font=font_s)
        draw.text((883 - w,100), f'{user_xp}/{str(max)}', font=font_s, fill='#fff')

        background.save('temp/temp_rank.png', format='PNG')
        ft = discord.File(open('temp/temp_rank.png', 'rb'))
        await ctx.send(ctx.author.mention, file=ft)



    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.command( pass_context=True, aliases=['daily'])
    async def diario(self, ctx):
        if not await Economiaperfil.verify_channel(self, ctx.channel.id, [842371888750657546, 842371888750657546, 827681511234863124, 830941514830053436], 'Você deve usar este comando no canal <#827681511234863124>'): return

        id = ctx.message.author.id
        criar_conta(id)
        
        nsort = randint(5, 50)
        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':nsort}})


        em = discord.Embed(title = f'Você recebeu {nsort} flerpoints no seu bonus diario.', description="Volte amanhã para poder pega-lo novamente.", color=0xE63E43)
        em.set_thumbnail(url='https://images.vexels.com/media/users/3/146457/isolated/preview/2bba99c4323c66745b5584ef7a1163a2-open-red-wrap-gift-box-by-vexels.png')
        await ctx.channel.send(embed = em)    
    @diario.error
    async def diario_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Esse comando está em cooldown. Você poderá **usar novamente em {}**'.format(Economiaperfil.formatar_tempo(self, error.retry_after))
            await ctx.send(msg)
        else:
            raise error



    @commands.command()
    async def roleta(self, ctx, arg:int):
        if not await Economiaperfil.verify_channel(self, ctx.channel.id, [842371888750657546, 827693206900310066, 830941514830053436], 'Você deve usar este comando no canal <#827693206900310066>'): return

        id = ctx.message.author.id
        criar_conta(id)
        if not '-' in str(arg) and arg != 0:
            if arg >= 1 and arg <=60:
                if banco.find_one({'_id':id})['flerpoints'] >= 100:
                    banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':-100}})
                    em = discord.Embed(title = f'Roleta da sorte', description="Você gastou 100 FlerPoints nesta aposta.\nGirando a roleta...", color=0xE63E43)
                    em.set_image(url='https://i.pinimg.com/originals/8f/5c/73/8f5c73ea3f81efb84f9043608cfb3467.gif')
                    roleta = await ctx.channel.send(embed = em)
                    await asyncio.sleep(3)
                    num_roleta = randint(1,60)
                    if arg == num_roleta:
                        banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':1000}})
                        await roleta.edit(embed = discord.Embed(title = f'A roleta parou no número {num_roleta}', description = f'{ctx.author.mention} você ganhou 1000 flerpoints na roleta!!', color=0xE63E43))
                    else:
                        await roleta.edit(embed = discord.Embed(title = f'A roleta parou no número {num_roleta}', description = f'{ctx.author.mention} não foi dessa vez...\nTente novamente, boa sorte!', color=0xE63E43))
                else:
                    await ctx.channel.send(embed = discord.Embed(title='Dinheiro insuficiente!', description = f'{ctx.author.mention} você não tem dinheiro suficiente para a aposta. O valor **mínimo é de 100 flerpoints**', color=0xFF0000))
            else:
                await ctx.channel.send(embed = discord.Embed(description = f'{ctx.author.mention} você deve escolher um número **entre 1 e 60**', color=0xE63E43))
        else:
            await ctx.channel.send('**Como você vai aspostar um valor negativo ou nulo na roleta?\nInforme um valor correto da próxima vez!**')
    @roleta.error
    async def roleta_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = discord.Embed(description='Você deve escolher um número **entre 1 e 60**\nEx: *roleta 7', color=0xE63E43))
        else:
            raise error


    
    @commands.command(pass_context=True, aliases=['aposta', 'bet'])
    async def apostar(self, ctx, member : discord.Member = None, quant : int = None):

        #if not await Economiaperfil.verify_channel(ctx.channel.id, [827693206900310066, 830941514830053436], 'Você deve usar este comando no canal <#827693206900310066>'): return

        if member == None:
            await ctx.channel.send(embed = discord.Embed(description = f'Você precisa informar para quem fará a aposta. Ex: f!apostar @jv 1000', color = 0xff0000))
        elif quant == None:
            await ctx.channel.send(embed = discord.Embed(description = f'Você precisa informar o valor da aposta. Ex: f!apostar @jv 1000', color = 0xff0000))
        else:
            if not '-' in str(quant) or quant == 0:
                if member.id != ctx.author.id:
                    id = ctx.author.id
                    other_id = member.id
                    criar_conta(id)
                    criar_conta(other_id)
                    aposta = await ctx.channel.send(embed=discord.Embed(title='APOSTA', description = f'{ctx.author.mention} quer fazer uma aposta de {quant} flerpoints para {member.mention}.\nAssim que o {member.mention} clicar em "✅", a aposta será inciada.', color=0xFECD00))
                    await aposta.add_reaction('✅')
                    await aposta.add_reaction('🛑')
                    user_id = ctx.author.id
                    member_id = member.id
                    quant_aposta = quant
                else:
                    await ctx.channel.send(embed = discord.Embed(description = '**Por que você quer apostar um valor com você mesmo?\nInforme um membro válido da próxima vez!**', color=0xff0000))
            else:
                await ctx.channel.send(embed = discord.Embed(description = '**Como você vai apostar um valor negativo ou nulo?\nInforme um valor correto da próxima vez!**', color=0xff0000))

        def check(reaction, user):
            return (user == member or user == ctx.author) and str(reaction.emoji) in ['✅', '🛑'] and reaction.message.id == aposta.id
            #verifica a pessoa mencionada, reacções e id da mensangem reagida
        while True:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=3600, check=check)
            emoji = str(reaction.emoji)
            if emoji == "✅" and user == member:
                await aposta.clear_reactions()
                user_saldo = banco.find_one({'_id':user_id})['flerpoints']
                member_saldo = banco.find_one({'_id':member_id})['flerpoints']
                if user_saldo >= quant_aposta:
                    if member_saldo >= quant_aposta:
                        moeda = randint(0, 1)   
                        if moeda == 0:
                            await ctx.channel.send(embed = discord.Embed(description = f'<@{user_id}> ganhou a aposta de {quant_aposta} flerpoints.',color=0xFECD00))
                            banco.find_one_and_update({'_id':user_id}, {'$inc':{'flerpoints':quant_aposta}})
                            banco.find_one_and_update({'_id':member_id}, {'$inc':{'flerpoints':-quant_aposta}})
                        else:
                            await ctx.channel.send(embed = discord.Embed(description = f'<@{member_id}> ganhou a aposta de {quant_aposta} flerpoints.', color=0xFECD00))
                            banco.find_one_and_update({'_id':member_id}, {'$inc':{'flerpoints':quant_aposta}})
                            banco.find_one_and_update({'_id':user_id}, {'$inc':{'flerpoints':-quant_aposta}})
                    else:
                        await ctx.channel.send(embed = discord.Embed(title='Dinheiro insuficiente!', description = f'<@{member_id}> você não tem dinheiro suficiente para a aposta.', color=0xFF0000))
                else:
                    await ctx.channel.send(embed = discord.Embed(title='Dinheiro insuficiente!', description = f'<@{user_id}>, você não tem dinheiro suficiente para a aposta.', color=0xFF0000))
                break
            if emoji == '🛑' and (user == ctx.author or user == member):
                await aposta.clear_reactions()
                await aposta.edit(embed = discord.Embed(title='APOSTA CANCELADA!', description = f'A aposta de {quant_aposta} FlerPoints foi cancelada', color=0xFF0000))
                break




    #===================================================
    #                       LOJA                       =
    #===================================================
    @commands.command(aliases=['shop'])  
    async def loja(self, ctx):
        '''
        if ctx.channel.id != 827602469660000287:
            await ctx.channel.send('Você deve usar este comando no canal <#827602469660000287>', delete_after=5)
            return
        em = discord.Embed(title='LOJA', description='Qual loja você deseja ver? ', color=0xFECD00)
        em.add_field(name='CARGOS', value='Reaja com 💎', inline=True)
        em.add_field(name='CUPONS DECONTO', value='Reaja com 💰', inline=True)
        em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')
        loja_msg = await ctx.channel.send(embed=em)

        reactions = ['💎', '💰']
        for i in reactions:
            await loja_msg.add_reaction(i)
        '''
        await ctx.send('**Loja Disponível em alguns dias! Aguarde...**')



def setup(bot):
    bot.add_cog(Economiaperfil(bot))