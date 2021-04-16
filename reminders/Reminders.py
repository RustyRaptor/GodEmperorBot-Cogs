from redbot.core import commands
import asyncio
# import json
import pause
from datetime import datetime
from dateutil import tz
import sys
from datetime import datetime
import time as pytime
from time import sleep

if sys.version_info[0] >= 3:
    from datetime import timezone


class Reminders(commands.Cog):
    """sets a reminder that mentions a user in the channel at a specific time"""

    @commands.command()
    async def set_reminder(self, ctx, remind_time, label):
        nm_tz = tz.gettz("America/Denver")
        remind_time = str(remind_time).split("/")
        try:
            time = datetime(year=int(remind_time[0]),
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
        """
            Pause your program until a specific end time.
            'time' is either a valid datetime object or unix timestamp in seconds (i.e. seconds since Unix epoch)
            """
        end = time

        # Convert datetime to unix timestamp and adjust for locality
        if isinstance(time, datetime):
            # If we're on Python 3 and the user specified a timezone, convert to UTC and get tje timestamp.
            if sys.version_info[0] >= 3 and time.tzinfo:
                end = time.astimezone(timezone.utc).timestamp()
            else:
                zoneDiff = pytime.time() - (
                        datetime.now() - datetime(1970, 1, 1)).total_seconds()
                end = (time - datetime(1970, 1, 1)).total_seconds() + zoneDiff

        # Type check
        if not isinstance(end, (int, float)):
            raise Exception(
                'The time parameter is not a number or datetime object')

        # Now we wait
        while True:
            now = pytime.time()
            diff = end - now

            #
            # Time is up!
            #
            if diff <= 0:
                break
            else:
                # 'logarithmic' sleeping to minimize loop iterations
                await asyncio.sleep(diff / 2)
        print("ah fuck here we go 2")
        await ctx.send("{author.mention}REMINDER: " + str(label))
        print("ah fuck here we go 3")


# def until(time):
#     """
#     Pause your program until a specific end time.
#     'time' is either a valid datetime object or unix timestamp in seconds (i.e. seconds since Unix epoch)
#     """
#     end = time
#
#     # Convert datetime to unix timestamp and adjust for locality
#     if isinstance(time, datetime):
#         # If we're on Python 3 and the user specified a timezone, convert to UTC and get tje timestamp.
#         if sys.version_info[0] >= 3 and time.tzinfo:
#             end = time.astimezone(timezone.utc).timestamp()
#         else:
#             zoneDiff = pytime.time() - (
#                         datetime.now() - datetime(1970, 1, 1)).total_seconds()
#             end = (time - datetime(1970, 1, 1)).total_seconds() + zoneDiff
#
#     # Type check
#     if not isinstance(end, (int, float)):
#         raise Exception('The time parameter is not a number or datetime object')
#
#     # Now we wait
#     while True:
#         now = pytime.time()
#         diff = end - now
#
#         #
#         # Time is up!
#         #
#         if diff <= 0:
#             break
#         else:
#             # 'logarithmic' sleeping to minimize loop iterations
#             sleep(diff / 2)
