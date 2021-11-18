import csv
import json


def can_be_a_int(s: str) -> bool:
    try:
        int(s)
        return True
    except:
        return False


def is_valid_year(y: str) -> bool:
    return all([
        y.isascii(),
        y.isdigit(),
        y.isdecimal(),
        y.isnumeric(),
        can_be_a_int(y)
    ])


def is_valid_rank(r: str) -> bool:
    return all([
        r.isascii(),
        r.isdigit(),
        r.isdecimal(),
        r.isnumeric(),
        can_be_a_int(r)
    ])


def can_be_a_float(x: str) -> bool:
    try:
        float(x)
        return True
    except:
        print("Not a float")
        return False


def is_valid_sales(s: str) -> bool:
    return all([
        s.isascii(),
        s.replace('.', '', 1).isdigit(),
        can_be_a_float(s)
    ])


invalids = list()
def is_valid_row(row: dict) -> bool:
    if not is_valid_year(row["year"]):
        invalids.append(dict(['reason', f"invalid year of {row['year']}", ['entry', row]))
        return False
    if not is_valid_rank(row["rank"]):
        invalids.append(dict(['reason', f"invalid rank of {row['rank']}", ['entry', row]))
        return False
    if not all(map(is_valid_sales, map(lambda k: row[k], ['na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales']))):
        invalids.append(dict(['reason', f"invalid sales value", ['entry', row]))
        return False

    return True


def cleanup_data(l: list) -> list:
    return list(
        filter(is_valid_row, l)
    )


def parse_row(row: dict) -> dict:
    out = dict([
        ['name', row['name']],
        ['publisher', row['publisher']],
        ['genre', row['genre']],
        ['platform', row['platform']],
        ['rank', int(row['rank'])],
        ['year', int(row['year'])],
        ['eu_sales', float(row['eu_sales'])],
        ['global_sales', float(row['global_sales'])],
        ['na_sales', float(row['na_sales'])],
        ['other_sales', float(row['other_sales'])],
        ['jp_sales', float(row['jp_sales'])],
    ])
    return out


def parse_data(dataset: list) -> list:
    return list(map(parse_row, dataset))


def jsonify(dataset: list) -> str:
    return json.dumps(
        dataset,
        ensure_ascii=True,
        check_circular=True,
        allow_nan=False,
        sort_keys=True,
        indent=None
    )



l = list()
with open("./dataset.csv", "r+") as datafile:
    dictReader = csv.DictReader(
        datafile,
        delimiter=',',
        quotechar='"',
    )
    for row in dictReader:
        l.append(d.copy())
        for key in row:
            l[len(l) - 1][key] = row[key]


data_json = jsonify(parse_data(cleanup_data(l)))

with open("./clean-dataset.json", "w+") as output:
    output.write(data_json)

with open("./invalids.json", "w+") as output:
    output.write(jsonify(invalids))
