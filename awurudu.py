import random
import requests
import sys

no_of_votes = int(sys.argv[1])
names = []
f = open("names.txt", "r")
for x in f:
    names.append(x.rstrip())
f.close()

req_str = "https://awrudu.backend.rotaractmora.org/games/contestantVote?cid=5ea7003250f214044ea18f0c&uid={user}@gmail.com&game=awruduKumariya"

for y in range (no_of_votes):
    us = names[random.randint(0,len(names)-1)]
    url_string = req_str.format(user = us)
    r = requests.get(url=url_string)
    print(r.text)