from wps import wps
from safe import safe
from shareit import shareit
from edlp import edlp
from scratch import scratch
from koto import koto
from whiteboard import whiteboard
from inshot import inshot
from esfile import esfile
from sketch import sketch
# from settings import settings
import subprocess
from io import StringIO
import csv
import io
import contextlib
from serialno import serialno
# from time import time
import time
from sdcard import sdcard

script_info = """
 Anti-manual script  v1.0
 Connect device and run the script before that make sure debugging is turned ON
 Happy Testing :)

 Fervid Smart Solutions Private Limited





          _   _ _______ _____      __  __          _   _ _    _         _
     /\   | \ | |__   __|_   _|    |  \/  |   /\   | \ | | |  | |  /\   | |
    /  \  |  \| |  | |    | |______| \  / |  /  \  |  \| | |  | | /  \  | |
   / /\ \ | . ` |  | |    | |______| |\/| | / /\ \ | . ` | |  | |/ /\ \ | |
  / ____ \| |\  |  | |   _| |_     | |  | |/ ____ \| |\  | |__| / ____ \| |____
 /_/    \_\_| \_|  |_|  |_____|    |_|  |_/_/    \_\_| \_|\____/_/    \_\______|
"""


if __name__ == '__main__':
    print(script_info)



subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'true'])

time.sleep(1)
notifications = subprocess.run(['python', 'notifications.py'])


folder_exists = False
cmd = 'adb shell ls /storage/emulated/0/Erudex'
output = subprocess.getoutput(cmd)
if "No such file or directory" not in output:
    folder_exists = True

# Count the number of files in the folder
num_files = 0
if folder_exists:
    cmd = 'adb shell ls -1 /storage/emulated/0/Erudex | find /v /c ""'
    output = subprocess.getoutput(cmd)
    num_files = int(output.strip())

print(f"Folder exists: {folder_exists}")
print(f"Number of files: {num_files}")
ace = "adb uninstall com.sk.aceinstaller2"

# Execute the command using subprocess
aceuninstall = subprocess.run(ace, shell=True)
print(aceuninstall)
subprocess.run(['adb', 'shell', 'svc', 'wifi', 'disable'])

time.sleep(2)



def run_and_save():
    # Create a dictionary mapping the function names to their function objects
    function_dict = {'serialno':serialno, 'edlp': edlp, 'esfile': esfile, 'safe': safe,'scratch':scratch,'whiteboard':whiteboard,'wps':wps,'shareit':shareit,'koto':koto,'inshot':inshot,'sketch':sketch}

    # Create an in-memory file object to capture the output
    output_file = io.StringIO()

    # Iterate over the functions and capture their output
    output_list = []
    for name, func in function_dict.items():
        # Redirect the output of the function to the in-memory file object
        with contextlib.redirect_stdout(output_file):
            func()
        # Save the output to a list
        output_value = output_file.getvalue().strip()
        output_list.append(output_value)
        # Reset the in-memory file object for the next function
        output_file.seek(0)
        output_file.truncate()
        # Print the output to the terminal
        print(f"{name}: {output_value}")

    # Open the CSV file in append mode
    with open('output.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        # Write the output list as a new row to the CSV file
        writer.writerow(output_list)


run_and_save()




# Define the shell command to retrieve the device's current date and time with timezone offset



time.sleep(1)




package_name = 'com.erudex.eduapp.mauritius'
activity_name = 'com.erudex.eduapp.SplashActivity'
open_cmd = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']

# Construct the adb command to force-stop the app

# Open the app using the subprocess module
subprocess.Popen(open_cmd)

time.sleep(1)

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

time.sleep(1)
sdcard()

time.sleep(1)

output = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.incremental"]).decode("utf-8")

# Print the build number
print(output.strip())
time.sleep(1)

subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'false'])
