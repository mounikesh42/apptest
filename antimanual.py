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


script_info = """
\033[32mAnti-manual script  v1.0\033[0m
\033[32m Connect device and run the script before that make sure debugging is turned ON \033[0m
\033[32m Happy Testing :) \033[0m

\033[32m Fervid Smart Solutions Private Limited.\033[0m



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

name = subprocess.run(['adb', 'devices'])

def run_and_save():
    # Create a dictionary mapping the function names to their function objects
    function_dict = {'serialno':serialno,'edlp': edlp, 'esfile': esfile, 'safe': safe,'scratch':scratch,'whiteboard':whiteboard,'wps':wps,'shareit':shareit,'koto':koto,'inshot':inshot,'sketch':sketch}

    # Create an in-memory file object to capture the output
    output_file = io.StringIO()

    # Open the CSV file in append mode
    with open('output.csv', 'a', newline='') as f:
        writer = csv.writer(f)

        # Iterate over the functions and capture their output
        output_list = []
        for name, func in function_dict.items():
            # Redirect the output of the function to the in-memory file object
            with contextlib.redirect_stdout(output_file):
                func()
            # Save the output to a list
            output_list.append(output_file.getvalue().strip())
            # Reset the in-memory file object for the next function
            output_file.seek(0)
            output_file.truncate()

        # Write the output list as a new row to the CSV file
        writer.writerow(output_list)


run_and_save()
# edlp()
# print("")
# esfile()
# print("")
# safe()
# print("")
# #
# scratch()
# print("")
# whiteboard()
# print("")
# shareit()
# print("")
# wps()
# print("")
# koto()
# print("")
#
#
# inshot()
# print("")


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

#
#

#









# settings()

subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'false'])
