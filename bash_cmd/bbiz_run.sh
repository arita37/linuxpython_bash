#!/bin/bash
# This script to running django application, 
# But change the variable to corresponding environment

ip="0.0.0.0:80"
commandEx="/home/noel/project27/geoapp/geoproject/manage.py runserver "
pythonEnv="COMPRESS=5 /home/noel/anaconda2/bin/python "

$pythonEnv $commandEx $ip


