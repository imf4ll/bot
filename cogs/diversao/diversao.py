import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps
from random import choice
from strs import *
import textwrap
#from main import verify_channel


class Diversao(commands.Cog):
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
    #                 GERADOR DE MEMES                 =
    #===================================================

    @commands.command()
    async def hipocrisia(self, ctx, *, arg):
        if arg == None:
            await ctx.channel.send('**VOCÊ PRECISA ADICIONAR UMA FRASE JUNTO DO COMANDO PARA PODER GERAR UM MEME**')
            return

        await ctx.channel.purge(limit=1)
        base = Image.open( 'bases/hipocrisia.jpg' )
        fonte = ImageFont.truetype('fonts/arial.ttf', 30)
        texto = arg
        draw = ImageDraw.Draw(base)
        W, H = base.size
        y_texto = 20
        lines = textwrap.wrap(texto, width=33)
        for line in lines:
            w, h = fonte.getsize(line)
            draw.text(((W-w)/2, y_texto), 
                    line, font=fonte)
            y_texto += h
        base.save('tmpHipocrisia.png', format='PNG')
        file = discord.File(open('tmpHipocrisia.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)
    
    @commands.command()
    async def kiko(self, ctx, *, arg):
        if arg == None:
            await ctx.channel.send('**VOCÊ PRECISA ADICIONAR UMA FRASE JUNTO DO COMANDO PARA PODER GERAR UM MEME**')
            return
        await ctx.channel.purge(limit=1)
        base = Image.open( 'bases/kiko.png' )
        fonte = ImageFont.truetype('fonts/Digital.otf', 60)
        texto = arg
        draw = ImageDraw.Draw(base)
        W, H = base.size
        y_texto = 360
        lines = textwrap.wrap(texto, width=20)
        for line in lines:
            w, h = fonte.getsize(line)
            draw.text(((W-w)/2, y_texto), line, font=fonte)
            y_texto += h
        base.save('tmpKiko.png', format='PNG')
        file = discord.File(open('tmpKiko.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command()
    async def stonks(self, ctx, *, arg):
        if arg == None:
            await ctx.channel.send('**VOCÊ PRECISA ADICIONAR UMA FRASE JUNTO DO COMANDO PARA PODER GERAR UM MEME**')
            return
        await ctx.channel.purge(limit=1)
        base = Image.open( 'bases/stonks.jpg' )
        fonte = ImageFont.truetype('fonts/arial.ttf', 60)
        texto = arg
        draw = ImageDraw.Draw(base)
        W, H = base.size
        y_texto = 20
        lines = textwrap.wrap(texto, width=45)
        for line in lines:
            w, h = fonte.getsize(line)
            draw.text(((W-w)/2, y_texto), line, font=fonte)
            y_texto += h
        base.save('tmpStonks.png', format='PNG')
        file = discord.File(open('tmpStonks.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command()
    async def notstonks(self, ctx, *, arg):
        if arg == None:
            await ctx.channel.send('**VOCÊ PRECISA ADICIONAR UMA FRASE JUNTO DO COMANDO PARA PODER GERAR UM MEME**')
            return
        await ctx.channel.purge(limit=1)
        base = Image.open( 'bases/notstonks.jpg' )
        fonte = ImageFont.truetype('fonts/arial.ttf', 20)
        texto = arg
        draw = ImageDraw.Draw(base)
        W, H = base.size
        y_texto = 5
        lines = textwrap.wrap(texto, width=55)
        for line in lines:
            w, h = fonte.getsize(line)
            draw.text(((W-w)/2, y_texto), line, font=fonte)
            y_texto += h
        base.save('tmpNotStonks.png', format='PNG')
        file = discord.File(open('tmpNotStonks.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command()
    async def pegadinhas(self, ctx, *, arg):
        if arg == None:
            await ctx.channel.send('**VOCÊ PRECISA ADICIONAR UMA FRASE JUNTO DO COMANDO PARA PODER GERAR UM MEME**')
            return
        await ctx.channel.purge(limit=1)
        base = Image.open( 'bases/pegadinhas.jpg' )
        fonte = ImageFont.truetype('fonts/arial.ttf', 60)
        texto = arg
        draw = ImageDraw.Draw(base)
        W, H = base.size
        y_texto = 140
        lines = textwrap.wrap(texto, width=10)
        for line in lines:
            w, h = fonte.getsize(line)
            draw.text(((310-w)/2, y_texto), line, font=fonte, fill=(161,27,28))
            y_texto += h
        base.save('tmpPegadinhas.png', format='PNG')
        file = discord.File(open('tmpPegadinhas.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command()
    async def botao(self, ctx, *, arg):
        if arg == None:
            await ctx.channel.send('**VOCÊ PRECISA ADICIONAR UMA FRASE JUNTO DO COMANDO PARA PODER GERAR UM MEME**')
            return
        await ctx.channel.purge(limit=1)
        base = Image.open( 'bases/botoes.jpg' )
        fonte = ImageFont.truetype('fonts/arial.ttf', 20)
        texto = arg
        if '+' in texto:
            texto = texto.split('+')
            draw = ImageDraw.Draw(base)
            lines = textwrap.wrap(texto[0], width=12)
            y_texto = 50
            for texto[0] in lines:
                w, h = fonte.getsize(texto[0])
                draw.text(((180-w)/2, y_texto), texto[0], font=fonte, fill='black')
                y_texto += h
            lines = textwrap.wrap(texto[1], width=12)
            y_texto = 20
            for texto[1] in lines:
                w, h = fonte.getsize(texto[1])
                draw.text(((480-w)/2, y_texto), texto[1], font=fonte, fill='black')
                y_texto += h
            base.save('tmpBotao.png', format='PNG')
            file = discord.File(open('tmpBotao.png', 'rb'))
            await ctx.send(ctx.author.mention, file=file)
        else:
            embed = discord.Embed(description=f'**você precisa usar "+" para separar os dois botões** \n\n{ctx.author}', color = 0xff0000)
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def medo(self, ctx, *, arg):
        if arg == None:
            await ctx.channel.send('**VOCÊ PRECISA ADICIONAR UMA FRASE JUNTO DO COMANDO PARA PODER GERAR UM MEME**')
            return
        await ctx.channel.purge(limit=1)
        base = Image.open( 'bases/medo.jpg' )
        fonte = ImageFont.truetype('fonts/Digital.otf', 20)
        W, H = base.size
        texto = arg
        if '+' in texto:
            texto = texto.split('+')
            draw = ImageDraw.Draw(base)
            lines = textwrap.wrap(texto[0], width=50)
            y_texto = 100
            for texto[0] in lines:
                w, h = fonte.getsize(texto[0])
                draw.text(((W-w)/2, y_texto), texto[0], font=fonte, fill='black')
                y_texto += h
            lines = textwrap.wrap(texto[1], width=50)
            y_texto = 380
            for texto[1] in lines:
                w, h = fonte.getsize(texto[1])
                draw.text(((W-w)/2, y_texto), texto[1], font=fonte, fill='black')
                y_texto += h
            base.save('tmpMedo.png', format='PNG')
            file = discord.File(open('tmpMedo.png', 'rb'))
            await ctx.send(ctx.author.mention, file=file)
        else:
            embed = discord.Embed(description=f'**você precisa usar "+" para separar as frases** \n\n{ctx.author}', color=0xff0000)
            await ctx.channel.send(embed=embed)




    #===================================================
    #                   MEMES AMONG US                 =
    #===================================================
    @commands.command(pass_context=True, aliases=['join'])
    async def entrar(self, ctx, member : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [842371888750657546, 827681511234863124, 830941514830053436], 'Você deve usar este comando no canal <#827681511234863124>'): return
        if member == None:
            await ctx.channel.send(embed = discord.Embed(description="Você precisa informar um usuário", color=0xff0000)) 
            return
        await ctx.channel.purge(limit=1)
        teste = choice(among)
        texto =f'{member}'
        if teste == 'era':
            fundo = Image.open( 'among/{}.png'.format(choice(amongentrar_impostor)) )
            cor = 229,32,39
            W = 1150
        else:
            fundo = Image.open( 'among/{}.png'.format(choice(amongentrar_crewmate)) )
            cor = 'white'
            W = 1170
        fonte = ImageFont.truetype('fonts/arial.ttf', 20)
        w, h = fonte.getsize(texto)
        draw = ImageDraw.Draw(fundo)
        draw.text(((W-w)/2, 410), texto, font=fonte, fill=cor)
        fundo.save('tmpAmongentrar.png', format='PNG')
        file = discord.File(open('tmpAmongentrar.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command()
    async def entrarimpostor(self, ctx, member : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [842371888750657546, 827681511234863124, 830941514830053436], 'Você deve usar este comando no canal <#827681511234863124>'): return
        if member == None:
            await ctx.channel.send(embed = discord.Embed(description="Você precisa informar um usuário", color=0xff0000))
            return
        await ctx.channel.purge(limit=1)
        texto =f'{member}'
        fundo = Image.open( 'among/{}.png'.format(choice(amongentrar_impostor)) )
        fonte = ImageFont.truetype('fonts/arial.ttf', 20)
        w, h = fonte.getsize(texto)
        draw = ImageDraw.Draw(fundo)
        draw.text(((1150-w)/2, 400), texto, font=fonte, fill=(229,32,39))
        fundo.save('tmpAmongimpostor.png', format='PNG')
        file = discord.File(open('tmpAmongimpostor.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command()
    async def entrarcrewmate(self, ctx, member : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [842371888750657546, 827681511234863124, 830941514830053436], 'Você deve usar este comando no canal <#827681511234863124>'): return
        if member == None:
            await ctx.channel.send(embed = discord.Embed(description="Você precisa informar um usuário", color=0xff0000))
            return
        await ctx.channel.purge(limit=1)
        texto =f'{member}'
        fundo = Image.open( 'among/{}.png'.format(choice(amongentrar_crewmate)) )
        fonte = ImageFont.truetype('fonts/arial.ttf', 20)
        w, h = fonte.getsize(texto)
        draw = ImageDraw.Draw(fundo)
        draw.text(((1170-w)/2, 430), texto, font=fonte)
        fundo.save('tmpAmonginocente.png', format='PNG')
        file = discord.File(open('tmpAmonginocente.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command(pass_context=True, aliases=['leave'])
    async def ejetar(self, ctx, member : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [842371888750657546, 827681511234863124, 830941514830053436], 'Você deve usar este comando no canal <#827681511234863124>'): return
        if member == None:
            await ctx.channel.send(embed = discord.Embed(description="Você precisa informar um usuário", color=0xff0000))
            return
        await ctx.channel.purge(limit=1)
        texto =f'{member} {choice(among)} impostor'
        fundo = Image.open( 'among/{}.png'.format(choice(amongexpulsar_crewmate)) )
        fonte = ImageFont.truetype('fonts/arial.ttf', 20)
        W, H = fundo.size
        w, h = fonte.getsize(texto)
        draw = ImageDraw.Draw(fundo)
        draw.text(((W-w)/2, 240), texto, font=fonte)
        fundo.save('tmpAmongeflerpointsulsar.png', format='PNG')
        file = discord.File(open('tmpAmongeflerpointsulsar.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command()
    async def ejetarimpostor(self, ctx, member : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [842371888750657546, 827681511234863124, 830941514830053436], 'Você deve usar este comando no canal <#827681511234863124>'): return
        if member == None:
            await ctx.channel.send(embed = discord.Embed(description="Você precisa informar um usuário", color=0xff0000))
            return
        await ctx.channel.purge(limit=1)
        texto =f'{member} era o impostor'
        fundo = Image.open( 'among/{}.png'.format(choice(amongexpulsar_crewmate)) )
        fonte = ImageFont.truetype('fonts/arial.ttf', 20)
        W, H = fundo.size
        w, h = fonte.getsize(texto)
        draw = ImageDraw.Draw(fundo)
        draw.text(((W-w)/2, 240), texto, font=fonte)
        fundo.save('tmpAmongeflerpointsulsarImpostor.png', format='PNG')
        file = discord.File(open('tmpAmongeflerpointsulsarImpostor.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)

    @commands.command()
    async def ejetarcrewmate(self, ctx, member : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [842371888750657546, 827681511234863124, 830941514830053436], 'Você deve usar este comando no canal <#827681511234863124>'): return
        if member == None:
            await ctx.channel.send(embed = discord.Embed(description="Você precisa informar um usuário", color=0xff0000))
            return
        await ctx.channel.purge(limit=1)
        texto =f'{member} não era o impostor'
        fundo = Image.open( 'among/{}.png'.format(choice(amongexpulsar_crewmate)) )
        fonte = ImageFont.truetype('fonts/arial.ttf', 20)
        W, H = fundo.size
        w, h = fonte.getsize(texto)
        draw = ImageDraw.Draw(fundo)
        draw.text(((W-w)/2, 240), texto, font=fonte)
        fundo.save('tmpAmongeflerpointsulsarImpostor.png', format='PNG')
        file = discord.File(open('tmpAmongeflerpointsulsarImpostor.png', 'rb'))
        await ctx.send(ctx.author.mention, file=file)
    

    #===================================================
    #                     DIVERSÃO                     =
    #===================================================
    @commands.command()
    async def berti(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send(choice(lista_gif_berti))

    @commands.command()
    async def adm(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send(choice(lista_gif_adm))

    @commands.command()
    async def paitaon(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send(choice(lista_gif_paitaon))

    @commands.command()
    async def paitaoff(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send(choice(lista_gif_paitaoff))

    @commands.command()
    async def furro(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send('**MORRA FURRO, MORRA IMEDIATAMENTE**')
        await ctx.send(choice(lista_gif_furros))

    @commands.command()
    async def pato(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send('**PATO FODA D+ :sunglasses:**')
        await ctx.send(choice(lista_gif_patos))

    @commands.command()
    async def kawaii(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send(choice(lista_gif_kawai))

    @commands.command()
    async def bolsonaro(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send(choice(lista_gif_bolsonaro))

    @commands.command()
    async def salve(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send(choice(lista_salves))


    @commands.command()
    async def tapa(self, ctx, arg1 : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        if arg1 == None:
            await ctx.channel.send('**VOCÊ PRECISA MARCAR ALGÚEM PARA USAR ESTE COMANDO**')
            return
        embed = discord.Embed(description= '{} **deu um tapa em** {}'.format(ctx.author.mention, arg1), color=0x1f1d1d) 
        embed.set_image(url= choice(lista_gif_tapas))
        await ctx.channel.send(embed=embed)


    @commands.command()
    async def monkiflip(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.send('https://media.tenor.com/images/15c52fa732da36b258c4d58079780468/tenor.gif')

    @commands.command()
    async def xandao(self, ctx):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        await ctx.channel.send(choice(lista_gif_xandao))

    @commands.command()
    async def atirar(self, ctx, arg1 : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        if arg1 == None:
            await ctx.channel.send('**VOCÊ PRECISA MARCAR ALGÚEM PARA USAR ESTE COMANDO**')
            return
        if arg1 == ctx.author.mention:
            await ctx.channel.send('{} se matou kkkk'.format(ctx.author.mention))
            await ctx.channel.send(choice(lista_gif_suicidio))
        else:
            await ctx.channel.send('{} atirou em {} :boom::gun:'.format(ctx.author.mention, arg1))
            await ctx.channel.send(choice(lista_gif_atirar))

    @commands.command()
    async def beijar(self, ctx, arg1 : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        if arg1 == None:
            await ctx.channel.send('**VOCÊ PRECISA MARCAR ALGÚEM PARA USAR ESTE COMANDO**')
            return
        await ctx.channel.send('{} deu um beijão em {} :kiss:'.format(ctx.author.mention, arg1))
        await ctx.channel.send(choice(lista_gif_beijar))


    @commands.command()
    async def pinto(self, ctx, arg1 : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        if arg1 == None:
            await ctx.channel.send('**VOCÊ PRECISA MARCAR ALGÚEM PARA USAR ESTE COMANDO**')
            return
        tamanho_pinto = randint(0, 20)
        embed = discord.Embed(title= '**Pintometro**', description= 'O pinto do {} mede **{}cm!\n 8{}D**'.format(arg1, tamanho_pinto, '=' * tamanho_pinto), color=0x30caf4) 
        embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/jo/jonathanrb/pinto.png')
        await ctx.channel.send(embed=embed)


    @commands.command()
    async def gado(self, ctx, arg1 : discord.Member = None):
        if not await Diversao.verify_channel(self, ctx.channel.id, [], ''): return
        if arg1 == None:
            await ctx.channel.send('**VOCÊ PRECISA MARCAR ALGÚEM PARA USAR ESTE COMANDO**')
            return
        porcentagem_gado = randint(0, 100)
        embed = discord.Embed(title= '**Gadometro**', description= 'O {} é **{}% gado**'.format(arg1, porcentagem_gado), color=0x30caf4) 
        embed.set_thumbnail(url='https://cdn.awsli.com.br/800x800/462/462594/produto/29654470/63bc5f4ec0.jpg')
        await ctx.channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Diversao(bot))