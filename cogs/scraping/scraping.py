import discord
from discord.ext import commands
#from scrapers.benchmark import main as func_benchmark
from scrapers.artigos import main as func_artigos
from scrapers.openbox import main as func_openbox
from scrapers.comparador import main as func_comparador
#from scrapers.gerador_link import main as gerar_link
#from scrapers.game_wizard import main as func_gamewizard
import asyncio
from dotenv import load_dotenv, find_dotenv
import os

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


class Scraping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #===================================================
    #                     WEBSCRAPERS                  =
    #===================================================
    @commands.command()        #artigos (adrenaline e clube (1 de cada a cada 2 dias))
    async def setup1(self, ctx):
        while True:
            artigos = self.bot.get_channel(837660806438191134)
            adrenaline = func_artigos('adrenaline')
            if type(adrenaline) != str:
                stp1 = server.find_one({'_id':1})['setup1']
                if adrenaline[0] not in stp1:
                    embed = discord.Embed(title = adrenaline[0], description = f'{adrenaline[1]}\n\nfonte: {adrenaline[3]}', color=0xFECD00)
                    embed.set_image(url=adrenaline[2])
                    await artigos.send('**Acabou de sair um artigo fresquinho <@828274624001343559>!**')
                    await artigos.send(embed=embed)
                    server.find_one_and_update({'_id':1}, {'$push':{'setup1':adrenaline[0]}})
            else:
                await artigos.send(embed=discord.Embed(title='ERROR', description=adrenaline, color=0xff0000))


            await asyncio.sleep(7200)


            cdh = func_artigos('cdh')
            if type(cdh) != str:
                if cdh[0] not in stp1:
                    embed = discord.Embed(title = cdh[0], description = f'{cdh[1]}\n\nfonte: {cdh[3]}', color=0xFECD00)
                    embed.set_image(url=cdh[2])
                    await artigos.send('**Acabou de sair um artigo fresquinho <&828274624001343559>**')
                    await artigos.send(embed=embed)
                    server.find_one_and_update({'_id':1}, {'$push':{'setup1':cdh[0]}})
            else:
                await artigos.send(embed=discord.Embed(title='ERROR', description=cdh, color=0xff0000))

            await asyncio.sleep(86400)


    @commands.command()        #oficina da net (jogos (2 vezes por dia))
    async def setup2(self, ctx):
        while True:
            artigos = self.bot.get_channel(837660806438191134)
            odn = func_artigos('odn')
            print(odn)
            if type(odn) != str:
                stp2 = server.find_one({'_id':2})['setup2']
                if odn[0] not in stp2:
                    embed = discord.Embed(title = odn[0], description = f'{odn[1]}\n\nfonte: {odn[3]}', color=0xFECD00)
                    if odn[2] != None:
                        embed.set_image(url=odn[2])
                    await artigos.send('**Acabou de sair um artigo fresquinho <@&828273763396354068>**')
                    await artigos.send(embed=embed)
                    server.find_one_and_update({'_id':2}, {'$push':{'setup2':odn[0]}})
                    await asyncio.sleep(43200)
            else:
                await artigos.send(embed=discord.Embed(title='ERROR', description=odn, color=0xff0000))
                await asyncio.sleep(43200)


    @commands.command()        #openbox(1 cada 2 hr)
    async def setup3(self, ctx):
        while True:
            canal = self.bot.get_channel(822821443385425971)
            kabum = func_openbox('kabum')
            try:
                for i in range(0, len(kabum['produtos'])):
                    stp3 = server.find_one({'_id':3})['setup3']
                    if kabum['produtos'][i] not in stp3:
                        embed = discord.Embed(title='OPENBOX KABUM', description = f'**<:kabum:830898774570041364> Itens em Promoção**\n\nProduto: [{kabum["produtos"][i]}]({kabum["links"][i]}) está a venda por **{kabum["precos"][i]}**\n\nInformações retiradas do site oficial da [kabum](https://www.kabum.com.br/cgi-local/site/listagem/openbox.cgi)', color=0xFF4F00)
                        embed.set_thumbnail(url=kabum['imgs'][i])
                        await canal.send(embed=embed)
                        server.find_one_and_update({'_id':3}, {'$push':{'setup3':kabum['produtos'][i]}})
                        await asyncio.sleep(7200)
            except:
                await canal.send('Ocorreu um problema durante a extração de conteúdo da pagina `Open Box Kabum`.\nEntre em contato com jv#2121 para reportar o problema')
                await asyncio.sleep(7200)
            

    @commands.command()        #deal daily(1 cada 2 hr)
    async def setup4(self, ctx):
        while True:
            canal = self.bot.get_channel(822821443385425971)
            await asyncio.sleep(3600)
            pichau = func_openbox('pichau')
            try:
                for i in range(0, len(pichau['produtos'])):
                    stp3 = server.find_one({'_id':3})['setup3']
                    if pichau['produtos'][i] not in stp3:
                        embed = discord.Embed(title='OPENBOX PICHAU', description = f'**<:pichau:830898774570041364> Itens em Promoção**\n\nProduto: [{pichau["produtos"][i]}]({pichau["links"][i]}) está a venda por **{pichau["precos"][i]}**\n\nInformações retiradas do site oficial da [pichau](https://www.pichau.com.br/cgi-local/site/listagem/openbox.cgi)', color=0xFF4F00)
                        embed.set_thumbnail(url=pichau['imgs'][i])
                        await canal.send(embed=embed)
                        server.find_one_and_update({'_id':3}, {'$push':{'setup3':pichau['produtos'][i]}})
                        await asyncio.sleep(3600)
            except:
                await canal.send('Ocorreu um problema durante a extração de conteúdo da pagina `Open Box Pichau`.\nEntre em contato com jv#2121 para reportar o problema')
                await asyncio.sleep(7200)

    @commands.command()        #promoçoes
    async def setup5(self, ctx):
        while True:
            canal = self.bot.get_channel(822548832788807691)
            links = 'http://pcbuildwizard.com.br/products/storage-devices/recommend http://pcbuildwizard.com.br/products/cpus/recommend http://pcbuildwizard.com.br/products/cpu-coolers/recommend http://pcbuildwizard.com.br/products/motherboards/recommend http://pcbuildwizard.com.br/products/memories/recommend http://pcbuildwizard.com.br/products/fans/recommend http://pcbuildwizard.com.br/products/power-supplies/recommend http://pcbuildwizard.com.br/products/cases/recommend http://pcbuildwizard.com.br/products/kits/recommend'.split()
            prods = {'nomes':[], 'precos':[], 'links':[], 'notas':[], 'lojas':[], 'menorpreco90':[]}
            ja_foi = []
            for i in links:
                site = req.get(i).json()
                for i in site:
                    prods['nomes'].append(i['description'])
                    prods['lojas'].append(i['storeName'])
                    prods['precos'].append(i['price'])
                    prods['menorpreco90'].append(i['bestPriceOverThePast90Days'])
                    prods['links'].append(i['url'])
                    prods['notas'].append(i['rating'])
            for i in range(0, len(prods['nomes'])):
                stp5 = server.find_one({'_id':5})['setup5']
                if prods["nomes"][i] not in stp5:
                    em = discord.Embed(title='PROMOÇÃO DO DIA', description = f'Produto: [{prods["nomes"][i]}]({prods["links"][i]}) **\nR${str(prods["precos"][i]).replace(".", ",")}.** {prods["notas"][i]} **estrelas**\nMenor preço nos ultimos 90 dias: {str(prods["menorpreco90"][i]).replace(".",",")}\n\nProduto disponível na loja: {prods["lojas"][i]}', color=0xFECD00)
                    em.set_footer(text='Não nos responsabilizamos caso o preço no site esteja diferente, afinal, ele pode mudar a qualquer hora')
                    message = await canal.send(embed=em)
                    await message.add_reaction('<a:verde:828431637763063829>')
                    await message.add_reaction('<a:amarelo:828431636718419978>')
                    await message.add_reaction('<a:vermelho:828431638135832616>')
                    server.find_one_and_update({'_id':5}, {'$push':{'setup5':prods["nomes"][i]}})
                    await asyncio.sleep(60*15)
                    




def setup(bot):
    bot.add_cog(Scraping(bot))