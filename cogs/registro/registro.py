import discord
from discord.ext import commands
import asyncio
from utils.mongoconnect import mongoConnect

cluster = mongoConnect()
db = cluster['codify']
conta = db['conta']
logs = db['logs']

class Registro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print('reação')
        emoji = str(payload.emoji)
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = message.guild
        user = await guild.fetch_member(payload.user_id)
        if channel.id == 743490687353487460:
            emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '🚹', '🚺', '🚼', '🟩', '🟢', '🟦', '🔵', '🟪', '🟣', '🌷', '🌸', '🟥', '🔴', '🟧', '🟠', '🟨', '🟡', '⬜', '⬛', '<:xxc:745084475402354718>',  '<:xxC:745084615160758352>',  '<:xx_csharp:745084850838569161>',  '<:xx_css:745084407265624244>',  '<:xx_html:745084335299887144>',  '<:xx_java:745084182354460742>',  '<:xx_JavaScript:745084094840438895>',  '<:xx_php:819281651631652896>',  '<:xx_python:745084957587931277>',  '<:xx_rust:819278093759807498>',  '<:xx_lua:759787810382675968>',  '<:xx_golang:819280057179832320>',  '<:xx_elixir:904837194852761600>',  '<:xx_ruby:904833654432337950>', '<:xy_vscode:819282673670291547>', '<:xy_jetbrains:745085628571582464>', '<:xy_sublimetext:745086136371642418>', '<:xy_eclipse:745086369029685301>', '<:xy_netbeans:746884552395325490>', '<:xy_vim:815271719824130058>', '<:xx_emacs:912057023514951771>', '⌨️', '🚫', '<:xa_designer:778104411711995934>', '<:bb_terminal:770642267463614504>', '<:xa_gamedev:778102624792477707>', '<:xa_frontend:778107468458098688>', '<:xa_backend:778106636593266699>', '<:xa_fullstack:778103884341575720>', '<:xa_bancodedados:778103884433588235>', '<:xa_servidor:778102616810192897>', '<:xa_mobile:778103884853936159>', '<:xa_desktop:778103885147406356>', '✅', '🔔']
            roles = ['743504369059889178', '743504370913509406', '743504376496259164', '743504676292657203', '743504686392279121', '743525068868550657', '743525096676655185', '821454370120925225', '743529159833288794', '743529159690682528', '743527187533004870', '743527185712808146', '743529159552139286', '743529159296286772', '743528964479254538', '743528962474377227', '743527183821308046', '743527181975552051', '743527179257774241', '743527162732216392', '743527160903368808', '743527159406002238', '743528960373293066', '743528957369909339', '745234055804616765', '745234075131969546', '745234102952787969', '745234022149390367', '745233977304023110', '745233859116793906', '745233933330939944', '745234155129929738', '745234190915731560', '844221994010411038', '808106726116425758', '844222602021175356', '904837424574758952', '904834425567711253', '745293963828658176', '745294152429994064', '745294098520342631', '745294034116804628', '746884082771689522', '844232644966613012', '844232638222303303', '761022873762005023', '842729167887401000', '761023038279122985', '761023097666797608', '778101737562701825', '778101499309850624', '778101501460611072', '778100207400648704', '771802609509466182', '778101688983748649', '778101496822497322', '778101642112401408', '745666021024858194', '778068609951989850']
            for i in emojis:
                if i == emoji:
                    try:
                        role_id = roles[emojis.index(i)]
                        role = guild.get_role(int(role_id))
                        await user.add_roles(role)
                    except:
                        pass
        elif channel.id == 904532938341896233:
            emojis = ['<:xxc:745084475402354718>',  '<:xxC:745084615160758352>',  '<:xx_csharp:745084850838569161>',  '<:xx_css:745084407265624244>',  '<:xx_html:745084335299887144>',  '<:xx_java:745084182354460742>',  '<:xx_JavaScript:745084094840438895>',  '<:xx_php:819281651631652896>',  '<:xx_python:745084957587931277>',  '<:xx_rust:819278093759807498>',  '<:xx_lua:759787810382675968>',  '<:xx_golang:819280057179832320>',  '<:xx_elixir:904837194852761600>','<:xa_servidor:778102616810192897>', '<:xa_fullstack:778103884341575720>', '<:xa_bancodedados:778103884433588235>', '<:bb_terminal:770642267463614504>']
            roles = [904487025070202880, 904487025070202880, 904487465983836210, 904487582161829908, 904487582161829908, 904487962128027748, 904485429896679464, 904486369349496922, 904486056739631174, 904485830792462336, 904488063168831558, 904487915940376636, 904829041259970601, 904829006501793892, 904834155030937650, 904513289998970890, 904484232645197845]
            for i in emojis:
                if i == emoji:
                    try:
                        role_id = roles[emojis.index(i)]
                        role = guild.get_role(int(role_id))
                        await user.add_roles(role)
                    except:
                        pass


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        print('reação')
        emoji = str(payload.emoji)
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = message.guild
        user = await guild.fetch_member(payload.user_id)
        if channel.id == 743490687353487460:
            emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '🚹', '🚺', '🚼', '🟩', '🟢', '🟦', '🔵', '🟪', '🟣', '🌷', '🌸', '🟥', '🔴', '🟧', '🟠', '🟨', '🟡', '⬜', '⬛', '<:xxc:745084475402354718>',  '<:xxC:745084615160758352>',  '<:xx_csharp:745084850838569161>',  '<:xx_css:745084407265624244>',  '<:xx_html:745084335299887144>',  '<:xx_java:745084182354460742>',  '<:xx_JavaScript:745084094840438895>',  '<:xx_php:819281651631652896>',  '<:xx_python:745084957587931277>',  '<:xx_rust:819278093759807498>',  '<:xx_lua:759787810382675968>',  '<:xx_golang:819280057179832320>',  '<:xx_elixir:904837194852761600>',  '<:xx_ruby:904833654432337950>', '<:xy_vscode:819282673670291547>', '<:xy_jetbrains:745085628571582464>', '<:xy_sublimetext:745086136371642418>', '<:xy_eclipse:745086369029685301>', '<:xy_netbeans:746884552395325490>', '<:xy_vim:815271719824130058>', '<:xx_emacs:912057023514951771>', '⌨️', '🚫', '<:xa_designer:778104411711995934>', '<:bb_terminal:770642267463614504>', '<:xa_gamedev:778102624792477707>', '<:xa_frontend:778107468458098688>', '<:xa_backend:778106636593266699>', '<:xa_fullstack:778103884341575720>', '<:xa_bancodedados:778103884433588235>', '<:xa_servidor:778102616810192897>', '<:xa_mobile:778103884853936159>', '<:xa_desktop:778103885147406356>', '✅', '🔔']
            roles = ['743504369059889178', '743504370913509406', '743504376496259164', '743504676292657203', '743504686392279121', '743525068868550657', '743525096676655185', '821454370120925225', '743529159833288794', '743529159690682528', '743527187533004870', '743527185712808146', '743529159552139286', '743529159296286772', '743528964479254538', '743528962474377227', '743527183821308046', '743527181975552051', '743527179257774241', '743527162732216392', '743527160903368808', '743527159406002238', '743528960373293066', '743528957369909339', '745234055804616765', '745234075131969546', '745234102952787969', '745234022149390367', '745233977304023110', '745233859116793906', '745233933330939944', '745234155129929738', '745234190915731560', '844221994010411038', '808106726116425758', '844222602021175356', '904837424574758952', '904834425567711253', '745293963828658176', '745294152429994064', '745294098520342631', '745294034116804628', '746884082771689522', '844232644966613012', '844232638222303303', '761022873762005023', '842729167887401000', '761023038279122985', '761023097666797608', '778101737562701825', '778101499309850624', '778101501460611072', '778100207400648704', '771802609509466182', '778101688983748649', '778101496822497322', '778101642112401408', '745666021024858194', '778068609951989850', '']
            for i in emojis:
                if i == emoji:
                    try:
                        role_id = roles[emojis.index(i)]
                        role = guild.get_role(int(role_id))
                        await user.remove_roles(role)
                    except:
                        pass
        if channel.id == 904532938341896233:
            emojis = ['<:xxc:745084475402354718>',  '<:xxC:745084615160758352>',  '<:xx_csharp:745084850838569161>',  '<:xx_css:745084407265624244>',  '<:xx_html:745084335299887144>',  '<:xx_java:745084182354460742>',  '<:xx_JavaScript:745084094840438895>',  '<:xx_php:819281651631652896>',  '<:xx_python:745084957587931277>',  '<:xx_rust:819278093759807498>',  '<:xx_lua:759787810382675968>',  '<:xx_golang:819280057179832320>',  '<:xx_elixir:904837194852761600>','<:xa_servidor:778102616810192897>', '<:xa_fullstack:778103884341575720>', '<:xa_bancodedados:778103884433588235>', '<:bb_terminal:770642267463614504>']
            roles = [904487025070202880, 904487025070202880, 904487465983836210, 904487582161829908, 904487582161829908, 904487962128027748, 904485429896679464, 904486369349496922, 904486056739631174, 904485830792462336, 904488063168831558, 904487915940376636, 904829041259970601, 904829006501793892, 904834155030937650, 904513289998970890, 904484232645197845]
            for i in emojis:
                if i == emoji:
                    try:
                        role_id = roles[emojis.index(i)]
                        role = guild.get_role(int(role_id))
                        await user.remove_roles(role)
                    except:
                        pass

def setup(bot):
    bot.add_cog(Registro(bot))
