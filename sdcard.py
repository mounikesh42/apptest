import subprocess

# Execute the adb shell df command

def sdcard():
    output = subprocess.check_output(["adb", "shell", "df"]).decode("utf-8")

    # Split the output into lines and grab the last line
    lines = output.strip().split("\n")
    last_line = lines[-1]

    # Split the line into fields
    fields = last_line.split()
    # Get the size in bytes and convert to GB
    size_kb = int(fields[1])
    size_gb = size_kb / (1024**2)

    if size_gb > 50:
        print("Size in GB: {:.2f}".format(size_gb))
        dir_path = fields[5]
        subprocess.run(["adb", "shell", f"touch '{dir_path}/test.txt'"])


        output = subprocess.check_output(["adb", "shell", "ls", fields[5]]).decode("utf-8")
        if "test.txt" in output:
                    # Remove the test file
            subprocess.run(["adb", "shell", "rm", fields[5] + "/test.txt"])
            return("working:64 GB")
        else:
            return("SDcard issue please check")
    else:
        return('SDcard issue please check')



    # Execute the adb shell touch command to create a test file in the specified directory
