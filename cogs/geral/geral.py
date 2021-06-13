import discord
from discord.ext import commands
#from main import verify_channel
from io import BytesIO
import requests as req
from random import choice, randint
import asyncio
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap


class Geral(commands.Cog):
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
    #                      GERAL                       =
    #===================================================

    @commands.command(aliases=['h', 'ajuda', 'comandos', 'commands'])
    async def help(self, ctx):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        pages = 4
        cur_page = 1
        message = await ctx.send(embed=discord.Embed(title = f'HELP 1/4:', description='**Prévia dos comandos:**\n\n**STAFF:**\n🔹  **kick**\n🔹  **ban**\n🔹  **mute**\n🔹  **warn**\n🔹  **clear**\n\n**GERADOR DE MEMES:**\n🔹 **hipocrisia:** cria um meme "enfim a hipocrisia" com o texto informado\n🔹 **stonks:** cria um meme "stonks" com o texto informado\n🔹 **notstonks:** cria um meme "not stonks" com o texto informado\n🔹 **pegadinha:** cria um meme "pegadinhas" com o nome informado\n🔹 **kiko:** cria um meme "kiko amaldiçoado" com o texto informado\n🔹 **medo:** cria um meme "medo" com o texto informado\n🔹 **botoes:** cria um meme "botões" com o texto informado\n\n**AMONG US:**\n🔹 **entrar:** Gera um meme com o usuário mencionado\n🔹 **entrarimpostor:** Gera um meme com o usuário mencionado\n🔹  **entrarcrewmate: Gera um meme com o usuário mencionado**\n🔹 **ejetar:** Gera um meme com o usuário mencionado\n🔹 **ejetarimpostor:** Gera um meme com o usuário mencionado\n🔹 **ejetarcrewmate:** Gera um meme com o usuário mencionado\n\nReaja com os emojis ◀️ e ▶️ para navegar entre os comandos', color = 0xFECD00))
        # getting the message object for editing and reacting
        em = discord.Embed(title = 'HELP 1/4:', description='**Prévia dos comandos:**\n\n**STAFF:**\n🔹  **kick**\n🔹  **ban**\n🔹  **mute**\n🔹  **warn**\n🔹  **clear**\n\n**GERADOR DE MEMES:**\n🔹 **hipocrisia:** cria um meme "enfim a hipocrisia" com o texto informado\n🔹 **stonks:** cria um meme "stonks" com o texto informado\n🔹 **notstonks:** cria um meme "not stonks" com o texto informado\n🔹 **pegadinha:** cria um meme "pegadinhas" com o nome informado\n🔹 **kiko:** cria um meme "kiko amaldiçoado" com o texto informado\n🔹 **medo:** cria um meme "medo" com o texto informado\n🔹 **botoes:** cria um meme "botões" com o texto informado\n\n**AMONG US:**\n🔹 **entrar:** Gera um meme com o usuário mencionado\n🔹 **entrarimpostor:** Gera um meme com o usuário mencionado\n🔹  **entrarcrewmate: Gera um meme com o usuário mencionado**\n🔹 **ejetar:** Gera um meme com o usuário mencionado\n🔹 **ejetarimpostor:** Gera um meme com o usuário mencionado\n🔹 **ejetarcrewmate:** Gera um meme com o usuário mencionado\n\nReaja com os emojis ◀️ e ▶️ para navegar entre os comandos', color = 0xFECD00)
        em2 = discord.Embed(title = 'HELP 2/4:', description='**DIVERSÃO**\n\n🔹  **berti:** meme do berti\n🔹  **adm:** meme do adm\n🔹  **paitaon:** meme do pai ta on\n🔹  **paitaoff:** meme do pai ta off\n🔹  **furro:** meme sobre furry\n🔹  **pato:** meme de pato\n🔹  **kawaii:** meme kawaii\n🔹  **bolsonaro:** meme do bolsonaro\n🔹  **xandao:** meme do xandão\n🔹  **monkiflip:** monkiflip oaooaoaoyeah\n🔹  **salve:** vou te mandar um salve :thumbs_up:\n🔹  **tapa:** vou dar um tapa em quem você quiser\n🔹  **tapa:** vou dar um tapa em quem você quiser\n🔹  **beijar:** vou dar um beijo em quem você quiser\n🔹  **tiro:** vou dar um tiro em quem você quiser\n🔹  **pinto:** vou mostrar o tamanho do pinto de quem você quiser\n🔹  **gado:** vou mostrar o nível de gado de quem você quiser\n\nReaja com os emojis ◀️ e ▶️ para navegar entre os comandos', color = 0xFECD00)
        em3 = discord.Embed(title = 'HELP 3/4:', description = '**UTILIDADES:**\n\n🔹 **benchmark:** Temporariamente indisponível\n🔹 **comparar:** Retorna o comparativo de benchmark entre 2 peças\n🔹 **pesquisar:** Mostra os preços do produto escolhido(Enifler, Kabum, Pichau, Terabyte)\n🔹 **enquete:** Gera uma enquete com a frase do usuário\n🔹 **bump:** Define um despertador para o bump (use antes do bump).\n🔹 **botinfo:** Mostra algumas informações sobre o bot\n🔹 **dolar:** Mostra o valor atual do dolar\n🔹 **euro:** Mostra o valor atual do euro\n🔹 **bitcoin:** Mostra o valor atual do bitcoin\n🔹 **avatar:** Pega a imagem de avatar do usuário mencionado\n🔹 **fale:** O bot irá falar o que você quiser\n🔹 **embed:** O bot irá enviar uma embed para você\n🔹 **mensagem:** O bot irá enviar uma mensagem na dm da pessoa informada.\n🔹  **calcular:** O bot resolverá qualquer problema matemático.\n🔹  **coinflip:** O bot jogará uma moeda (cara ou coroa).\n🔹  **dado:** O bot irá jogar um dado (1 a 6).\n🔹  **piada:** O bot irá contar uma piada\n\nReaja com os emojis ◀️ e ▶️ para navegar entre os comandos', color = 0xFECD00)
        em4 = discord.Embed(title = 'HELP 4/4:', description = '**ECONOMIA E PERFIL:**\n\n🔹  **perfil:** veja seu perfil (imagem).\n🔹 **descricao:** Altera a sua descrição.\n🔹 **saldo:** Mostra seu saldo de FlerPoints e FlerCoins.\n🔹 **xp:** Mostra seu xp.\n🔹 **invites:** Veja/troque seus invites por recompensas\n🔹 **resgatar:** Troque seus FlerPoints por FlerCoins\n🔹  **transferir:** Transfere uma quantia de dinheiro para alguém\n🔹  **apostar:** Faz uma aposta com o usuário mencionado\n🔹  **daily:** Recebe seu bônus diário\n🔹  **loja:** Compre créditos na Enifler e Cargos no server\n🔹  **roleta:** Faz uma aposta na roleta\n\n**BOLSA DE VALORES:**\n🔹  **stocks:** Mostra as empresas dad Bolsa de Valores\n🔹  **acoes:** Mostra os investimentos de um usuário\n🔹  **comprar:** Compre ações da bolsa para obter lucro\n🔹  **vender:** Venda ações da bolsa para obter lucro\n\n**GIVEAWAY:**\n\n🔹  **giveaway:** cria um novo giveaway(sorteio)\n🔹  **reroll:** refaz o ultimo giveaway\n\nReaja com os emojis ◀️ e ▶️ para navegar entre os comandos', color = 0xFECD00)
        
        lista=[em, em2, em3, em4]

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        await message.add_reaction('🚫')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️", '🚫']
            # This makes sure nobody except the command sender can interact with the "menu"

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=180, check=check)
                # waiting for a reaction to be added - times out after x seconds, 60 in this
                # example

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=lista[cur_page - 1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=lista[cur_page - 1])
                    await message.remove_reaction(reaction, user)
                
                elif str(reaction.emoji) == '🚫':
                    await message.delete()

                else:
                    await message.remove_reaction(reaction, user)
                    # removes reactions if the user tries to go forward on the last page or
                    # backwards on the first page
            except asyncio.TimeoutError:
                await message.delete()
                break
                # ending the loop if user doesn't react after x seconds


    @commands.command(pass_context=True, aliases=['votacao'])
    async def enquete(self, ctx, *, arg):
        enquete = await ctx.channel.send(embed=discord.Embed(title='ENQUETE', description = f'{arg}', color=0xFECD00))
        await enquete.add_reaction('✅')
        await enquete.add_reaction('⛔')

    @commands.command(pass_context=True, aliases=['say', 'falar'])
    async def fale(self, ctx, *, arg):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(f'{arg} - {ctx.author.mention}')


    @commands.command(pass_context=True)
    async def embed(self, ctx, *, arg):
        await ctx.channel.purge(limit=1)
        em = discord.Embed(description=arg, color=0xFECD00)
        em.set_thumbnail(url='https://media.discordapp.net/attachments/752989626007945257/824313926224838656/e6a8aed12e9d87ede15d3f8887ee70b6.png?width=670&height=670')
        await ctx.channel.send(embed=em)

    @commands.command(pass_context=True)
    async def embed_sem(self, ctx, *, arg):
        await ctx.channel.purge(limit=1)
        em = discord.Embed(description=arg, color=0xFECD00)
        await ctx.channel.send(embed=em)

    @commands.command(pass_context=True)
    async def embed_url(self, ctx, url, *, arg):
        await ctx.channel.purge(limit=1)
        em = discord.Embed(description=arg, color=0xFECD00)
        em.set_thumbnail(url=url)
        await ctx.channel.send(embed=em)

    @commands.command(aliases=['imagem', 'foto'])
    async def img(self, ctx, arg):
        em = discord.Embed()
        em.set_image(url=arg)
        await ctx.channel.send(embed=em)


    @commands.command(aliases=['imagem_sem', 'foto_sem'])
    async def img_sem(self, ctx, arg):
        await ctx.channel.send(arg)


    @commands.command(pass_context=True, aliases=['msg'])
    async def mensagem(self, ctx, user : discord.Member = None, *, arg = None):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        if user == None:
            await ctx.channel.send(embed=discord.Embed(description='Você precisa informar um usuário. Ex: as!mensagem @jv olá jv!', color=0xff0000))
        else:
            if arg == None:
                await ctx.channel.send(embed=discord.Embed(description='Você precisa informar um texto para ser enviado. Ex: as!mensagem @jv olá jv!', color=0xff0000))
            else:
                await user.send(f'{arg} - enviada por: {ctx.author.name}')


    @commands.command(pass_context=True, aliases=['calculadora', 'calc', 'calcule'])
    async def calcular(self, ctx, *, arg = None):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        char_proib = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ç','~']
        index = []
        if arg == None:
            await ctx.channel.send(embed = discord.Embed(title='Você precisa informar o que quer calcular', description='Ex: as!calcular 1 + 1 * 2', color = 0xff0000))
        else:
            for e in char_proib:
                if e not in arg:
                    index.append('1')
                else:
                    index.append('0')
            if '0' not in index:
                em = discord.Embed(title = f'RESULTADO DE: {arg}', description = str(eval(arg)), color=0x9BCB64)
                em.set_thumbnail(url='https://cdn.discordapp.com/attachments/796529367046946876/796841376335527966/image-removebg-preview_4.png')
                await ctx.channel.send(f'{ctx.author.mention}', embed = em)
            else:
                await ctx.channel.send(embed = discord.Embed(description='**Não use carácteres especias!**', color = 0xff0000))


    @commands.command()
    async def avatar(self, ctx, other : discord.Member):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        global avatar
        global user_name
        user_name = other
        user_avatar = req.get(other.avatar_url)
        avatar = Image.open(BytesIO(user_avatar.content))
        avatar.save('avat.jpg', 'jpeg')
        file = discord.File(open('avat.jpg', 'rb'))  
        em = discord.Embed(title = f'FOTO DE PERFIL DE: {other}', color = 0xFECD00)
        em.set_image(url='attachment://avat.jpg')
        await ctx.channel.send(file=file, embed = em)
    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            avatar2 = avatar.resize((500, 500))
            avatar2.save('avat.gif', 'gif')
            file = discord.File(open('avat.gif', 'rb'))  
            em = discord.Embed(title = f'FOTO DE PERFIL DE: {user_name}', color = 0xFECD00)
            em.set_image(url='attachment://avat.gif')
            await ctx.channel.send(file=file, embed = em)
        else:
            raise error

    @commands.command(pass_context=True, aliases=['latencia'])
    async def ping(self, ctx):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        latencia_variavel = self.bot.latency
        embed = discord.Embed(title='Latência atual', description=f'**{str(latencia_variavel)}ms** \n{ctx.author}', color=0xffff00)
        embed.set_thumbnail(url='https://cdn.pixabay.com/photo/2012/04/01/19/21/exclamation-mark-24144_960_720.png')
        await ctx.channel.send(embed=embed)


    @commands.command()
    async def botinfo(self, ctx):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        latencia_variavel = self.bot.latency
        latencia = str(latencia_variavel)
        embed = discord.Embed(title='INFORMAÇÕES DO BOT:', description = f'**SOBRE MIM:**\n:wrench: **Nome:**  Enifler\n:wrench:**  Id:**  {self.bot.user.id}\n:wrench:  **Data de Criação:**  15/03/2021\n:wrench:**  Criador:**  jv#2121\n:wrench:**  Comandos:**  x\n:wrench:**  Modelo:**  Versão Platina - gerenciamento/staff/diversão/scraping\n:wrench:**  Linguagem:**  Python\n:wrench:**  Ping:**  {latencia}')
        await ctx.channel.send(embed=embed)


    @commands.command(pass_context=True, aliases=['cf', 'caraoucoroa', 'caracoroa', 'moeda', 'cc'])
    async def coinflip(self, ctx):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        moeda = randint(0, 1)
        if moeda == 0:
            embed = discord.Embed(title='CARA OU COROA:', description='Deu coroa !', color = 0xE9B545)
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/741306635372331089/806898017591754792/image-removebg-preview_6.png')  
        else:
            embed = discord.Embed(title='CARA OU COROA:', description='Deu cara !', color = 0xE9B545)
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/741306635372331089/806898025543893012/imagem_2021-02-04_114401-removebg-preview.png')  
        await ctx.channel.send(embed = embed)


    @commands.command(pass_context=True, aliases=['dice'])
    async def dado(self, ctx):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        num = randint(1,6)
        embed = discord.Embed(title='DADO', description = f'Você jogou o dado e ele parou no número: {num}', color=0x000000)
        if num == 6:
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/741306635372331089/807233745685577738/1612529900883.png')
        elif num == 5:
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/741306635372331089/807233745425268774/1612529873871.png')
        elif num == 4:
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/741306635372331089/807233745139662868/1612529787649.png')
        elif num == 3:
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/741306635372331089/807233744825876490/1612529764639.png')
        elif num == 2:
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/741306635372331089/807233744506454026/1612529681119.png')
        elif num == 1:
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/741306635372331089/807233743524855828/1612529648074.png')
        await ctx.channel.send(embed = embed)


    @commands.command(pass_context=True, aliases=['piadas', 'joke', 'jokes'])
    async def piada(self, ctx):
        if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.channel.send(f'"{choice(piadas)}"')



def setup(bot):
    bot.add_cog(Geral(bot))