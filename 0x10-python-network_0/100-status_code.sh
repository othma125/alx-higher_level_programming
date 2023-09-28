#!/bin/bash
# Script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl -sLf "$1" -X GET -w "%{http_code}"
