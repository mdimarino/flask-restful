#!/usr/bin/env python

import requests

BASE = "http://127.0.0.1:8000/"

data = [
    {"name": "USS Enterprise", "class": "Sovereign-class", "owner": "United Federation of Planets", "operator": "Starfleet", "status": "Active"},
    {"name": "USS Defiant",    "class": "Defiant-class",   "owner": "United Federation of Planets", "operator": "Starfleet", "status": "Destroyed"},
    {"name": "USS Voyager",    "class": "Intrepid-class",  "owner": "United Federation of Planets", "operator": "Starfleet", "status": "Active"}
]

print("=== Inserting ships ==")

response = requests.put(BASE + "ship/" + 'NCC-1701-E', data[0])
print(response.json())

response = requests.put(BASE + "ship/" + 'NX-74205', data[1])
print(response.json())

response = requests.put(BASE + "ship/" + 'NCC-74656', data[2])
print(response.json())


print("=== Deleting ships ===")

response = requests.delete(BASE + "ship/NX-74205")
print(response)


print("=== Recovering ships ===")

response = requests.get(BASE + "ship/NCC-74656")
print(response.json())
