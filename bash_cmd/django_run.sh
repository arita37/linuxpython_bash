#!/bin/bash
# This script to running django application, 
# But change the variable to corresponding environment

# Development
# ip="0.0.0.0:8080"
# commandEx="/home/handry/Documents/belajarPython/webIKP/website/manage.py runserver"
# pythonEnv="/home/handry/Documents/belajarPython/webIKP/env/bin/python3.5"


# Production
ip="0.0.0.0:80"
<<<<<<< HEAD:django_run.sh
commandEx="/home/noel/project27/geoapp/geoproject/manage.py runserver"
pythonEnv="/home/noel/anaconda2/bin/python"
=======
commandEx="/home/noel/project27/geoapp/geoproject/manage.py runserver "
pythonEnv="COMPRESS=5 /home/noel/anaconda2/bin/python "
>>>>>>> 2b7dfd5663e435cc4d8af0ef0a38328b470a8856:bash_cmd/django_run.sh

$pythonEnv $commandEx $ip


