import discord
from discord.ext import commands
import asyncio
import datetime
from utils.mongoconnect import mongoConnect

cluster = mongoConnect()
db = cluster['codify']
conta = db['conta']

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def criar_conta(self, mem_id):
        if mem_id != 851618408965079070:
            try:    
                await conta.insert_one({"_id":mem_id, "saldo":0, "stars":[], "wallet":{}, "warnings":[], 'xp':0, "level":0, "descricao":"Use .descricao para alterar a sua descrição"})
            except:
                pass
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

            muteRole = discord.utils.get(ctx.guild.roles,name="mutado")
            await member.add_roles(muteRole)

            warn_log = self.bot.get_channel(743492526542946424)
            
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
    @commands.has_permissions(kick_members=True) 
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title='Usuario punido', description=f'**Nome:** {member} \n**Guilda:** {ctx.guild}  \n**Motivo:** {reason} \n**Punição:** Kick \n\n**Aplicado por:** \n{ctx.author}', color=0xff0000)
        embed.set_thumbnail(url='https://media.gazetadopovo.com.br/2019/05/29175756/briga-irmaos-martelo-juiz-660x372.jpg')
        try:
            warn_log = self.bot.get_channel(743492526542946424) 
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
            warn_log = self.bot.get_channel(743492526542946424)
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

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member = None, *, motivo : str = None):
        id = member.id
        await Staff.criar_conta(self, id)

        if member == None:
            await ctx.send(embed=discord.Embed(description='Você precisa informar quem será avisado. Ex: .warn @jv mto lindo', color=0xff0000))
        if motivo == None:
            motivo = 'Motivo não definido'

        data_pura = date.today()
        data = data_pura.strftime('%D/%M/%Y')
        hora_pura = datetime.datetime.now() - datetime.timedelta(hours=3)
        hora = hora_pura.strftime('%H:%M')

        novo_aviso = f'> Motivo: {motivo}\n> Aplicador: {ctx.author}\n> Data e hora: {str(data) + " | " + str(hora)}'
        conta.find_one_and_update({'_id':id}, {'$push':{'warnings':novo_aviso}})

        em = discord.Embed(title = f'{member.name} foi avisado', description = f'🛑 {member.mention} recebeu um **aviso** de {ctx.author.mention} 🛑\nMotivo: "{motivo}".', color = 0xff0000)
        em.set_thumbnail(url='https://i.pinimg.com/474x/6e/d2/3c/6ed23c7f96498fe1fb56022077a352a7.jpg')
        await ctx.channel.send(embed=em)
        warn_log = self.bot.get_channel(743492526542946424)
        await warn_log.send(embed=em)
    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(embed=discord.Embed(description='Você não tem permissão para usar este comando', color=0xff0000))
        else:
            raise error


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def warnings(self, ctx, member : discord.Member = None):
        if member == None:
            await ctx.send(embed=discord.Embed(description='Você precisa informar um usuário. Ex: .warnings @jv mto lindo', color=0xff0000))
            return
        member_id = member.id 
        warns = conta.find_one({'_id':member_id})['warnings']
        if len(warns) == 0:
            await ctx.send(embed=discord.Embed(description='Este usuário não possui nenhum aviso', color=0xff0000))  
        else:
            msg = ''
            for i in warns:
                msg += f'{i}\n\n'
            await ctx.send(embed=discord.Embed(title=f'warnings de {member.name}', description=msg, color=0x1CFEFE)) 


    @warnings.error
    async def warnings_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(embed=discord.Embed(description='Você não tem permissão para usar este comando', color=0xff0000))
        else:
            raise error


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def unwarn(self, ctx, member: discord.Member, arg1 : int):
        member_id = member.id 
        if member == None:
            await ctx.send(embed=discord.Embed(description='Você precisa informar um usuário. Ex: .unwarn @jv 1', color=0xff0000))
        if arg1 == None:
            await ctx.send(embed=discord.Embed(description='Você precisa informar o número do aviso que deseja remover. Ex: .unwarn @jv 1', color=0xff0000))
        else:
            try:
                warns = conta.find_one({'_id':member_id})['warnings']
                warns.pop(int(arg1) - 1)
                
                conta.find_one_and_update({'_id':member_id}, {'$set':{'warnings':warns}})
                await ctx.send(embed=discord.Embed(description='Aviso removido!', color=0x1CFEFE))
            except:
                await ctx.send(embed=discord.Embed(description='Este usuário não possui nenhum aviso', color=0xff0000))   

    @unwarn.error
    async def unwarn_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(embed=discord.Embed(description='Você não tem permissão para usar este comando', color=0xff0000))
        else:
            raise error

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
