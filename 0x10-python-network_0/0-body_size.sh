#!/bin/bash
# Write a Bash script that takes in -> (URL)
curl -s "$1" | wc -c
