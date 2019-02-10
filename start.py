import subprocess
import shutil
import time
import os
import json
import media_entry





# # list of instagram usernames to scrape from
# usernames = ["arianagrande","rihanavy","beyonce","city_of_newyork","travelers.inspiration","vancouverfoodie","dominqueansel",
# "magnoliabakery","sushiloveforever","pardonyourfrench","earthpix","loic.lagarde","beautifuldestinations","doyoutravel","_itsbeautifulhere",
# "taramilktea","hackbeanpot"]

usernames = ["rihanavy","magnoliabakery","sushiloveforever","earthpix"]

# putting together the process to call the instagram scraper with
process = ["instagram-scraper"]
process.extend(usernames)
process.extend(["-u", "user", "-p", "pass", "--include-location", "-m", "1", "-d", "jsons"])
# creates json files with instagram data
subprocess.run(process)

# cleans up folders
json_dir = ""
for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		if 'jsons' in root and ('jpg' in name or 'mp4' in name):
			json_dir = root
			os.remove(os.path.join(root, name))

# combines media from json files
media_list = media_entry.get_all_media(json_dir)

# combined media into a single list
print(media_list)