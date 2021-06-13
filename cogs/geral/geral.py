import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv, find_dotenv


class Geral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    '''
    async def verify_channel(self, id, channels : None, msg: None):
        if id == 743482860161466509:
            await self.bot.get_channel(id).send('**Não é permitido o uso de comandos no chat <#743482860161466509>**')
            return False
        if id not in channels and len(channels) > 0:
            await self.bot.get_channel(id).send(msg)
            return False
        return True
    '''

    #===================================================
    #                      GERAL                       =
    #===================================================

    @commands.command(aliases=['h', 'ajuda', 'comandos', 'commands'])
    async def help(self, ctx):
        print('help')

    @commands.command(pass_context=True)
    async def embed(self, ctx, *, arg):
        await ctx.channel.purge(limit=1)
        em = discord.Embed(description=arg, color=0xFECD00)
        em.set_thumbnail(url='https://images-ext-2.discordapp.net/external/hC40eQUDn5ZDoR9ahV_MU2WOIojJBoP6V2eh3dYmPHw/%3Fsize%3D2048/https/cdn.discordapp.com/icons/743482187365613641/a_1f4a7a14c16f1dd1e00eec21c9fddb12.gif')
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


    @commands.command(pass_context=True, aliases=['latencia'])
    async def ping(self, ctx):
        #if not await Geral.verify_channel(self, ctx.channel.id, [], ''): return
        latencia_variavel = self.bot.latency
        embed = discord.Embed(title='Latência atual', description=f'**{str(latencia_variavel)}ms** \n{ctx.author}', color=0xffff00)
        embed.set_thumbnail(url='https://cdn.pixabay.com/photo/2012/04/01/19/21/exclamation-mark-24144_960_720.png')
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Geral(bot))