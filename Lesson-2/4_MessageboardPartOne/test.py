#!/usr/bin/env python3
#
# Test script for the Messageboard Part One server.

import requests, random

words = ["Angel", "Buffy", "Cordelia", "Dawn", "Ethan", "Faith", "Glory",
         "Harmony", "Jenny", "Kendra", "Liam", "Maggie", "Nikki", "Oz",
         "Parker", "Rupert", "Spike", "Tara", "Wesley", "Xander"]

random.shuffle(words)
mesg = "{} says hello to {}!".format(words[0], words[1])

try:
  uri = "http://localhost:8000/"
  print("Sending POST request to:", uri)
  print("message:", mesg)
  r = requests.post(uri, data = {"message": mesg})
  if r.status_code == 501:
    print("The server returned status code 501 Not Implemented.")
    print("This means it doesn't know how to handle a POST request.")
    print("(Is the right server code running?)")
  elif r.status_code != 200:
    print("The server returned status code {}"
          " instead of a 200 OK.".format(r.status_code))
  elif r.text == mesg:
    print("Looks good!")
  else:
    print("The server sent a 200 OK response, but the content differed.")
    print("I expected '{}', but the server sent '{}'.".format(mesg, r.text))
except requests.ConnectionError:
  print("Couldn't connect to the server. Is it running on port 8000?")
except requests.RequestError:
  print("Couldn't communicate with the server ({})".format(e))
  print("If it's running, take a look at the server's output.")

