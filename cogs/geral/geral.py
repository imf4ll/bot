import discord
from discord.ext import commands
import asyncio

class Geral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
        await ctx.channel.send(embed=em)


    @commands.command(pass_context = True, aliases = ['latencia'])
     async def ping(self, ctx):
        embed = discord.Embed(title = 'Latência', description = f'A latência atual é de **{round(self.bot.latency * 1000)}ms**', c  olor = 0xffff00)
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url='https://cdn.pixabay.com/photo/2012/04/01/19/21/exclamation-mark-24144_960_720.png')
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Geral(bot))
