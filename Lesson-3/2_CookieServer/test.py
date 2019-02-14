#!/usr/bin/env python3
#
# Test script for the Cookie server.
#
# The server should be listening on port 8000, answer a GET request with
# an HTML document, answer a POST request by setting a cookie and issuing
# a redirect.

import requests, random, socket

def test_connect():
    '''Try connecting to the server.'''
    print("Testing connecting to the server.")
    try:
        with socket.socket() as s:
           s.connect(("localhost", 8000))
        print("Connection attempt succeeded.")
        return None
    except socket.error:
        return "Server didn't answer on localhost port 8000.  Is it running?"

def test_POST_cookie():
    '''The server should accept a POST and return a 303 to / with a cookie.'''
    print("Testing POST request, looking for redirect & cookie.")

    name = random.choice(["Alice", "Bob", "Charlie", "Debra"])
    uri = "http://localhost:8000/"
    try:
        r = requests.post(uri, data = {'yourname': name}, allow_redirects=False)
    except requests.RequestException as e:
        return ("Couldn't communicate with the server. ({})\n"
                "If it's running, take a look at its output.").format(e)
    if r.status_code == 501:
        return ("The server returned status code 501 Not Implemented.\n"
                "This means it doesn't know how to handle a POST request.\n"
                "(Is the correct server code running?)")
    elif r.status_code != 303:
        return ("The server returned status code {} instead of a 303 redirect."
                ).format(r.status_code)
    elif 'location' not in r.headers:
        return ("Server returned a 303 redirect with no Location header.")
    elif r.headers['location'] != '/':
        return ("The server sent a 303 redirect to the wrong location."
                "I expected '/' but it sent '{}'.").format(
                    r.headers['location'])
    elif 'set-cookie' not in r.headers:
        return ("Server returned a 303 redirect without a cookie.")
    else:
        print("POST request succeeded and issued a cookie.")
        return None

def test_GET_plain():
    '''The server should accept a GET and return the form.'''
    print("Testing GET request.")
    uri = "http://localhost:8000/"
    try:
        r = requests.get(uri)
    except requests.RequestException as e:
        return ("Couldn't communicate with the server. ({})\n"
                "If it's running, take a look at its output.").format(e)
    if r.status_code == 501:
        return ("The server returned status code 501 Not Implemented.\n"
                "This means it doesn't know how to handle a GET request.\n"
                "(Is the correct server code running?)")
    elif r.status_code != 200:
        return ("The server returned status code {} instead of a 200 OK."
                ).format(r.status_code)
    elif not r.headers['content-type'].lower().startswith('text/html'):
        return ("The server didn't return Content-type: text/html.")
    elif '<title>I Remember You</title>' not in r.text:
        return ("The server didn't return the form text I expected.")
    else:
        print("GET request without cookie succeeded!")
        return None


def test_GET_cookie():
    '''The server should accept a GET with a cookie on and return the name.'''
    print("Testing GET request with cookie.")
    uri = "http://localhost:8000/"
    name = random.choice(["Alice", "Bob", "Carla", "David"])
    jar = requests.cookies.RequestsCookieJar()
    jar.set('yourname', name)
    try:
        r = requests.get(uri, cookies=jar)
    except requests.RequestException as e:
        return ("Couldn't communicate with the server. ({})\n"
                "If it's running, take a look at its output.").format(e)
    if r.status_code == 501:
        return ("The server returned status code 501 Not Implemented.\n"
                "This means it doesn't know how to handle a GET request.\n"
                "(Is the correct server code running?)")
    elif r.status_code != 200:
        return ("The server returned status code {} instead of a 200 OK."
                ).format(r.status_code)
    elif not r.headers['content-type'].lower().startswith('text/html'):
        return ("The server didn't return Content-type: text/html.")
    elif name not in r.text:
        return ("The server didn't display the name from the cookie.")
    else:
        print("GET request with cookie succeeded!")
        return None
     

if __name__ == '__main__':
    tests = [test_connect, test_GET_plain, test_POST_cookie, test_GET_cookie]
    for test in tests:
        problem = test()
        if problem is not None:
            print(problem)
            break
    if not problem:
        print("All tests succeeded!")
