#!/bin/bash
# sends a JSON post request with the contents of a file
# display body of response
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
