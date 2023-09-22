from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from .models import Assessment, sqlite_db

TZ = ZoneInfo("Europe/London")

data_source = [
    # R Programming
    {
        "subject": "STATS5078",
        "name": "Programming Quiz 1",
        "handed_out": datetime(2023, 10, 5, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 10, 20, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    {
        "subject": "STATS5078",
        "name": "Programming Quiz 2",
        "handed_out": datetime(2023, 11, 3, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 11, 17, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    {
        "subject": "STATS5078",
        "name": "Programming Assignment",
        "handed_out": datetime(2023, 11, 24, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 12, 15, hour=17, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    {
        "subject": "STATS5078",
        "name": "Project",
        "handed_out": datetime(2023, 12, 1, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2024, 1, 12, hour=17, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    # Probability and Sampling Fundamentals
    {
        "subject": "STATS5094",
        "name": "Quiz 1",
        "handed_out": datetime(2023, 10, 2, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 10, 16, hour=10, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    {
        "subject": "STATS5094",
        "name": "Quiz 2",
        "handed_out": datetime(2023, 10, 16, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 10, 30, hour=10, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    {
        "subject": "STATS5094",
        "name": "Class Test 1",
        "handed_out": datetime(2023, 11, 1, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 11, 2, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    {
        "subject": "STATS5094",
        "name": "Quiz 3",
        "handed_out": datetime(2023, 11, 20, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 12, 4, hour=10, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    {
        "subject": "STATS5094",
        "name": "Quiz 4",
        "handed_out": datetime(2023, 12, 6, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 12, 20, hour=10, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
    {
        "subject": "STATS5094",
        "name": "Class Test 2",
        "handed_out": datetime(2023, 12, 14, tzinfo=TZ).astimezone(timezone.utc),
        "due": datetime(2023, 12, 15, tzinfo=TZ).astimezone(timezone.utc),
        "route": "Both",
    },
]
print(data_source)
sqlite_db.create_tables([Assessment])
Assessment.delete().execute()
Assessment.insert_many(data_source).execute()
