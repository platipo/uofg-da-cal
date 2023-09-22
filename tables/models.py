from peewee import (
    SQL,
    CharField,
    CompositeKey,
    DateField,
    DateTimeField,
    Field,
    ForeignKeyField,
    Model,
    SqliteDatabase,
)

sqlite_db = SqliteDatabase(
    "calendar.db",
    pragmas={
        "journal_mode": "wal",
        "foreign_keys": 1,
    },
)


class EnumField(Field):
    db_field = "enum"

    def pre_field_create(self, model):
        field = "e_%s" % self.name

        self.get_database().get_conn().cursor().execute(
            "DROP TYPE IF EXISTS %s;" % field
        )

        query = self.get_database().get_conn().cursor()

        tail = ", ".join(["'%s'"] * len(self.choices)) % tuple(self.choices)
        q = "CREATE TYPE %s AS ENUM (%s);" % (field, tail)
        query.execute(q)

    def post_field_create(self, model):
        self.db_field = "e_%s" % self.name

    def coerce(self, value):
        if value not in self.choices:
            raise Exception("Invalid Enum Value `%s`", value)
        return str(value)

    def get_column_type(self):
        return "enum"

    def __ddl_column__(self, ctype):
        return SQL("e_%s" % self.name)


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = sqlite_db


class Semester(BaseModel):
    start = DateField(unique=True)
    end = DateField()
    midterm = DateField()


class Subject(BaseModel):
    class_id = CharField(primary_key=True)
    name = CharField()
    moodle_page = CharField()


class Assessment(BaseModel):
    subject = ForeignKeyField(Subject, backref="exams")
    name = CharField()
    handed_out = DateTimeField()
    due = DateTimeField()
    route = EnumField(choices=["Normal", "Faster", "Both"])

    class Meta:
        primary_key = CompositeKey("subject", "name")


# class LiveSession(BaseModel):
#     subject = ForeignKeyField(Subject, backref="sessions")
#     day = DateField()
