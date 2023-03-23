import subprocess

def time():

    cmd = ['adb', 'shell', 'date']

    # Run the command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Decode the output
    output = output.decode().strip()

    # Extract the time information
    device_time = output.split(' ')[3]

    print('Device time:', device_time)


time()
