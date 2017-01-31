#!/usr/bin/env python3
#
# Client for the UINames.com service.

import requests


def SampleRecord():
    r = requests.get("http://uinames.com/api?ext&region=United%20States",
                     timeout=2.0)
    j = r.json()

    return "My name is {} {} and the PIN on my card is {}.".format(
        j["name"],
        j["surname"],
        j["credit_card"]["pin"]
    )

if __name__ == '__main__':
    print(SampleRecord())
