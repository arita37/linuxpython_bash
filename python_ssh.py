from paramiko import client
import sys


class ssh:
	client = None

	def __init__(self, address, username, password, filename):
		# Let the user know we're connecting to the server
		print("Connecting to server.")
		# Create a new SSH Client
		self.client = client.SSHClient()
		# The following line is required if you want the script to be able to access a server that's not yet in the knows_hosts file
		self.client.set_missing_host_key_policy(client.AutoAddPolicy())
		# Make the connection
		self.client.connect(address, username=username, password=password, key_filename=filename)

   	def sendCommand(self, command):
   		if(self.client):
   			stdin, stdout, stderr = self.client.exec_command(command)
   			while not stdout.channel.exit_status_ready():
   				# Print data when available
   				if stdout.channel.recv_ready():
   					alldata = stdout.channel.recv(1024)
   					prevdata = b"1"
   					while prevdata:
   						prevdata = stdout.channel.recv(1024)
   						alldata += prevdata

   					print(str(alldata))
   		else:
   			print('Connection not opened.')


arg = []

for i in range(len(sys.argv)):
	if i == 0:
		continue
	else:
		arg.append(sys.argv[i])

result = ' '.join(arg)
# print result

# change the ssh configuration as you wish
connection = ssh("127.0.0.1", "handry", "vangke", 'id_rsa')
connection.sendCommand(result)