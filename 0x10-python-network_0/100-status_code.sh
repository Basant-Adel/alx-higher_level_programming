#!/bin/bash
# Sends request -> (URL) passed as argument
curl -s -o /dev/null -w "%{http_code}" "$1"
