from datetime import datetime, timezone, timedelta
tz = timezone(timedelta(hours=6))
now = datetime.now(tz)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

