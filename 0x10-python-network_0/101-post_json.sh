#!/bin/bash
# sends a JSON post request with the contents of a file
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
