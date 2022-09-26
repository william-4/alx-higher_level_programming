#!/usr/bin/bash
# send a GET request to a URL and display response body
# -s-silet, -L- redo request in new redirected location, -f-fail silently(no output on server errors)
# -x-http method
curl -sfL "$1" -X GET
