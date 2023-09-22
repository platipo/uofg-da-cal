from .models import Subject, sqlite_db

data_source = [
    {
        "class_id": "STATS5077",
        "name": "Probability and Stochastic Models",
        "moodle_page": "https://moodle.gla.ac.uk/course/view.php?id=38878",
    },
    {
        "class_id": "STATS5094",
        "name": "Probability and Sampling Fundamentals",
        "moodle_page": "https://moodle.gla.ac.uk/course/view.php?id=38890",
    },
    {
        "class_id": "STATS5078",
        "name": "R Programming",
        "moodle_page": "https://moodle.gla.ac.uk/course/view.php?id=38896",
    },
    {
        "class_id": "STATS5082",
        "name": "Data Programming in Python",
        "moodle_page": "https://moodle.gla.ac.uk/course/view.php?id=38885",
    },
]

sqlite_db.create_tables([Subject])
Subject.insert_many(data_source).execute()
