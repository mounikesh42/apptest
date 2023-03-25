import subprocess

# path to the new Erudex folder on your local machine
new_folder_path = 'Erudex'

# path to the existing Erudex folder on your phone
phone_folder_path = '/storage/emulated/0/'

# list of device ids to push the content to
device_ids = ['HNP096D4', 'HNP096E2']

# construct the adb push commands for each device
cmds = []
for device_id in device_ids:
    cmd = ['adb', '-s', device_id, 'push', new_folder_path, phone_folder_path]
    cmds.append(cmd)

# execute the adb push commands using subprocess
processes = []
for cmd in cmds:
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    processes.append(process)

# wait for all processes to complete
for process in processes:
    process.wait()

    # check for errors on stdout
    stdout_output = process.stdout.read().decode().strip()
    if 'error' in stdout_output:
        print(f'Error occurred during adb push for device {device_id}:', stdout_output)
    else:
        print(f'Replaced content successfully for device {device_id}!')
