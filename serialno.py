import subprocess

def serialno():

    cmd = ['adb', 'get-serialno']

    # Run the command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Decode the output
    device_serial_number = output.decode().strip()

    print('Device serial number:', device_serial_number)
