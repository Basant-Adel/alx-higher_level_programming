#!/bin/bash
# Sends JSON POST request -> (URL) passed as first arg
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
