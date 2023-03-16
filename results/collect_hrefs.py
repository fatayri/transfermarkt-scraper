import os 
import json 

os.remove("parsed_hrefs.txt")

directories = [x.path for x in os.scandir('../results') if x.is_dir()]
players = [x + '/players.json' for x in directories]

all_hrefs = []
for file in players:
	with open(file) as f:
		print(file)
		for line in f:
			x = json.loads(line)
			all_hrefs.append(x['href'])

with open('parsed_hrefs.txt', 'w') as f:
	for href in all_hrefs:
		f.write(f"{href}\n")

print(len(all_hrefs))

