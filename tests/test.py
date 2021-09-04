#!/usr/bin/env python

import requests, json

BASE = "http://127.0.0.1:8000/"

data = [
    {"name": "USS Enterprise", "class": "Sovereign-class", "owner": "United Federation of Planets", "operator": "Starfleet", "status": "Active"},
    {"name": "USS Defiant",    "class": "Defiant-class",   "owner": "United Federation of Planets", "operator": "Starfleet", "status": "Active"},
    {"name": "USS Voyager",    "class": "Intrepid-class",  "owner": "United Federation of Planets", "operator": "Starfleet", "status": "Active"}
]

print("=== Inserting ships ==")

response = requests.post(BASE + "ship/" + "NCC-1701-E", data[0])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NX-74205", data[1])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-74656", data[2])
print(json.dumps(response.json(), indent=2))

print("=== Updating ships ==")

data[1] = {"name": "USS Defiant", "class": "Defiant-class", "owner": "United Federation of Planets", "operator": "Starfleet", "status": "Destroyed"}

response = requests.put(BASE + "ship/" + "NCC-74656", data[1])
print(json.dumps(response.json(), indent=2))

print("=== Deleting ships ===")

response = requests.delete(BASE + "ship/" + "NX-74205")
print(response)

print("=== Recovering a ship ===")

response = requests.get(BASE + "ship/" + "NCC-74656")
print(json.dumps(response.json(), indent=2))

print("=== Recovering all ships ===")

response = requests.get(BASE + "ships")
print(json.dumps(response.json(), indent=2))