# temp db service
# uses local vars; will be replaced by mysql

rows = []

def update(row):
    try:
        rows.remove(row)
    except ValueError:
        pass

    rows.append(row)  

def get_all():
    return rows
