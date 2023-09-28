#!/bin/bash
# Ttakes in a URL as an arg, sends GET request -> (URL)
curl -sH "X-School-User-Id: 98" "$1"
