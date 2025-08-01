def format_date_short(d):
    try:
        return d.strftime("%a %-m/%-d")
    except ValueError:
        return d.strftime("%a %#m/%#d")
