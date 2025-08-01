def format_phone_number(number):
    s = str(number)

    # Remove country code if present
    if s.startswith("1") and len(s) == 11:
        s = s[1:]

    if len(s) != 10:
        raise ValueError("Phone number must have 10 digits after removing country code.")

    area_code = s[:3]
    prefix = s[3:6]
    line_number = s[6:]

    return f"({area_code}) {prefix}-{line_number}"
