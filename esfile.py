import subprocess
import time
def esfile():


    package_name = 'com.estrongs.android.pop'


    activity_name = 'com.estrongs.android.pop.view.FileExplorerActivity'

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
        elif line.strip().startswith('android.permission.WRITE_EXTERNAL_STORAGE: granted='):
            granted = line.strip().split('=')[1]
            if granted == 'true, flags':
                has_write_storage_permission = True
        elif line.strip().startswith('android.permission.ACCESS_MEDIA_LOCATION: granted='):
            granted = line.strip().split('=')[1]
            if granted == 'true, flags':
                has_media_location_permission = True

    if has_read_storage_permission and has_write_storage_permission and has_media_location_permission:
        print("Esfile:Granted")
    else:
        print("Esfile:Failed")
