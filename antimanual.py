from wps import wps
from safe import safe
from shareit import shareit
from edlp import edlp
from scratch import scratch
from koto import koto
from whiteboard import whiteboard
from inshot import inshot
from esfile import esfile
# from settings import settings
import subprocess


subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'true'])

name = subprocess.run(['adb', 'devices'])

edlp()
print("")
esfile()
print("")
safe()
print("")
#
scratch()
print("")
whiteboard()
print("")
shareit()
print("")
wps()
print("")
koto()
print("")


inshot()
print("")


cmd = ['adb', 'shell', 'date']

# Run the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# Decode the output
output = output.decode().strip()

# Extract the time information
device_time = output.split(' ')[3]

print('Device time:', device_time)


# Construct the command
cmd = ['adb', 'get-serialno']

# Run the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# Decode the output
device_serial_number = output.decode().strip()

print('Device serial number:', device_serial_number)

#
#

#









# settings()

subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'false'])
