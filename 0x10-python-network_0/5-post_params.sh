#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sLf "$1" -X POST -d "
