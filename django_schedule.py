#!/usr/bin/env python
"""
This script to restart django-service every 4 am
Don't forget to change the user
"""

from crontab import CronTab
import sys
import subprocess


def restart_daily():
	myCron = CronTab(user='noel')

	job = myCron.new(command='sudo /home/noel/anaconda2/bin/python   /home/noel/project27/scheduler/cmd_line/django_service.py restart', comment='restart-django-service')
	job.minute.on(0)
	job.hour.on(4)

	myCron.write()

	for jb in myCron:
		print jb


def check_daily():
	myCron = CronTab(user='noel')

	job = myCron.new(command='sudo /home/noel/anaconda2/bin/python    /home/noel/project27/scheduler/cmd_line/django_check.py check', comment='check-django-service')
	job.minute.on(0)
	job.hour.on(5)

	myCron.write()	

	for jb in myCron:
		print jb


def clear_rule():
	cmd = 'crontab -r'
	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	result = output
	return result


def show_rule():
	cmd = 'crontab -l'
	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	result = output
	return result


def logs(command):
	if command == 'restart':
		cmd = 'sudo grep restart-django-service /var/log/syslog'
		process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		result = output
		return result
	elif command == 'check':
		cmd = 'sudo grep check-django-service /var/log/syslog'
		process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		result = output
		return result
	else:
		return "You should use restart and check"

	
# main program
arg = sys.argv[1]

if arg == "restart":
	arg = sys.argv[1]
	restart_daily()
elif arg == "check":
	check_daily()
elif arg == 'logs':
	arg2 = sys.argv[2]
	if arg2 == 'restart':
		print logs('restart')
	elif arg2 == 'check':
		print logs('check')
	else:
		print "You should use restart and check"
elif arg == 'clear':
	print clear_rule()
elif arg == 'rule':
	print show_rule()
else:
	print 'You should use "django-schedule.py restart, check, rule, clear and logs"'