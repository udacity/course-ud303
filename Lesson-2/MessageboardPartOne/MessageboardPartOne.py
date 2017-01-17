#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
# 
# You'll need to add two things to the do_POST method to make it work:
# first, it'll need to find the length of the request data; then read the
# request data, then extract the "message" field into a variable.
#
# When you're done, run this server and test it from your browser using
# the MessageboardPartOne.html form.  Then run the test.py script to
# validate it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message?
        # (Use the Content-Length header.)
        
        # 2. Read the correct amount of data from the request.
        
        # 3. Extract the "message" field from the request data.
        
        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
