from redbot.core import commands
import os


class CMD(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def cmd(self, ctx, arg, *arg2):
        await ctx.send("```sh\n" + os.popen(arg + " " + " ".join(arg2) if type(arg2) is tuple else "").read() + "\n```")
