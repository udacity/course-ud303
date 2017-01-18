#!/usr/bin/env python3
#
# A quick & dirty URL shortener

import http.server
import requests
from urllib.parse import unquote, parse_qs

memory = {}

form = '''<!DOCTYPE html>
<title>Bookmark Server</title>
<form method="POST">
  <label>Long URI:
    <input name="long">
  </label>
  <br>
  <label>Short name:
    <input name="short">
  </label>
  <br>
  <button type="submit">Save it!</button>
</form>
<p>URIs I know about:
<pre>
{}
</pre>
'''

class Shortener(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    name = unquote(self.path[1:])

    if name:
      if name in memory:
        # We know that name! Send a redirect to it.
        self.send_response(303)
        self.send_header('Location', memory[name])
        self.end_headers()
      else:
        # We don't know that name! Send a 404 error.
        self.send_response(404)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("I don't know that name.".encode())
    else:
      # Root path. Send the form.
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      # List the known associations in the form.
      known = "\n".join("{} : {}".format(key, memory[key]) 
                        for key in sorted(memory.keys()))
      self.wfile.write(form.format(known).encode())

  def do_POST(self):
    # Decode the form data.
    length = int(self.headers.get('Content-length', 0))
    body = self.rfile.read(length).decode()
    params = parse_qs(body)
    long = params["long"][0]
    short = params["short"][0]

    # Check the URI.
    try:
      r = requests.get(long)
      success = r.status_code == 200
    except requests.RequestException:
      success = False

    if success:
      # Store the association.
      memory[short] = long

      # Serve a redirect to the form.
      self.send_response(303)
      self.send_header('Location', '/')
      self.end_headers()
    else:
      # Didn't successfully fetch the long URI.
      self.send_response(404)
      self.send_header('Content-type', 'text/plain; charset=utf-8')
      self.end_headers()
      self.wfile.write("Couldn't fetch {}. Sorry!".format(long).encode())

if __name__ == '__main__':
  server_address = ('', 8000)
  httpd = http.server.HTTPServer(server_address, Shortener)
  httpd.serve_forever()
