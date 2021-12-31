import discord
from discord.ext import commands
import requests as req
import os
from dotenv import load_dotenv, find_dotenv
import datetime
import asyncio

def valor_acoes(code):
    if type(code) == str:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={code}"
        res = req.request("GET", url).json()
        return int(float(res['lastPrice']))
    else:
        list_res = []
        for i in code:
            url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={i}"
            res = req.request("GET", url).json()
            list_res.append(res)
        list_cryptos = {}
        for i in list_res:
            print(i)
            list_cryptos[str(i['symbol'])] = [
                int(float(i['lastPrice'])),
                "{:.2f}".format(float(i['priceChangePercent']))
                ]
        return list_cryptos

def criar_conta(mem_id):
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

cryptos = {'BTC':'BTCBRL', 'ETH':'ETHBRL', 'BNB':'BNBBRL', 'LTC':'LTCBRL', 'AXS':'AXSBRL', 'SOL':'SOLBRL', 'DOT':'DOTBRL', 'LINK':'LINKBRL', 'CAKE':'CAKEBRL'}
cryptos_inverso = {'BTCBRL':'BTC', 'ETHBRL':'ETH', 'BNBBRL':'BNB', 'LTCBRL':'LTC', 'AXSBRL':'AXS', 'SOLBRL':'SOL', 'DOTBRL':'DOT', 'LINKBRL':'LINK', 'CAKEBRL':'CAKE'}
cryptos_nome = {'BTC':'Bitcoin', 'ETH':'Ethereum', 'BNB':'Binance Coin', 'LTC':'Litecoin', 'AXS':'Axie Infinity','SOL':'Solano', 'DOT':'Polkadot', 'LINK':'Chainlink', 'CAKE':'PancakeSwap'}

