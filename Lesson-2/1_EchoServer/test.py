#!/usr/bin/env python3
#
# Test script for the echo server.

import requests, random

words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf",
         "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November",
         "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform",
         "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]

query = "".join(random.choice(words) for _ in range(3))
uri = "http://localhost:8000/" + query
print("Sending query for:", uri)
try:
  r = requests.get(uri)
  output = r.text.strip()
  if r.status_code != 200:
    print("The server returned status code {}"
          "instead of a 200 OK.".format(r.status_code))
  elif output == query:
    print("Looks good!")
  else:
    print("The server sent a 200 OK response, but it wasn't an echo.")
    print("I expected '{}', but the server said '{}'".format(query, output))
    if output == "Hello, HTTP!":
      print("That looks like the hello server talking.")
except requests.ConnectionError:
  print("Couldn't connect to the server. Is it running on port 8000?")
except requests.RequestException as e:
  print("Couldn't communicate with the server ({})".format(e))
  print("If it's running, take a look at the server's output.")

