#!/bin/bash
# This script to running django application, 
# But change the variable to corresponding environment

# Development
# ip="0.0.0.0:8080"
# commandEx="/home/handry/Documents/belajarPython/webIKP/website/manage.py runserver"
# pythonEnv="/home/handry/Documents/belajarPython/webIKP/env/bin/python3.5"


# Production
ip="0.0.0.0:80"
commandEx="/home/noel/project27/geoapp/geoproject/manage.py runserver"
pythonEnv="/home/noel/anaconda2/bin/python"

$pythonEnv $commandEx $ip