class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def isnumber(self, msg):
        try:
            int(msg)
            if int(msg) > 0:
                return True
            else:
                return False
        except:
            return False

    async def verify_channel(self, id, channels : None, msg: None):
        if id == 733851707800289340:
            await self.bot.get_channel(id).send('**Não é permitido o uso de comandos no chat <#733851707800289340>**')
            return False
        if id not in channels and len(channels) > 0:
            await self.bot.get_channel(id).send(msg)
            return False
        return True


    #===================================================
    #                  SISTEMA CRYPTO                  =
    #===================================================

    @commands.command(aliases=['exch', 'binance'])
    async def exchange(self, ctx):
        id = ctx.author.id
        criar_conta(id)
        if not await Crypto.verify_channel(self, ctx.channel.id, [880453245208764416, 842371888750657546], 'Você deve usar este comando no canal <#880453245208764416>'): return
        msg = await ctx.send('Coletando dados das criptomoedas <a:loading:871155991633342534>')
        await asyncio.sleep(1)
        await msg.delete()


        secure = False
        dia_banco = conta.find_one({'_id':id})['ultimoexchange']
        saldo = banco.find_one({'_id':id})['flerpoints']
        data = datetime.date.today()
        dia = '0' + str(data.day) if len(str(data.day)) == 1 else '' + str(data.day)
        mes = '0' + str(data.month) if len(str(data.month)) == 1 else '' + str(data.month)
        data = str(dia) + str(mes)

        if dia_banco != data:
            await ctx.send(ctx.author.mention, embed = discord.Embed( description = f'**Você utilizou sua consulta diária Gratuita! A partir da próxima, será cobrada uma taxa de `50` FlerPoints.**', color=0x3dff3d))
            secure = True
            data = datetime.date.today()
            dia = '0' + str(data.day) if len(str(data.day)) == 1 else '' + str(data.day)
            mes = '0' + str(data.month) if len(str(data.month)) == 1 else '' + str(data.month)
            data = str(dia) + str(mes)
            conta.find_one_and_update({'_id':id}, {'$set':{'ultimoexchange':data}})
        else:
            if saldo >= 50:
                banco.find_one_and_update({'_id':id}, {'$inc':{'flerpoints':-50}})
                await ctx.send(ctx.author.mention, embed = discord.Embed(description = f'**Foi cobrada uma taxa de `50` FlerPoints para realizar esta consulta.**', color=0xff3d3d))

                secure = True
            else:
                await ctx.channel.send(ctx.author.mention, embed = discord.Embed(description = f'{ctx.author.mention}, você não tem flerpoints o suficientes para verificar a exchange de criptomoedas', color=0xff0000))

        if secure == True:
            print('remove 50 flerpoints')
            embed=discord.Embed(title='EXCHANGE・Invista em Cripto Agora!', description='Utilize o comando `f!comprar` para Comprar e `f!vender` para Vender.\nEx: `f!comprar/vender <crypto> <quantidade> <preço>`.\n⠀', color=0xB588EC)  
            
            graficos = 'https://coinmarketcap.com/pt-br/currencies/bitcoin/ https://coinmarketcap.com/pt-br/currencies/ethereum/ https://coinmarketcap.com/pt-br/currencies/binance-coin/ https://coinmarketcap.com/pt-br/currencies/litecoin/ https://coinmarketcap.com/pt-br/currencies/axie-infinity/ https://coinmarketcap.com/pt-br/currencies/solana/ https://coinmarketcap.com/pt-br/currencies/polkadot-new/ https://coinmarketcap.com/pt-br/currencies/chainlink/ https://coinmarketcap.com/pt-br/currencies/pancakeswap/'.split()
            emojis_logos = "<:bitcoin:880881235159834624> <:ethereum:880881369813762118> <:binancecoin:880882818014654565> <:litecoin:880883095941828670> <:axie:880883712609361992> <:solano:885937537556807690> <:polkadot:885936994855837766> <:chainlink:885937487585878090> <:pancakeswap:885936857471410247>".split()
            codes = []
            for i in cryptos_inverso:codes.append(i)
            crypto_json = valor_acoes(codes)
            counter = 0
            for i in cryptos:
                counter +=1
                valor = crypto_json[cryptos[i]][0]
                porce = crypto_json[cryptos[i]][1]
                porcentagem = f"```diff\n+{porce}%```" if not '-' in porce else f"```diff\n{porce}%```"

                embed.add_field(name = f"{emojis_logos[counter - 1]} {str(cryptos_nome[i].capitalize())} ({i})", value = f"Price: `{valor}` FP・[Gráfico]({graficos[counter - 1]}){porcentagem}⠀", inline=True)
            
            embed.set_footer(text='⚠️ Atenção: Para a comprar e vender criptomoedas corretamente, utilize o código localizado após o nome da cripto.\n\n💡 Dica: Compre Criptos quando estiverem em baixa para vende-las quando estiverem em alta! Mas Cuidado! Nem sempre é assim.')
            await ctx.send(embed=embed)


    @commands.command()
    async def comprar(self, ctx, code = None, quant = None, price = None):       
        #registra o usuário
        id = ctx.author.id
        criar_conta(id)
        #realiza verificações de canal e parametros do comando
        if not await Crypto.verify_channel(self, ctx.channel.id, [880453245208764416, 842371888750657546], 'Você deve usar este comando no canal <#880453245208764416>'): return
        if code == None:
            await ctx.send(F"{ctx.author.mention}, **você precisa informar a criptomoeda que deseja comprar.\nEx: `f!comprar ETH 1 3500`**")
            return
        elif quant == None:
            await ctx.send(F"{ctx.author.mention}, **você precisa informar a quantidade de ações que deseja comprar \nEx: `f!comprar ETH 1 3500`**")
            return
        elif price == None:
            await ctx.send(F"{ctx.author.mention}, **você precisa informar o preço que irá comprar a criptomoeda\nEx: `f!comprar ETH 1 3500`**")
            return
        else:
            #verifica se a cripto escolhida existe
            criptos_code = []
            for i in cryptos:
                criptos_code.append(cryptos_inverso[cryptos[i]])
            if code not in criptos_code:
                await ctx.send(F"{ctx.author.mention}, **você precisa informar qual criptomoeda deseja vender corretamente.\nCopie e cole o código para garantir que está certo\n**")
                return
            #verifica se os paremtros são validos
            if (await Crypto.isnumber(self, quant) and await Crypto.isnumber(self, price)):
                #coleta os dados necessários e chama a api para pegar o valor
                quant = int(quant)
                price = int(price)
                user = conta.find_one({'_id':id})
                valor = int(valor_acoes(cryptos[code]))
                #verifica se o valor de ordem é maior que o valor da cripto
                if price >= valor:
                    #verifica se o usuário tem saldo o suficiente para comprar
                    if banco.find_one({"_id":id})['flerpoints'] >=  price * quant:
                        wallet = user['wallet']
                        #verifica se ele já tem o array da cripto na wallet dele
                        try:
                            wallet[code]
                        except:
                            wallet[code] = []
                        counter = 0
                        #percorre o array da cripto e vai adicionando os valores (se já tiver algum com o mesmo valor, ele soma com o objeto)
                        if wallet[code] != []:
                            for i in wallet[code]:
                                try:
                                    if i['preco'] == price:
                                        i['quantidade'] += quant
                                    else:
                                        counter += 1
                                except:
                                    wallet[code].append({'preco':price, 'quantidade':quant, 'code':code})
                        else:
                            wallet[code].append({'preco':price, 'quantidade':quant, 'code':code})
                        if counter == len(wallet[code]):
                            wallet[code].append({'preco':price, 'quantidade':quant, 'code':code})
                        #atualiza o banco de dados e envia a embed
                        conta.find_one_and_update({'_id':id}, {'$set':{'wallet':wallet}})
                        banco.find_one_and_update({"_id":id}, {'$inc':{'flerpoints':(price * quant) * -1}})
                        await ctx.channel.send(F'{ctx.author.mention}, você comprou {quant} Criptomoeda{"" if quant == 1 else "s"} de {cryptos_nome[code]}')
                    else:
                        await ctx.send(f"{ctx.author.mention}, você não possui dinheiro o suficiente para comprar estas criptos.")
                else:
                    await ctx.send(f'{ctx.author.mention}, O valor de compra que você inseriu é menor do que o atual ({valor}). Informe um valor igual ou um pouco maior para conseguir')
            else:
                await ctx.channel.send(F'{ctx.author.mention}, **a quantidade informada está incorreta. O valor não pode ser negativo ou nulo! Tente novamente com um valor correto!**')


    @commands.command()
    async def vender(self, ctx, code = None, quant : int = None, price : int = None):
        #registra o usuário
        id = ctx.author.id
        criar_conta(id)
        #realiza verificações de canal e parametros do comando
        if not await Crypto.verify_channel(self, ctx.channel.id, [880453245208764416, 842371888750657546], 'Você deve usar este comando no canal <#880453245208764416>'): return
        if code == None:
            await ctx.send(F"{ctx.author.mention}, **você precisa informar a criptomoeda que deseja vender.\nEx: `f!vender ETH 1 3500`**")
        elif quant == None:
            await ctx.send(F"{ctx.author.mention}, **você precisa informar a quantidade de criptos que deseja vender \nEx: `f!vender ETH 1 3500`**")
        elif price == None:
            await ctx.send(F"{ctx.author.mention}, **você precisa informar o preço que irá vender a criptomoeda\nEx: `f!comprar ETH 1 3500`**")
            return
        else:
            #verifica se os paremtros são validos
            if (await Crypto.isnumber(self, quant) and await Crypto.isnumber(self, price)):
                quant_inicial = int(quant)
                quant = int(quant)
                price = int(price)
                #verifica se a cripto escolhida existe
                criptos_code = []
                for i in cryptos:
                    criptos_code.append(i)
                if code not in criptos_code:
                    await ctx.send(F"{ctx.author.mention}, **você precisa informar qual criptomoeda deseja vender corretamente.\nCopie e cole o código para garantir que está certo\n**")
                else:
                    valor = int(valor_acoes(cryptos[code]))
                    criptos_total = conta.find_one({'_id':id})['wallet']
                    safe = False
                    real_quant = 0
                    for i in criptos_total[code]:
                        if i['code'] == code:safe=True
                        real_quant += i['quantidade']
                    if safe == True:
                        #verifica os valores
                        if real_quant >= quant:
                            price = int(price)
                            if price <= valor:
                                #faz um loop por todas as criptos e verifica se o preço é o mesmo
                                print(criptos_total)
                                print(criptos_total[code])
                                for i in criptos_total[code]:
                                    #se tiver mais criptos do q o cara quer vender, ele vende o valor definido e deixa o resto lá no obj
                                    if i['quantidade'] > quant:
                                        print(1)
                                        i['quantidade'] -= quant
                                        break
                                    #se a quantidade de criptos q o cara tiver for igual a que ele quer vender, o obj é deletado (vende tudo)
                                    elif i['quantidade'] == quant:
                                        print(2)
                                        criptos_total[code].remove(i)
                                        break
                                    else:
                                        #se a quantidade de criptos q o cara tiver for menor do que o cara quer vender, ele remove o que dá e retira o resto do próximo obj.
                                        print(3)
                                        quant -= i['quantidade']
                                        i['quantidade'] -= i['quantidade']
                                for i in range(0, quant_inicial):
                                    #limpa os objetos de criptos vazios
                                    for i in criptos_total[code]:
                                        print(0)
                                        if i['quantidade'] == 0:
                                            criptos_total[code].remove(i)
                                #loga no banco e envia a embed
                                print(price * quant_inicial)
                                conta.find_one_and_update({'_id':id}, {'$set':{'wallet':criptos_total}})
                                await ctx.channel.send(F'{ctx.author.mention}, **você vendeu {quant_inicial} {code}**')
                                banco.find_one_and_update({"_id":id}, {"$inc":{'flerpoints':price * quant_inicial}})
                            else:
                                await ctx.send(f'**{ctx.author.mention}, O valor de venda que você inseriu é maior do que o atual ({valor}). Informe um valor igual ou um pouco menor para conseguir efetivar a ordem de venda!**')
                        else:   
                            await ctx.send(F"{ctx.author.mention}, **você não possui esta quantidade de criptos. Compre mais para depois poder vende-las**")
                    else:
                        await ctx.send(F"{ctx.author.mention}, **você ainda não comprou cripto. Compre-a para depois poder vende-la**")
            else:
                await ctx.channel.send(F'{ctx.author.mention}, **a quantidade informada está incorreta. O valor não pode ser negativo ou nulo! Tente novamente com um valor correto!**')


    @commands.command(aliases=['wlt', 'carteira'])
    async def wallet(self, ctx, member:discord.Member = None):
        if not await Crypto.verify_channel(self, ctx.channel.id, [880453245208764416, 842371888750657546], 'Você deve usar este comando no canal <#880453245208764416>'): return
        if member == None:
            id = ctx.author.id
            name = ctx.author.name
            mention = ctx.author.mention
        else:
            id = member.id
            name = member.name
            mention = member.mention
        criar_conta(id)
        user_criptos = conta.find_one({'_id':id})['wallet']
        print(user_criptos)
        criptos_txt = ''
        
        #percorre e monta a string
        for e in user_criptos:
            for i in user_criptos[e]:
                print(i)
                criptos_txt += f"`{i['quantidade']}` **{cryptos_nome[i['code']]}({i['code']})** - comprada por `{i['preco']} FlerPoints`\n"

        if criptos_txt == '':
                await ctx.channel.send(F'{mention}, **{"você" if ctx.author.id == id else "o usuário mencioando "} ainda não possui nenhuma cripto. Use `f!exchange` para poder olhar a exchange de Criptomoedas**')
        else:
            await ctx.channel.send(embed = discord.Embed(title = f'CRIPTOS DE {str(name).upper()}', description = criptos_txt, color=0xB686EF))



def setup(bot):
    bot.add_cog(Crypto(bot))