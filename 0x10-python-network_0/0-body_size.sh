#!/bin/bash
# ends a request to that URL displays the size of the response body
# I-header only, s-silent, i-ignore case distinctions, -d-use " " as delimiter, -f2-select field
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
