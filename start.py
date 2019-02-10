import subprocess
import shutil
import time
import os
import json
import media_entry

usernames = ["luke.janik", "aaronpradhan1", "mileycyrus"]
process = ["instagram-scraper"]
process.extend(usernames)
process.extend(["-u", "user", "-p", "pass", "--include-location", "-m", "1", "-d", "jsons"])

# get the json files for insta images
subprocess.run(process)
# get the jsons into one folder
json_dir = ""
for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		if 'jsons' in root and ('jpg' in name or 'mp4' in name):
			json_dir = root
			os.remove(os.path.join(root, name))

media_list = media_entry.get_all_media(json_dir)
print(media_list)