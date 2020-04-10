"""
$ pip install requests
"""
from concurrent.futures import ThreadPoolExecutor
import requests, json
import os
try:
    os.remove("movies.json")
except:
    pass

# call page 1 to access the number of pages
total_number_of_pages = requests.get("https://vidsrc.me/movies/latest/page-1.json").json()["pages"]

movies_list = []
for i in range(1, 100):
    movies = requests.get("https://vidsrc.me/movies/latest/page-"+str(i)+".json").json()["result"]
    for j in movies:
        if j["quality"] == "DVD" and "2020" in j["title"]:
            movies_list.append(j)
            print(j)
            break

# print(json.dumps(movies_list, indent=4))
with open("movies.json", "w") as f:
    json.dump(movies_list, f, indent=4, sort_keys=True)
