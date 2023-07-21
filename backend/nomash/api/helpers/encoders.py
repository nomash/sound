from datetime import datetime
from pytz import utc


def convert_datetime_to_iso_8601_with_z_suffix(dt: datetime) -> str:
    format = '%Y-%m-%dT%H:%M:%SZ'
    if dt.tzinfo is None:
        return dt.strftime(format)
    else:
        return dt.astimezone(utc).strftime(format)
