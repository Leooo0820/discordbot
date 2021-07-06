import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re
url='https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx'
class lottery(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
    help = '''
    newest Lottery information.
    For example:
    $lotto (wait for the next instruction)
    01 02 03 04 05 06
    ''', 
    brief = "newest Lottery information."
    )
    async def lotto(self,ctx):
        def is_valid(m):
            return m.author==ctx.author
        await ctx.send("Enter your lottery number")
        n=await self.bot.wait_for('message',check=is_valid,timeout=300)
        m=n.content.split()
        if len(m)!=6:
            await ctx.send("Invalid input QQ")
            return
        for i in m:
            if m.count(i)>1:
                await ctx.send("Repeated or Invalid~ UWU")
                return
        r=requests.get(url)
        a=0
        lott1=[]
        soup=BeautifulSoup(r.text,'html.parser')
        period=soup.find_all("td",class_="td_w")
        await ctx.send(f"期別: {period[0].span.string}")
        lott=soup.find_all("td", class_="td_w font_black14b_center")
        for i in range(6):
            lott1.append(lott[i].span.string)
        await ctx.send("特別號(無請任意輸入字母)")
        res=await self.bot.wait_for('message',check=is_valid,timeout=300)
        spe=soup.find_all("td",class_="td_w font_red14b_center")
        special=spe[0].span.string
        if res.content==special:
            s=1
        else :
        	s=0
        award=soup.find_all('td',class_='td_w font_black14b td_hm')
        prize=[]
        for i in range(8,16):
            if award[i].span.string=='0':
                prize.append(award[i+8].span.string)
            else:
                prize.append(award[i].span.string)
        m=n.content.split()
        a=sum([1 for i in range(6) if m[i] in lott1])
        if a==3 and s==0:
        	await ctx.send(f"Win {prize[7]}")
        elif a==2 and s==1:
        	await ctx.send(f"Win {prize[6]}")
        elif a==3 and s==1:
        	await ctx.send(f"Win {prize[5]}")
        elif a==4 and s==0:
        	await ctx.send(f"Win {prize[4]}")
        elif a==4 and s==1:
        	await ctx.send(f"Win {prize[3]}")
        elif a==5 and s==0:
            await ctx.send(f"Win {prize[2]}")
        elif a==5 and s==1:
            await ctx.send(f"Win {prize[1]}")
        elif a==6 :
            await ctx.send(f"Win {prize[0]}")
        else:
            await ctx.send("So sad~uwu")
def setup(bot):
    bot.add_cog(lottery(bot))



                



              
