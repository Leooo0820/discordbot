import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re
import os
rank_url='https://playboard.co/en/youtube-ranking/'
class N:
    def __init__(self, dimension, country, period):
        self.dimension=dimension
        self.country=country
        self.period=period
    def __repr__(self):   
        return f"{self.dimension} {self.country} {self.period}"
class ranking(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(
        help = '''
        Rank on playboard.
        For example:
        $rank most-superchatted south-korea daily
        ''', # 輸入 $help rank 時顯示
        brief = "youtube ranking." # 輸入 $help 時顯示
    )
    async def rank(self,ctx,dimension,country,period):
        def is_valid(m):
            return m.author==ctx.author
        try :
            n=N(dimension,country,period)
            r=requests.get(f"{rank_url}{n.dimension}-all-channels-in-{n.country}-{n.period}")
            soup=BeautifulSoup(r.text,'html.parser')
            channel=soup.find_all("h3")
            channel1=soup.find_all("img")
            date=soup.find_all("li",class_="item item--selected")
            await ctx.send(f"Time : {date[-1].span.string}")
            await ctx.send("查第幾名(1~15)")
            await ctx.send("可以查10次，q 或 quit退出")
            for j in range(10):
                ans=await self.bot.wait_for('message',check=is_valid,timeout=300)
                try:
                    i=int(ans.content)
                    if i>15:
                        await ctx.send("Out of range sry~")
                    else:
                        name=channel[i+4].string
                        res=channel1[i-1].attrs['data-src']
                        pic=requests.get(res)
                        await ctx.send(f"Num {i} is {name}\n")
                        with open(os.path.join("..", "storage", "rank_logo.png"), "wb") as f:
                            f.write(pic.content)
                            f.close()
                        with open(os.path.join("..", "storage", "rank_logo.png"), "rb") as f:
                            picture = discord.File(f) 
                            await ctx.send(file = picture)
                            f.close()
                except:
                    if ans.content=='q' or ans.content=='quit':
                        await ctx.send("Quit!!!")
                        return
                    elif '$' in ans.content:
                        return
                    else:
                        await ctx.send("Invalid input QAQ")
            await ctx.send("Toooo many times~")
        except:
            await ctx.send("Invalid input ><")
            return
def setup(bot):
    bot.add_cog(ranking(bot))


