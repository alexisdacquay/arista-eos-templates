#/bin/python

https://www.team-cymru.org/Services/Bogons/fullbogons-ipv4.txt
https://www.team-cymru.org/Services/Bogons/fullbogons-ipv6.txt

#$ pipenv install requests
import requests

r = requests.get(url)
r.text

with open(filename, 'r') as f:
    contents = f.readlines() #put the lines to a variable (list).
    print(contents)
