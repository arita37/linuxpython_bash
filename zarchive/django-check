#!/usr/bin/env python
"""
This script for check there is an error of django application at 5 Am, 
if an error backup the django application to the /tmp
"""
import subprocess
import sys
from datetime import datetime

date = datetime.now()
year = str(date.year)
month = str(date.month)
day = str(date.day)
hour = str(date.hour)
minute = str(date.minute)
second  = str(date.second)
port = "80/tcp"

def check():
	command = 'fuser '+ port
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	result = output.strip()

	return result


def backup():
	command = 'tar -zcvf /tmp/backup_' + year + month + day + hour + minute + second + '.tar.gz -P /home/noel/project27/'
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	result = 'Backup the django application'

	return result


if check() == "":
	print "Django service not running!"
	print backup()
else:
	print "Django service already running with PID number",check()
