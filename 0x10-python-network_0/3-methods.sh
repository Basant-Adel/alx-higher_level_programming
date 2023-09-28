#!/bin/bash
# Takes in a URL & displays all -> (HTTP)
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
