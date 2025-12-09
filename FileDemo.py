
from datetime import datetime
from zoneinfo import ZoneInfo  # Available in Python 3.9+

# Time zones
tz_amsterdam = ZoneInfo("Europe/Amsterdam")
tz_india = ZoneInfo("Asia/Kolkata")

# Current times
now_amsterdam = datetime.now(tz_amsterdam)
now_india = datetime.now(tz_india)

print("Hello Ram")
print(f"Time in Amsterdam: {now_amsterdam:%Y-%m-%d %H:%M:%S %Z}")
print(f"Time in India:     {now_india:%Y-%m-%d %H:%M:%S %Z}")
