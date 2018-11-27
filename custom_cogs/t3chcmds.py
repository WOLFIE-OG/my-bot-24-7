import discord
from discord.ext import commands

'''Just a bunch of ascii faces and such.'''


class T3CHCmds:

    def __init__(self, bot):
        self.bot = bot
		
    @commands.command()
    async def xd(self, ctx):
        """Large XD made of XDs"""
        await ctx.message.edit(content='XD      XD    XD  XD\n  XD  XD      XD      XD\n     XD           XD       XD\n  XD  XD      XD      XD\nXD      XD    XD  XD')

    @commands.command()
    async def lenny(self, ctx):
        """( ͡° ͜ʖ ͡°)"""
        await ctx.message.exit(content='( ͡° ͜ʖ ͡°)')

    @commands.command()
    async def shrug(self, ctx):
        """¯\_(ツ)_/¯"""
        await ctx.message.exit(content='¯\_(ツ)_/¯')
    
    @commands.command()
    async def magic(self, ctx):
        """(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ"""
        await ctx.message.edit(content='(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ')

    @commands.command()
    async def tableflip(self, ctx):
        """(ノಠ益ಠ)ノ彡┻━┻"""
        await ctx.message.edit(content='(ノಠ益ಠ)ノ彡┻━┻')

    @commands.command()
    async def unflip(self, ctx):
        """ ┬─┬ ノ( ゜-゜ノ)"""
        await ctx.message.edit(content=' ┬─┬ ノ( ゜-゜ノ)')

    @commands.command()
    async def wtf(self, ctx):
        """Ծ_Ծ"""
        await ctx.message.edit(content='Ծ_Ծ')

    @commands.command()
    async def soon(self, ctx):
        """™"""
        await ctx.message.edit(content='Soon™')

    @commands.command()
    async def lennyshrug(self, ctx):
        """¯\_( ͡° ͜ʖ ͡°)_/¯"""
        await ctx.message.edit(content='¯\_( ͡° ͜ʖ ͡°)_/¯')

def setup(bot):
    bot.add_cog(T3CHCmds(bot))
