#!/usr/bin/env python3
#
# Step two in building the messageboard server.
# 
# Instructions:
#   1. In the do_POST method, send a 303 redirect back to the / page.
#   2. In the do_GET method, put the response together and send it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # Extract the "message" field from the request data.
        message = parse_qs(data)["message"][0]

        # Escape HTML tags in the message so users can't break world+dog.
        message = message.replace("<", "&lt;")

        # Store it in memory.
        memory.append(message)

        # 1. Send a 303 redirect back to the root page.

    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # 2. Put the response together out of the form and the stored messages.

        # 3. Send the response.

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
