# You need to create resultdata.json before running

# OVERPASS COMMAND
# [out:json][timeout:600];
# area["ISO3166-1"="BY"][admin_level=2]->.pt;

# way
#   ["railway"="rail"]
#   ["maxspeed"]
#   (area.pt);
  
# out body;
# >;
# out skel qt;

import json, statistics

filelink = "C:\\Users\\YOUR USER\\Downloads\\export.json"
outfile = "C:\\Users\\YOUR USER\\Downloads\\resultdata.json"

# Read the file
print("Loading Data...")

with open(filelink, "r", encoding="utf-8") as f:
    rawdata = f.read()

print("Converting to JSON...")
jsondata = json.loads(rawdata)["elements"]
totalentries = len(jsondata)
print(f'{totalentries} entries loaded. Starting...')

# Work with the data
resultdata = {}
keys = []
completed = 0
for item in jsondata:
    completed += 1

    if item["type"] != "node" and "tags" in item:
        speed = item["tags"].get("maxspeed")
        if not speed:
            continue

        electrified = item["tags"].get("electrified", "unknown")
        if "contact_line" in electrified:
            electrified = "contact_line"

        if electrified in ["planned", "proposed", "construction", "<unterschiedlich>"]:
            continue

        if completed % 10000 == 0:
            print(f'{completed / totalentries * 100:.2f}% vollständig')

        if electrified not in resultdata:
            resultdata[electrified] = []
            keys.append(electrified)

        try:
            speed_val = int(speed.split()[0].replace(" mph", "")) * 1.609
            resultdata[electrified].append(speed_val)
        except:
            continue

# Prepare data for archiving
print("Preparing Data...")

final_stats = {}
all_speeds = []

for key in keys:
    speeds = resultdata[key]
    avg = sum(speeds) / len(speeds)
    med = statistics.median(speeds)
    all_speeds.extend(speeds)
    final_stats[key] = {
        "average": round(avg, 2),
        "median": med
    }

# Total
total_avg = sum(all_speeds) / len(all_speeds)
total_median = statistics.median(all_speeds)
final_stats["total"] = {
    "average": round(total_avg, 2),
    "median": total_median
}

# Write data
print("Writing Data...")
with open(outfile, "w", encoding="utf-8") as f:
    json.dump(final_stats, f, indent=4)

print("Done!")
