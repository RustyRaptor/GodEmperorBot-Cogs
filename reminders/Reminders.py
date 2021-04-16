from redbot.core import commands
# import json
import pause
from datetime import datetime
from dateutil import tz


class Reminders(commands.Cog):
    """sets a reminder that mentions a user in the channel at a specific time"""

    @commands.command()
    async def set_reminder(self, ctx, remind_time, label):
        nm_tz = tz.gettz("America/Denver")
        remind_time = str(remind_time).split("/")
        try:
            dt = datetime(year=int(remind_time[0]),
                          month=int(remind_time[1]),
                          day=int(remind_time[2]),
                          hour=int(remind_time[3]), minute=int(remind_time[4]),
                          tzinfo=nm_tz)
        except IndexError:
            ctx.send(
                "{author.mention} please enter remind time as "
                "year/month/day/hour/minute")
            return
        print("ah fuck here we go")
        pause.until(dt)
        print("ah fuck here we go 2")
        ctx.send("{author.mention}REMINDER: " + str(label))
        print("ah fuck here we go 3")