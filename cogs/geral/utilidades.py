import discord
from discord.ext import commands
#from main import verify_channel
from random import choice, randint
from scrapers.comparador import main as func_comparador
import re
import asyncio
import requests as req
import time

time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}

class Utilidades(commands.Cog):
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
    #               BENCHMARK E PESQUISA               =
    #===================================================
    @commands.command()
    async def benchmark(self, ctx, *, arg):
        '''
        if 'vs' in arg.lower():
            msg = await ctx.channel.send(f'coletando dados de benchmark para as peças: {arg}...')
            await asyncio.sleep(1)
            await msg.edit(content='Formatando dados para o envio: (cerca de 8 segundos)')
            pecas = arg.split(' vs ')
            benchs = func_benchmark(pecas[0], pecas[1])
            peca1 = benchs[0]
            peca2 = benchs[1]
            embed = discord.Embed(title = f'BENCHMARK {str(pecas[0]).upper()} VS {str(pecas[1]).upper()}', description='Comparativo feito pelo site UserBenchmark', color=0xFECD00)
            embed.add_field(name=pecas[0], value = f'Pontuação (Gaming): {peca1[0]}\nPontuação (Desktop): {peca1[7]}\nPreço (USD): {peca1[1]}\nLançamento: {peca1[2].replace("Months", "Meses")}\nCores: {peca1[3]}\nThreads: {peca1[4]}\nClocks: {peca1[5]}\nBoost Clock: {peca1[6]}\nResumo Traduzido: próxima versão')
            embed.add_field(name=pecas[1], value = f'Pontuação (Gaming): {peca2[0]}\nPontuação (Desktop): {peca2[7]}\nPreço (USD): {peca2[1]}\nLançamento: {peca2[2].replace("Months", "Meses")}\nCores: {peca2[3]}\nThreads: {peca2[4]}\nClocks: {peca2[5]}\nBoost Clock: {peca2[6]}\nResumo Traduzido: próxima versão')
            
            #resumo1 = gerar_link(translator.translate(peca1[8]))

            #embed.add_field(name=pecas[0], value = f'Resumo final (traduzido): {resumo1}')
            #embed.add_field(name=pecas[1], value = f'Resumo final (traduzido): {translator.translate(peca2[8])}')
            
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/824275240623669251/829702955128455258/cpu.png?width=668&height=669')
            await ctx.send(embed=embed)
            await msg.delete()
        else:
            await ctx.channel.send(f'coletando dados de benchmark para a peça: {arg}...')
        '''
        await ctx.send('**Este comando ainda não está disponível!**')


    @commands.command(aliases=['comparar', 'pesquise', 'comparacao'])
    async def pesquisar(self, ctx, *, item):
        if not await Utilidades.verify_channel(self, ctx.channel.id, [], ''): return
        msg = await ctx.send('**Coletando dados...**', delete_after=8)
        await asyncio.sleep(1)
        await msg.edit(content="**Organizando Preços...**")
        await asyncio.sleep(1)
        await msg.edit(content="**Aguarde...**")

        produto = func_comparador(item)
        enifler = produto['enifler']
        if type(enifler) != str:
            em = discord.Embed(title='COMPARATIVO DE PRODUTOS: (ENIFLER)', description = f'Produto: [{enifler[0]}]({enifler[3]}) está a venda por **{enifler[1]}**\n\nInformações retiradas do site oficial da [Enifler](https://www.enifler.com.br/)', color=0xFECD00)
            em.set_thumbnail(url=enifler[2])
        else:
            em=discord.Embed(title='ERROR (ENIFLER)', description=enifler, color=0xff0000)
        await ctx.send(embed=em)

        kabum = produto['kabum']
        if type(kabum) != str:
            em = discord.Embed(title='COMPARATIVO DE PRODUTOS: (KABUM)', description = f'Temporariamente Indisponível', color=0xFF4F00)#Produto: [{kabum[0]}]({kabum[3]}) está a venda por **{kabum[1]}**\n\nInformações retiradas do site oficial da [kabum](https://www.kabum.com.br/)', color=0xFF4F00)
            em.set_thumbnail(url='https://media.discordapp.net/attachments/816164215932715028/830601509187878952/error-image-generic.png')
        else:
            em=discord.Embed(title='ERROR (KABUM)', description=kabum, color=0xff0000)
        await ctx.send(embed=em)


        pichau = produto['pichau']
        if type(pichau) != str:
            em = discord.Embed(title='COMPARATIVO DE PRODUTOS: (PICHAU)', description = f'Produto: [{pichau[0]}]({pichau[3]}) está a venda por **{pichau[1]}**\n\nInformações retiradas do site oficial da [pichau](https://www.pichau.com.br/)', color=0xC92027)
            em.set_thumbnail(url=pichau[2])
        else:
            em=discord.Embed(title='ERROR (PICHAU)', description=pichau, color=0xff0000)
        await ctx.send(embed=em)


        terabyte = produto['terabyte']
        if type(terabyte) != str:
            em = discord.Embed(title='COMPARATIVO DE PRODUTOS: (TERABYTE)', description = f'Produto: [{terabyte[0]}]({terabyte[3]}) está a venda por **{terabyte[1]}**\n\nInformações retiradas do site oficial da [terabyte](https://www.terabyte.com.br/)', color=0xFF5510)
            if terabyte[2] != None:
                em.set_thumbnail(url=terabyte[2])
            else:
                em.set_thumbnail(url='https://media.discordapp.net/attachments/828454132973043714/828989752547475516/noimage.png')
        else:
            em=discord.Embed(title='ERROR (TERABYTE)', description=terabyte, color=0xff0000)
        await ctx.send(embed=em)
        await ctx.send(content = f"**Aqui estão os resultados para {item}**")

    #===================================================
    #                     COTAÇÕES                     =
    #===================================================
    @commands.command(pass_context=True)
    async def dolar(self, ctx):
        if not await Utilidades.verify_channel(self, ctx.channel.id, [], ''): return
        requisicao = req.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        cotacao = requisicao.json()
        agora = time.strftime('%H:%M • %d-%m-%Y', time.localtime())
        embed = discord.Embed(title=f'{agora}', description='**1 Dólar americano é igual a:** \n{} **Reais brasileiro**'.format(cotacao['USD']['bid'] ))
        embed.set_thumbnail(url='https://cdn.jornaldebrasilia.com.br/wp-content/uploads/2019/05/dolar1.jpg')
        await ctx.channel.send(embed=embed)



    @commands.command(pass_context=True)
    async def euro(self, ctx):
        if not await Utilidades.verify_channel(self, ctx.channel.id, [], ''): return
        requisicao = req.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
        cotacao = requisicao.json()
        agora = time.strftime('%H:%M • %d-%m-%Y', time.localtime())
        embed = discord.Embed(title=f'{agora}', description = f'**1 Euro é igual a:** \n{cotacao["EUR"]["bid"] } **Reais brasileiro**')
        embed.set_thumbnail(url='https://cdn.jornaldebrasilia.com.br/wp-content/uploads/2019/05/dolar1.jpg')
        await ctx.channel.send(embed=embed)

    @commands.command(pass_context=True, aliases=['bitcoin'])
    async def btc(self, ctx):
        if not await Utilidades.verify_channel(self, ctx.channel.id, [], ''): return
        requisicao = req.get('https://economia.awesomeapi.com.br/all/BTC-BRL')
        cotacao = requisicao.json()
        agora = time.strftime('%H:%M • %d-%m-%Y', time.localtime())
        embed = discord.Embed(title=f'{agora}', description = f'**1 Bitcoin é igual a:** \n{cotacao["BTC"]["bid"] } **Reais brasileiro**')
        embed.set_thumbnail(url='https://cdn.jornaldebrasilia.com.br/wp-content/uploads/2019/05/dolar1.jpg')
        await ctx.channel.send(embed=embed)


    #===================================================
    #                      GIVEAWAY                    =
    #===================================================

    def convert(self, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for key, value in matches:
            try:
                time += time_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(
                    f"{value} is an invalid time key! h|m|s|d are valid arguments"
                )
            except ValueError:
                raise commands.BadArgument(f"{key} is not a number!")
        return round(time)

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
        
    @commands.command(pass_context=True, aliases=['sorteio', 'sortear'])
    async def giveaway(self, ctx, timingg = None, winnerss: int = None, *, prizee = None):
        global prize, timing, winners
        prize = prizee
        timing = timingg
        winners = winnerss
        if timing == None:
            await ctx.channel.send(embed = discord.Embed(description = f'Você precisa informar qual será a duração do giveaway. Ex: f!giveaway 1h(ou 1m ou 1s ou 1d) 1 titulo do giveaway', color = 0xff0000))
        elif winners == None:
            await ctx.channel.send(embed = discord.Embed(description = f'Você precisa informar quantas pessoas poderão ganhar o giveaway. Ex: f!giveaway 1h 1 titulo do giveaway', color = 0xff0000))
        elif prize == None:
            await ctx.channel.send(embed = discord.Embed(description = f'Você precisa informar qual será o título do giveaway. Ex: f!giveaway 1h 1 titulo do giveaway', color = 0xff0000))
        else:
            gwembed = discord.Embed(
                title="🎉 __**Giveaway**__ 🎉",
                description=f'**Presente: {prize}**',
                color=0xb4e0fc
            )
            time = Utilidades.convert(self, timing)
            time_formatado = Utilidades.formatar_tempo(self, time)
            gwembed.set_footer(text=f"O giveaway acabará em {time_formatado}")
            gwembed = await ctx.send(embed=gwembed)
            await gwembed.add_reaction("🎉")
            await asyncio.sleep(time)
            message = await ctx.fetch_message(gwembed.id)
            users = await message.reactions[0].users().flatten()
            users.pop(users.index(ctx.guild.me))
            if len(users) == 0:
                await ctx.send("Não teve nenhum vencedor.")
                return
            for i in range(winners):
                winner = choice(users)
                await ctx.send(f'**Parabéns {winner} por ganhar o sorteio "{prize}"!**')

    @commands.command()
    async def reroll(self, ctx, id):
        message = await ctx.fetch_message(id)
        users = await message.reactions[0].users().flatten()
        users.pop(users.index(ctx.guild.me))
        for i in range(winners):
            winner = choice(users)
            await ctx.send(f'**Parabéns {winner} por ganhar o sorteio "{prize}"!**')



def setup(bot):
    bot.add_cog(Utilidades(bot))