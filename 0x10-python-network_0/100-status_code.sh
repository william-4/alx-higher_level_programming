#!/bin/bash
# send a request to URL and display response status code only
curl -s -o /dev/null -w "%{http_code}" "$1"
