#!/usr/bin/python3
"""
A script that takes a URL, sends a request and displays
the value of the x-Request-Id variable in the header
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
