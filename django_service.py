#!/usr/bin/env python
"""
This script to manage django service like run, restart, stop, start, enable, disable service.
exp : django-service run to running django service.

django_service

"""

# import subprocess
# import sys

# def run():
# 	command = 'systemctl start djangorun.service'
# 	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()
# 	result = "Django service running"

# 	return result

# def stop():
# 	command = 'systemctl stop djangorun.service'
# 	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()
# 	result = "Django service stopped"

# 	return result


# def restart():
# 	command = 'systemctl restart djangorun.service'
# 	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()
# 	result = "Django service restarting"

# 	return result


# def start():
# 	command = 'systemctl start djangorun.service'
# 	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()
# 	result = "Django service starting"

# 	return result


# def disable():
# 	command = 'systemctl disable djangorun.service'
# 	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()
# 	result = "Django service disabled"

# 	return result


# def enable():
# 	command = 'systemctl enable djangorun.service'
# 	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()
# 	result = "Django service enabled"

# 	return result	


# def status():
# 	command = 'systemctl status djangorun.service'
# 	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()
# 	# result = "Django service enabled"

# 	return output


# # main program
# arg = sys.argv[1]

# if arg == 'run':
# 	print run()
# elif arg == 'stop':
# 	print stop()
# elif arg == 'restart':
# 	print restart()
# elif arg == 'start':
# 	print start()
# elif arg == 'enable':
# 	print enable()
# elif arg == 'disable':
# 	print disable()
# elif arg == 'status':
# 	print status()
# else:
# 	print 'Your command should be run, stop, restart, start, enable, disable or status'



# def getPID():
# 	command = 'fuser 8000/tcp'
# 	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# 	output, error = process.communicate()
# 	result = output.split(' ')
# 	servicePID = result[-1]

# 	return servicePID


# def killPID(pid):
# 	commandKill = 'kill ' + pid
# 	processKill = subprocess.Popen(commandKill.split(), stdout=subprocess.PIPE)
# 	output, error = processKill.communicate()
# 	result = 'Django service killed successfully'

# 	return result

# if getPID() == '':
# 	msg = 'Django service not running'
# 	print msg
# 	quit()
# else:
# 	print killPID(getPID())


import subprocess
import sys
import os

def run():
	command = 'sudo /home/noel/project27/scheduler/cmd_line/bash_cmd/django_run.sh'
	os.system(command)


def getPID():
	command = 'sudo netstat -nlp | grep :80'
	# os.system(command)
	output = subprocess.check_output(command, shell=True)
	result = output.split()
	result = result[-1]
	result = result.split('/')
	return result[0]


def stop(pid):
	command = 'sudo kill -9 ' + pid
	os.system(command)
	result = 'Django application stopped'

	return result


def restart(pid):
	stop(pid)
	run()


# main program
if sys.argv[1] == 'start':
	run()
elif sys.argv[1] == 'stop':
	pid = getPID()
	pid = str(pid)
	stop(pid)
elif sys.argv[1] == 'restart':
	pid = getPID()
	print stop(pid)
	run()
elif sys.argv[1] == 'pid':
	getPID()
else:
	print 'You should use start, stop, restart'
