from datetime import date

from .models import Semester, sqlite_db

data_source = [
    {
        "id": 1,
        "start": date(2023, 9, 18),
        "end": date(2023, 12, 2),
        "midterm": date(2023, 10, 23),
    },
    {
        "id": 2,
        "start": date(2024, 1, 8),
        "end": date(2024, 3, 29),
        "midterm": date(2024, 2, 12),
    },
    {
        "id": 3,
        "start": date(2024, 4, 29),
        "end": date(2024, 7, 12),
        "midterm": date(2024, 6, 3),
    },
]

sqlite_db.create_tables([Semester])
Semester.insert_many(data_source).execute()
