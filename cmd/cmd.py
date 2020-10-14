from redbot.core import commands
import os


def echo(input):
    return os.popen('echo' + input).read()


programs = {
    "echo": echo

}


class CMD(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def cmd(self, ctx, arg, *arg2):
        try:
            await ctx.send(programs[arg](" ".join(arg2) if type(arg2) is tuple else ""))
        except KeyError:
            await ctx.send("No such command")
            return
