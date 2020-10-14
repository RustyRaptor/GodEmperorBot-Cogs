from redbot.core import commands


def echo(input):
    return input


programs = {
    "echo": echo
}


class CMD(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def cmd(self, ctx, arg):
        try:
            await ctx.send(programs[arg])
        except KeyError:
            await ctx.send("No such command")
            return
