import csv

d = {}

with open("./data.csv", "r+") as datafile:
  cols = datafile.readline().strip().split(",")
  for col in cols:
    d[col] = list()

l = list()

with open("./data.csv", "r+") as datafile:
  dictReader = csv.DictReader(datafile, fieldnames = list(d.keys()), delimiter = ',', quotechar = '"')
  for row in dictReader:
    l.append(d.copy())
    for key in row:
      l[len(l) - 1][key] = row[key]

print(l)
