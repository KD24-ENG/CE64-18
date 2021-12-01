import json
import csv

with open("1_Lat Phrao.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"1_Lat Phrao": []}
    for row in reader:
        data["1_Lat Phrao"].append({"RD_ID": row[0], "Junction_ID": row[1], "lat": row[2], "long": row[3], "Alley": row[4]})

with open("1_Lat Phrao.json", "w") as f:
    json.dump(data, f, indent=4)