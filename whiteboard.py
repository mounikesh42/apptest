import subprocess


def whiteboard():
    package_name = 'air.fourdWhiteboard.debug'

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
        elif line.strip().startswith('android.permission.CAMERA: granted='):
            granted = line.strip().split('=')[1]
            if granted == 'true, flags':
                has_media_location_permission = True

    if has_read_storage_permission and has_write_storage_permission and has_media_location_permission:
        print("All permissions granted for whiteboard app")
    else:
        print("Permissions missing")
