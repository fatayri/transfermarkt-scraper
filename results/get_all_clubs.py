import os
import json

if os.path.exists("all_clubs.json"):
    os.remove("all_clubs.json")

directories = [x.path for x in os.scandir('../results') if x.is_dir()]
players = [x + '/clubs.json' for x in directories]

all_hrefs = []
for file in players:
	with open(file) as f:
		print(file)
		for line in f:
			x = json.loads(line)
			all_hrefs.append(x)

with open('all_clubs.json', 'w') as f:
	for href in all_hrefs:
		f.write(f"{href}\n")

print(len(all_hrefs))

