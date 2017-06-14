import sys
import os
import subprocess

fileName = sys.argv[1]

def readPpk(filename):
	command = 'puttygen -L '+ filename
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	result = output.strip()

	return result


def toRSA(publicKey, filename):
	target = open(filename, 'w')
	target.write(publicKey)
	target.close()


publicKey = readPpk(fileName)
toRSA(publicKey, 'id_rsa')
with open('id_rsa') as file:
	for fl in file:
		print fl

