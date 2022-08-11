import datetime

# This code below is from the python documentation for
# tzinfo: https://docs.python.org/2.3/lib/datetime-tzinfo.html

ZERO = datetime.timedelta(0)
HOUR = datetime.timedelta(hours=1)


class UTC(datetime.tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO

   


