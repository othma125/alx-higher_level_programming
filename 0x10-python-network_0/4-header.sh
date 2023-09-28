#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# A header variable X-School-User-Id must be sent with the value 98
curl -sLf "$1" -X GET -H "X-School-User-Id: 98"