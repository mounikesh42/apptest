import subprocess
import time

def sketch():



    package_name = 'com.sonymobile.sketch'
    activity_name = '.dashboard.DashboardActivity'

    # Construct the adb command to open the app
    open_cmd = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']

    # Construct the adb command to force-stop the app
    stop_cmd = ['adb', 'shell', 'am', 'force-stop', package_name]

    # Open the app using the subprocess module
    subprocess.Popen(open_cmd)

    # Wait for 10 seconds
    time.sleep(3)

    # Force-stop the app using the subprocess module
    subprocess.Popen(stop_cmd)

    result = subprocess.run(['adb', 'shell', 'dumpsys', 'package', package_name], capture_output=True, text=True)




    has_read_storage_permission = False
    has_write_storage_permission = False
    has_media_location_permission = False

    for line in result.stdout.split('\n'):

        if line.strip().startswith('android.permission.READ_EXTERNAL_STORAGE: granted='):
            granted = line.strip().split('=')[1]
            if granted == 'true, flags':
                has_read_storage_permission = True
        elif line.strip().startswith('android.permission.WRITE_EXTERNAL_STORAGE: granted='):
            granted = line.strip().split('=')[1]
            if granted == 'true, flags':
                has_write_storage_permission = True
        # elif line.strip().startswith('android.permission.CAMERA: granted='):
        #     granted = line.strip().split('=')[1]
        #     if granted == 'true, flags':
        #         has_media_location_permission = True

    if has_read_storage_permission and has_write_storage_permission:
        print("All permissions granted for sketch app")
    else:
        print("Permissions missing")

sketch()
