import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.command()
    async def ping(self, ctx):
        ping_embed = discord.Embed(title="ping", description="Latency in ms", color=discord.Color.blue())
        ping_embed.add_field(name=f"{self.bot.user.name}'s latency (ms): ", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
        ping_embed.set_footer(text=f"Requested by {ctx.author.name}.", icon_url=ctx.author.avatar)
        await ctx.send(embed=ping_embed)
        
async def setup(bot):
    await bot.add_cog(Test(bot))