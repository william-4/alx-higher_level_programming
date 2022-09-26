#!/usr/bin/bash
# curl sends a GET request and displays body, send a header

curl -s -H "X-School-User-Id: 98" "$1"
