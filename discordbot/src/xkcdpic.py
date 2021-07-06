import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re
import random 
import os
url=[] 
n='https://xkcd.com/' 
m=2467 
for i in range(1,2467): 
    url.append(n+str(i)) 
while True: 
    res=requests.get(n+str(m)) 
    if '200' in res: 
        url.append(n+str(m)) 
        m+=1 
    else: 
        break 
class xkcdpic(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command(
        help = '''
        find xkcd manga.
        For example:
        $xkcd (wait for next instruction)
        3,5,7
        ''', 
        brief = "find xkcd manga"
    )
    async def xkcd(self,ctx):
        def is_valid(m):
            return m.author==ctx.author
        url1=url 
        def pic():
            soup=BeautifulSoup(r.text,'html.parser') 
            res=soup.select('#comic>img') 
            if res==[]: 
                res=soup.select('#comic>a>img') 
            if res!=[]:
                result='https:'+res[0].attrs['src'] 
                image=requests.get(result) 
                result=result.replace('jpg','png')
                result=result.split('/')
                with open(os.path.join("..", "storage", "xkcd_pic.png"), "wb") as f:
                    f.write(image.content)
                    f.close()
        await ctx.send("指定範圍")
        b=await self.bot.wait_for('message',check=is_valid,timeout=300)
        try:
            c=int(b.content)
            if n+str(c) in url:
                b=int(c)
                r=requests.get(url1[c-1]) 
                pic()
                with open(os.path.join("..", "storage", "xkcd_pic.png"), "rb") as f:
                    picture = discord.File(f) 
                    await ctx.send(file = picture)
                    f.close()
            else:
                await ctx.send(f"查無 {c}")
        except:
            if b.content=='r' or b.content=='random': 
                random.shuffle(url1)
                r=requests.get(url1[0]) 
                pic()
                with open(os.path.join("..", "storage", "xkcd_pic.png"), "rb") as f:
                    picture = discord.File(f) 
                    await ctx.send(file = picture)
                    f.close()
            elif ',' in b.content: 
                b=b.content.split(',')
                for i in b: 
                    if n+str(i) in url: 
                        i=int(i)
                        r=requests.get(url1[i-1]) 
                        pic()
                        with open(os.path.join("..", "storage", "xkcd_pic.png"), "rb") as f:
                            picture = discord.File(f) 
                            await ctx.send(file = picture)
                            f.close()
                    else:
                        await ctx.send(f"查無 {i}")
            elif '-' in b.content:
                b=b.content.split('-')
                x,y=int(b[0]),int(b[-1])
                for i in range(x,y+1):
                    if n+str(i) in url:
                        i=int(i)
                        r=requests.get(url1[i-1]) 
                        pic() 
                        with open(os.path.join("..", "storage", "xkcd_pic.png"), "rb") as f:
                            picture = discord.File(f) 
                            await ctx.send(file = picture)
                            f.close()
                    else:
                        await ctx.send(f"查無 {str(i)}")
def setup(bot):
    bot.add_cog(xkcdpic(bot))