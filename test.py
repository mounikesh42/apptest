import subprocess

# Define the shell command to retrieve the device's current date and time with timezone offset
cmd = ['adb', 'shell', 'date "+%Y-%m-%d %H:%M:%S %z"']

# Run the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# Decode the output
output = output.decode().strip()

# Extract the time and timezone offset information
device_time, timezone_offset = output.split(' ')[1:3]

# Print the device time and timezone offset
print('Device time:', device_time)
print('Timezone offset:', timezone_offset)

# Check if the timezone offset is GMT+4:00 (Mauritius Time)
if timezone_offset == '+0400':
    print('Device timezone is Mauritius Time ')
else:
    print('Device timezone is not set to Mauritius Time ')
