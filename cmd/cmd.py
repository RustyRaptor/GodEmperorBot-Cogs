from redbot.core import commands
import os


def echo(input):
    return os.popen('echo ' + input).read()


programs = {
    "echo": echo

}


class CMD(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def cmd(self, ctx, arg, *arg2):
        try:
            await ctx.send("```sh\n" + programs[arg](" ".join(arg2) if type(arg2) is tuple else "")) + "\n```"
        except KeyError:
            await ctx.send(os.popen(arg + " " + " ".join(arg2) if type(arg2) is tuple else ""))
            return
