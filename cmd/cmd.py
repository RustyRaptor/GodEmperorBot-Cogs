from redbot.core import commands
import os


class CMD(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def cmd(self, ctx, arg, *arg2):
        command = arg
        args = " ".join(arg2)
        print("THIS IS IT THIS IS THE OMMAND ARGSSSSS", arg2)
        print(args)
        output = os.popen(command + " " + args).read()

        await ctx.send("```\n" + output + "\n" + "```")
