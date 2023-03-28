import subprocess
from appium import webdriver
from PIL import Image
import pytesseract
from PIL import Image
import time

import subprocess
import time
from appium import webdriver

def safe():


# Set the package name and activity name for the Chrome app
    package_name = 'com.qihoo.security'
    activity_name = 'com.qihoo.security.ui.main.HomeActivity'

    # Construct the adb command to open the app
    open_cmd = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']

    subprocess.Popen(open_cmd)

    time.sleep(2)



    stop_cmd = ['adb', 'shell', 'am', 'force-stop', package_name]
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
        # elif line.strip().startswith('android.permission.WRITE_EXTERNAL_STORAGE: granted='):
        #     granted = line.strip().split('=')[1]
        #     if granted == 'true, flags':
        #         has_write_storage_permission = True
        # elif line.strip().startswith('android.permission.CAMERA: granted='):
        #     granted = line.strip().split('=')[1]
        #     if granted == 'true, flags':
        #         has_media_location_permission = True

    if has_read_storage_permission :
        print("Safe:Granted")
    else:
        print("Safe:Failed")





# safe()
