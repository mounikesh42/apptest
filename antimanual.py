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
from io import StringIO
import csv
import io
import contextlib
from serialno import serialno



subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'true'])

name = subprocess.run(['adb', 'devices'])



# def run_and_save():
#     # Run the three functions and capture their output in a list
#     output = []
#     output.append(edlp())
#     output.append(esfile())
#     output.append(safe())
#
#     # Convert the list to a CSV-formatted string
#     csv_data = StringIO()
#     writer = csv.writer(csv_data)
#     for row in output:
#         writer.writerow([row])
#
#     # Save the CSV-formatted string to a file
#     with open('output.csv', 'w') as f:
#         f.write(csv_data.getvalue())
def run_and_save():
    # Create a dictionary mapping the function names to their function objects
    function_dict = {'serialno':serialno,'edlp': edlp, 'esfile': esfile, 'safe': safe }

    # Create an in-memory file object to capture the output
    output_file = io.StringIO()

    # Create a dictionary to hold the output of each function
    output_dict = {}

    # Iterate over the functions and capture their output
    for name, func in function_dict.items():
        # Redirect the output of the function to the in-memory file object
        with contextlib.redirect_stdout(output_file):
            func()
        # Save the output to a dictionary with the function name as the key
        output_dict[name] = output_file.getvalue()
        # Reset the in-memory file object for the next function
        output_file.seek(0)
        output_file.truncate()

    # Convert the dictionary to a CSV-formatted string
    csv_data = io.StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(['Function Name', 'Output'])
    for name, output in output_dict.items():
        writer.writerow([name, output])

    # Save the CSV-formatted string to a file
    with open('output.csv', 'w') as f:
        f.write(csv_data.getvalue())

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
