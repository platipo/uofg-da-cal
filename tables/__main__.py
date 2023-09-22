import json
from datetime import timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from colorhash import ColorHash
from jinja2 import Template

from .models import Assessment, Semester

_ROOT_DIR = Path(__file__).parent.parent
_TEMPLATE_DIR = _ROOT_DIR / "templates"
TEMPLATE_MAPPING = {
    Semester: _TEMPLATE_DIR / "semesters.jinja2",
    Assessment: _TEMPLATE_DIR / "assessments.jinja2",
}
TZ = ZoneInfo("Europe/London")


def main():
    event_dir = _ROOT_DIR / "events"

    for table, template_path in TEMPLATE_MAPPING.items():
        event_path = event_dir / f"{template_path.stem}.json"
        template = Template(template_path.read_text())
        print(list(table.select().dicts().execute()))
        event_data = template.render(
            {
                "arg": list(table.select().execute()),
                "timedelta": timedelta,
                "colorhash": ColorHash,
                "tzinfo": TZ,
            }
        )
        try:
            json_valid_data = json.dumps(json.loads(event_data))
        except json.decoder.JSONDecodeError:
            print(event_data)
            raise
        print(json_valid_data)
        event_path.write_text(json_valid_data)


if __name__ == "__main__":
    main()
    #
