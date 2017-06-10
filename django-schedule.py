#!/usr/bin/env python
"""
This script to restart django-service every 4 am
Don't forget to change the user
"""

from crontab import CronTab
import sys

def restart_daily():
	myCron = CronTab(user='handry')

	job = myCron.new(command='systemctl restart djangorun.service', comment='restart-django-service')
	job.hour.on(4)

	myCron.write()

	for jb in myCron:
		print jb


def check_daily():
	myCron = CronTab(user='handry')

	job = myCron.new(command='django-check', comment='restart-django-service')
	job.hour.on(5)
	# job.minute.every(1)

	myCron.write()	

	for jb in myCron:
		print jb


# main program
arg = sys.argv[1]
if arg == "restart":
	restart_daily()
elif arg == "check":
	check_daily()
else:
	print 'You should use "django-schedule restart or check"'



