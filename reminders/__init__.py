from .Reminders import Reminders


def setup(bot):
    bot.add_cog(Reminders())
