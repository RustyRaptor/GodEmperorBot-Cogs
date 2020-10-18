from redbot.core import commands
from redbot.core import Config
from redbot.core import checks
import os


class CMD(commands.Cog):
    """My custom cog"""

    @commands.guild_only()
    @checks.is_owner()
    @commands.command()
    async def cmd(self, ctx, arg, *arg2):
        command = arg
        args = " ".join(arg2)
        print("THIS IS IT THIS IS THE OMMAND ARGSSSSS", arg2)
        print(args)
        output = os.popen(command + " " + args).read()

        await ctx.send("```\n" + output + "\n" + "```")
