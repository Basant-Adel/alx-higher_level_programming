#!/bin/bash
# Sends a (DELETE) request -> (URL) passed as first argument
curl -sX DELETE "$1"
