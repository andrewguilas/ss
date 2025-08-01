from datetime import datetime

def format_date_short(d):
    try:
        return d.strftime("%a %-m/%-d")
    except ValueError:
        return d.strftime("%a %#m/%#d")

def parse_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None
