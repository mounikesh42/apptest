import subprocess

# path to the new Erudex folder on your local machine
new_folder_path = 'Erudex'

# path to the existing Erudex folder on your phone
phone_folder_path = '/storage/emulated/0/'

# construct the adb push command
cmd = ['adb', 'push', new_folder_path, phone_folder_path]

# execute the adb push command using subprocess
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# check if the device is connected for the first time
first_connection = True
while first_connection:
    # check if the process has output on stderr indicating that the device is requesting debug permissions
    stderr_output = process.stderr.readline().decode().strip()
    if 'Allow USB debugging' in stderr_output:
        print('Please grant debug permissions on your phone and press ENTER to continue...')
        input()
        # send the 'ENTER' key to the process to continue the execution
        process.stdin.write('\n'.encode())
        process.stdin.flush()
    elif not stderr_output and process.poll() is not None:
        # process has completed, check for errors on stdout
        stdout_output = process.stdout.read().decode().strip()
        if 'error' in stdout_output:
            print('Error occurred during adb push:', stdout_output)
        else:
            print('adb push completed successfully!')
        first_connection = False
