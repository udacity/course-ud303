# Echo server

In this exercise, you'll take the code from the *hello server* and change
it into the *echo server*.  This new server will also listen on port 8000,
but it will respond to GET requests by repeating back ("echoing") the text
of the request path.

See `EchoServer.py` for starter code.

To test your code, you'll need two terminals open.  In one of them, run the
server (with `python EchoServer.py`).  You can then access it from your
browser, for instance at http://localhost:8000/GoodMorningHTTP.  In the
other terminal, run the test script provided (`python test.py`).  The test
script will send a request to the server and tell you whether it worked.

