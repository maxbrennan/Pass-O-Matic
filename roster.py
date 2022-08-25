import circuitpython_csv as csv

lookup = {}

with open("roster.csv", mode="r", encoding="utf-8") as csvfile:
    csvreader = csv.DictReader(csvfile, fieldnames=("id", "name"))
    for student in csvreader:
        try:
            lookup[int(student["id"])] = student["name"]
        except:
            pass