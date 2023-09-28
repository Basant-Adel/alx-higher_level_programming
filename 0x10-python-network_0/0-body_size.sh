#!/bin/bash
# Write a Bash script that takes in a URL
# sends a request to that URL, and displays size of body of response

curl -s "$1" | wc -c
