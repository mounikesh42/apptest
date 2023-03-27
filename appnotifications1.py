import subprocess
import time

# List of app package names to check for
app_package_names = ['cn.wps.moffice_eng', 'com.lenovo.anyshare.gps']

for app_package_name in app_package_names:
    # Run the command and capture the output as a byte string
    output = subprocess.run(['adb', 'shell', 'dumpsys', 'notification', '--noredact'], capture_output=True).stdout

    # Convert the byte string to a regular string
    output_str = output.decode('utf-8')

    # Search for the app package name in the output
    if app_package_name in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if app_package_name in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

            # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', f'package:{app_package_name}'])

            # Wait for a few seconds to ensure that the settings activity is launched
            time.sleep(1)

            # Simulate screen tap at (500, 650)
            subprocess.run(['adb', 'shell', 'input', 'tap', '500', '650'])

            # Wait for a few seconds before simulating the second tap
            time.sleep(1)

            # Simulate screen tap at (500, 550)
            subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])

            time.sleep(1)

        else:
            print(f'No notification importance found for {app_package_name}')
