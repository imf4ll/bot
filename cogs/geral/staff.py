import discord
from discord.ext import commands
import asyncio

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #===================================================
    #                  COMANDOS STAFF                  =
    #===================================================
    @commands.command(pass_context = True)
    async def mute(self, ctx, member: discord.Member, temp : str = None):
        if temp == None:
            role = discord.utils.get(ctx.author.server.roles, name='Muted')
            await ctx.remove_roles(member, role)
        else:

            if 's' in temp:
                temp = int(temp.lower().replace('s', ''))
            elif 'm' in temp:
                temp = int(temp.lower().replace('m', '')) * 60
            elif 'h' in temp:
                temp = int(temp.lower().replace('h', '')) * 60 * 60
            elif 'd' in temp:
                temp = int(temp.lower().replace('d', '')) * 60 * 60 * 24

            muteRole = discord.utils.get(ctx.guild.roles,name="Muted")
            await member.add_roles(muteRole)

            warn_log = self.bot.get_channel(828481686512599070)
            
            embed=discord.Embed(title="Usuário Mutado!", description="**{0}** foi mutado por **{1}**!".format(member, ctx.message.author), color=0xff0000)
            await ctx.send(embed=embed)
            await warn_log.send(embed=embed)

            await asyncio.sleep(temp)
            await member.remove_roles(muteRole)

            embed=discord.Embed(title="Usuário Desmutado!", description="O tempo de mute de **{0}** acabou!".format(member), color=0xff0000)
            await ctx.send(embed=embed)
            await warn_log.send(embed=embed)

    @mute.error
    async def mute_error(ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            embed=discord.Embed(title="Permissão Negada.", description="Você não tem permissão para usar este comando.", color=0xff00f6)
            await ctx.send(embed=embed)
        else:
            raise error 

    @commands.command()
    @commands.has_permissions(ban_members=True) 
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title='Usuario punido', description=f'**Nome:** {member} \n**Guilda:** {ctx.guild}  \n**Motivo:** {reason} \n**Punição:** Kick \n\n**Aplicado por:** \n{ctx.author}', color=0xff0000)
        embed.set_thumbnail(url='https://media.gazetadopovo.com.br/2019/05/29175756/briga-irmaos-martelo-juiz-660x372.jpg')
        try:
            warn_log = self.bot.get_channel(828481686512599070) 
            await member.kick(reason=reason)
            await ctx.channel.send(embed=embed)
            try:
                await member.send(embed=embed)
            except:
                embed = discord.Embed(title=f'{member}', description=f'Usuario incapaz de receber mensagem DMs \n\n{ctx.author}', color=0xff0000)
                await ctx.channel.send(embed=embed)
                await warn_log.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Não posso Kickar este usuario', description=f'{member} \n\n{ctx.author}', color=0x0000ff)
            await ctx.channel.send(embed=embed)
            await warn_log.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members=True) 
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title='Usuario punido', description=f'**Nome:** {member} \n**Guilda:** {ctx.guild} \n**Motivo:** {reason} \n**Punição:** Ban \n\n**Aplicado por:** \n{ctx.author}', color=0xff0000)
        embed.set_thumbnail(url='https://media.gazetadopovo.com.br/2019/05/29175756/briga-irmaos-martelo-juiz-660x372.jpg')
        try:
            warn_log = self.bot.get_channel(828481686512599070)
            await member.ban(reason=reason)
            await ctx.channel.send(embed=embed)
            try:
                await member.send(embed=embed)
            except:
                embed = discord.Embed(title=f'{member}', description=f'Usuario incapaz de receber mensagem DMs \n\n{ctx.author}', color=0xff0000)
                await ctx.channel.send(embed=embed)
                await warn_log.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Não posso Banir este usuario', description=f'{member} \n\n{ctx.author}', color=0xff0000)
            await ctx.channel.send(embed=embed)
            await warn_log.send(embed=embed)

    '''
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, other: discord.Member, *, arg : str = None):
        id = str(ctx.author.id)
        criar_conta(id)
        if arg == None:
            arg = 'Causa não informada'
        other_id = str(other.id)

        if other_id not in logs:
            criar_conta(other_id)

        logs[other_id]['warnings'].append(f'"{arg}" - autor: {ctx.author.name}')
        logs[other_id]['count'] += 1
        em = discord.Embed(title = f'{other.name} foi avisado', description = f'🛑 {other.mention} recebeu um **aviso** de {ctx.author.mention} 🛑\nMotivo: "{arg}".', color = 0xff0000)
        em.set_thumbnail(url='https://i.pinimg.com/474x/6e/d2/3c/6ed23c7f96498fe1fb56022077a352a7.jpg')
        await ctx.channel.send(embed=em)
        warn_log = self.bot.get_channel(828481686512599070)
        await warn_log.send(embed=embed)
        _save()
        if other == None:
            await ctx.send(embed=discord.Embed(description='Você precisa informar o usuário. Ex: f!warn @jv', color=0xff0000))
    @warn.error
    async def warn_error(ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(embed=discord.Embed(description='Você não tem permissão para usar este comando', color=0xff0000))
        else:
            raise error


    @commands.command(pass_context=True)
    async def warnings(self, ctx, other : discord.Member):
        other_id = str(other.id)
        if other_id not in logs:
            await ctx.send(embed=discord.Embed(description='Este usuário ainda não tem nenhum warn', color=0xff0000))
        else:
            if logs[other_id]['warnings'] == []:
                await ctx.send(embed=discord.Embed(description='Este usuário ainda não tem nenhum warn', color=0xff0000))
            else:
                avisos_str = ''
                await ctx.channel.send(embed = discord.Embed(title = f'Warnings de {other.name}: ', color = 0xFECD00))
                tamanho_aval = len(logs[other_id]['warnings'])
                i = 0
                while i < tamanho_aval:
                    avisos_str = avisos_str + '\n' + logs[other_id]['warnings'][i]
                    i += 1
                await ctx.channel.send(embed = discord.Embed(description = avisos_str, color = 0x5e11ab))
                _save()
    @warnings.error
    async def warnings_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(description='Você precisa informar o usuário. Ex: ms!warnings @jv', color=0xff0000))
        else:
            raise error


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def remover(self, ctx, arg, other: discord.Member, arg1 : int):
        other_id = str(other.id)
        if other_id not in logs:
            await ctx.send(embed=discord.Embed(description='Este usuário ainda não tem nenhum warn', color=0xff0000))
        else:
            if arg == 'warn' and arg1 > 0:
                num = int(arg1) - 1
                aviso = logs[other_id]["warnings"][num].replace('"', '')
                warn_log = self.bot.get_channel(828481686512599070)
                await ctx.channel.send(embed = discord.Embed(title = f'O aviso "{aviso}" foi removido', color = 0xFECD00))
                await warn_log.send(embed = discord.Embed(title = f'O aviso "{aviso}" foi removido', color = 0xFECD00))
                del(logs[other_id]['warnings'][num])
                logs[other_id]['count'] -= 1
            else:
                await ctx.channel.send(embed = discord.Embed(title='Você precisa informar o que quer remover corretamente.', description='Ex: as!remover warn @jv 1', color = 0xff0000))
            _save()
    @remover.error
    async def remover_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(embed = discord.Embed(title='Você precisa informar o que quer remover corretamente.', description='Ex: as!remover warn @jv 1', color = 0xff0000))
        else:
            raise error
    @remover.error
    async def remover_error2(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(embed=discord.Embed(description='Você não tem permissão para usar este comando', color=0xff0000))
        else:
            raise error
    '''

    @commands.command(pass_context=True, aliases=['clear'])
    @commands.has_permissions(manage_messages=True)                                                                            
    async def limpar(self, ctx, amount=0):
        await ctx.channel.purge(limit=1)
        if amount > 1000 or amount <= 1:
            embed = discord.Embed(title='**Só limpo entre 2 e 100 mensagens por vez**', description=f'{ctx.author}')
            embed.set_thumbnail(url='https://cdn.pixabay.com/photo/2012/04/01/19/21/exclamation-mark-24144_960_720.png')
            await ctx.send(embed=embed) 
        else:
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(title = f'**{amount} mensagens foram apagadas!**', description=f'{ctx.author}')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/775809271995957251/776204349809885244/devot.png')
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Staff(bot))