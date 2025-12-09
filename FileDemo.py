# Added First version of the copy
from datetime import datetime
from zoneinfo import ZoneInfo  # Available in Python 3.9+

# Use Europe/Amsterdam to get CET/CEST automatically depending on the date
tz = ZoneInfo("Europe/Amsterdam")
now = datetime.now(tz)

print("Hello Ram")
print(f"Time is now {now:%Y-%m-%d %H:%M:%S %Z}")


# Also print India time
india_tz = ZoneInfo("Asia/Kolkata")
india_now = datetime.now(india_tz)
print(f"Time in India is now {india_now:%Y-%m-%d %H:%M:%S %Z}")
