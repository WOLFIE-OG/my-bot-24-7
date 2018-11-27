import discord
from discord.ext import commands

'''Module for custom PS Vita modding assistance commands.'''


class VitaAssistance:

    def __init__(self, bot):
        self.bot = bot

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def vitamodule(self, ctx):
        """Lists information on the module and links to the module"""
        await ctx.message.delete()
        embed = discord.Embed(title="T3CHNOLOG1C's custom Vita assistance module")
        embed.description = "Thanks for the interest in this module!"
        embed.add_field(name="What is this for?", value="This module is to help with Vita Hacking related assistance, primarily for the Vita Hacking server.")
        embed.add_field(name="Where can I download this?", value="https://github.com/T3CHNOLOG1C/vita-assistance")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def henguide(self, ctx):
        """Links to the guide."""
        await ctx.message.delete()
        embed = discord.Embed(title="Guide", color=discord.Color.blue())
        embed.set_author(name="T3CHNOLOG1C", url="https://psvita.guide/")
        embed.set_thumbnail(url="https://psvita.guide/images/bio-photo.png")
        embed.url = "https://psvita.guide/"
        embed.description = "A complete guide to PS Vita / Vita TV Homebrew Enablers, from stock to HENkaku Ensō (3.60), ePSP CFW (3.61-3.63) or ePSP Homebrew (3.65+)."
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def enso(self, ctx):
        """Ensō information"""
        await ctx.message.delete()
        embed = discord.Embed(title="What is HENkaku Ensō?", color=discord.Color.blue())
        embed.description = "HENkaku Ensō is the successor to the email exploit. It runs at boot and is easy to set up"
        embed.add_field(name="How do I switch from the email exploit to Ensō?", value="Follow the guide to [go from the offline exploit to boot9strap](https://psvita.guide/offline-to-enso).")
        embed.add_field(name="How do I install Ensō from stock (3.60 or below)?", value="Follow [the guide](https://psvita.guide).")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=["stock"])
    async def stock361(self, ctx):
        """Advisory for users on stock 3.61+ firmware"""
        await ctx.message.delete()
        embed = discord.Embed(title="Regarding users on stock 3.61+ firmware...", color=discord.Color.blue())
        embed.description = "You currently cannot get HENkaku Ensō on firmware versions above 3.60. Your best option is to [downgrade by replacing the motherboard](https://www.reddit.com/r/vitahacks/comments/59tv9u/downgrading_by_replacing_motherboard/) of your console with one that comes with firmware 3.60 or below."
        embed.add_field(name="I am unable to swap motherboards", value="If the above option is not an option for you, then you will **not be able** to run native Vita homebrew. **Downgrading is not possible without swapping the motherboard.** You can however, use [ARK ePSP CFW on 3.61-3.63](https://psvita.guide/ARK-ePSP(psvimgtools)) or use [VHBL on 3.65](https://psvita.guide/VHBL(psvimgtools).")
        embed.add_field(name="Can you inform me when an exploit is available?", value="You should either refer to [/r/vitahacks](https://www.reddit.com/r/vitahacks) or [Wololo](http://wololo.net).")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(VitaAssistance(bot))
