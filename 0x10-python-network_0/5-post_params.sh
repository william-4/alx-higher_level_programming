#!/bin/bash
# curl sends a POST request and display response body
# send data with the request using -d option
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
