import subprocess
import time

# List of app package names to check for
app_package_names = ['com.lenovo.anyshare.gps', 'com.sonymobile.sketch', 'org.scratchjr.android', 'com.qihoo.security', 'com.kotobee.readerapp', 'com.camerasideas.instashot', 'com.estrongs.android.pop', 'air.fourdWhiteboard.debug', 'cn.wps.moffice_eng']

for app_package_name in app_package_names:
    # Run the command and capture the output as a byte string
    output = subprocess.run(['adb', 'shell', 'dumpsys', 'notification', '--noredact'], capture_output=True).stdout

    # Convert the byte string to a regular string
    output_str = output.decode('utf-8')

    # Search for the app package name in the output
    if app_package_name in output_str:

        # Extract the line with the app's notification settings
        lines = [line.strip() for line in output_str.split('\n') if app_package_name in line]
        for line in lines:
            if line.startswith('AppSettings:') and 'importance=NONE' not in line :
                print(line)
                # if line.startswith('AppSettings'):
                #     print(line)


                # if 'importance=NONE' not in line:
                #     print(line.strip())
