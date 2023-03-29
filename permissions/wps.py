import subprocess
import time
output = subprocess.run('adb shell dumpsys notification --noredact | findstr air.Whiteboard.debug', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# print()

app_package_name =  'cn.wps.moffice_eng'



output_str = output.stdout



if app_package_name in output_str:
        # Extract the line with the app's notification settings
    line = [line for line in output_str.split('\n') if app_package_name in line][0]

        # Check if the app's notification importance is not NONE
    if 'importance=NONE' not in line:
        print(line)
        time.sleep(1)

            # Launch the app notification settings
        subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', f'package:{app_package_name}'])

            # Wait for a few seconds to ensure that the settings activity is launched
        time.sleep(3)

            # Simulate screen tap at (500, 650)
        subprocess.run(['adb', 'shell', 'input', 'tap', '500', '650'])

            # Wait for a few seconds before simulating the second tap
        time.sleep(1)

            # Simulate screen tap at (500, 550)
        subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])

        time.sleep(1)

    else:
        print(f'No notification importance found for {app_package_name}')
