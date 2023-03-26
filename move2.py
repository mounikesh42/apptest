import subprocess
import csv
import os
import smtplib
from email.mime.text import MIMEText


# create or open the csv file to write data
with open('device_data.csv', mode='a+', newline='') as csv_file:
    fieldnames = ['Device', 'Num_Files']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # check if the csv file is empty and write the headers
    csv_file.seek(0)
    first_char = csv_file.read(1)
    if not first_char:
        writer.writeheader()

    # path to the new Erudex folder on your local machine
    new_folder_path = 'Erudex'

    # path to the existing Erudex folder on your phone
    phone_folder_path = '/storage/emulated/0/'

    # construct the adb push command
    cmd = ['adb', 'push', new_folder_path, phone_folder_path]

    dele = ['adb','shell','rm','/storage/emulated/0/Erudex/*']
    devices_output = subprocess.getoutput('adb devices -l')
    device_name = None
    for line in devices_output.split('\n'):
        if 'model:' in line:
            device_name = line.split('model:')[0].strip()
            break
    # execute the adb push command using subprocess
    delete = subprocess.Popen(dele, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    delete.wait()

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()

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
                with open('error.csv', mode='a+', newline='') as csv_file:
                    fieldnames = ['Device', 'status']
                    check = csv.DictWriter(csv_file, fieldnames=fieldnames)

                    # check if the csv file is empty and write the headers
                    csv_file.seek(0)
                    first_char = csv_file.read(1)
                    if not first_char:
                        check.writeheader()

                    check.writerow({'Device': device_name, 'status': 'failed'})





                print('Error occurred during adb push:', stdout_output)
                print(  """
                   __      _ _          _               _
                  / _|    (_) |        | |             | |
                 | |_ __ _ _| | ___  __| |             | |
                 |  _/ _` | | |/ _ \/ _` |             | |
                 | || (_| | | |  __/ (_| |  _ _ _ _ _  |_|
                 |_| \__,_|_|_|\___|\__,_| (_|_|_|_|_) (_)
                                                          """ )
            else:
                num_files = 0
                # check if the Erudex folder exists on the device
                folder_exists_cmd = 'adb shell "[ -d /storage/emulated/0/Erudex ] && echo 1 || echo 0"'
                folder_exists_output = subprocess.getoutput(folder_exists_cmd)
                folder_exists = True if int(folder_exists_output.strip()) == 1 else False
                if folder_exists:
                    # get the number of files in the Erudex folder on the device
                    cmd = 'adb shell ls -1 /storage/emulated/0/Erudex | find /v /c ""'
                    output = subprocess.getoutput(cmd)
                    num_files = int(output.strip())

                # write the device data to the csv file

                writer.writerow({'Device': device_name, 'Num_Files': num_files})
                if num_files < 100:
                    if num_files > 100:

                        print('failed')
                        print(  """
   __      _ _          _               _
  / _|    (_) |        | |             | |
 | |_ __ _ _| | ___  __| |             | |
 |  _/ _` | | |/ _ \/ _` |             | |
 | || (_| | | |  __/ (_| |  _ _ _ _ _  |_|
 |_| \__,_|_|_|\___|\__,_| (_|_|_|_|_) (_)
                                          """ )
                else:

                    print( 'Succes' )
                    print(f'Device: {device_name}')
                    print(f'Device: {num_files}')


            first_connection = False
