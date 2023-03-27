import subprocess
import time
# Run the command and capture the output as a byte string
def appnotifications():

    time.sleep(3)
    output = subprocess.run(['adb', 'shell', 'dumpsys', 'notification', '--noredact'], capture_output=True).stdout

    # Convert the byte string to a regular string
    output_str = output.decode('utf-8')

    # Search for the app package name in the output
    if 'cn.wps.moffice_eng' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'cn.wps.moffice_eng' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:cn.wps.moffice_eng'])

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
            print('noooo')


    if 'com.lenovo.anyshare.gps' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'com.lenovo.anyshare.gps' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.lenovo.anyshare.gps'])

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
            print('noooo')



    if 'com.estrongs.android.pop' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'com.estrongs.android.pop' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.estrongs.android.pop'])

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
            print('noooo')



    if 'com.camerasideas.instashot' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'com.camerasideas.instashot' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.camerasideas.instashot'])

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
            print('noooo')

    if 'com.kotobee.readerapp' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'com.kotobee.readerapp' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.kotobee.readerapp'])

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
            print('noooo')
    if 'com.qihoo.security' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'com.qihoo.security' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.qihoo.security'])

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
            print('noooo')




    if 'org.scratchjr.android' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'org.scratchjr.android' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:org.scratchjr.android'])

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
            print('noooo')


    if 'com.sonymobile.sketch' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'com.sonymobile.sketch' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.sonymobile.sketch'])

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
            print('noooo')



    if 'air.fourdWhiteboard.debug' in output_str:
        # Extract the line with the app's notification settings
        line = [line for line in output_str.split('\n') if 'air.fourdWhiteboard.debug' in line][0]

        # Check if the app's notification importance is not NONE
        if 'importance=NONE' not in line:

        # Launch the app notification settings
            subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:air.fourdWhiteboard.debug'])

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
            print('noooo')
# appnotifications()
    # hereeeeeeeeeeeeeee..................????????????????/
    # import subprocess
    # import time
    #
    # # Launch app details settings for a package
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.qihoo.security'])
    #
    # # Wait for a few seconds to ensure that the settings activity is launched
    # time.sleep(1)
    #
    # # Simulate screen tap at (500, 650)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '650'])
    #
    # # Wait for a few seconds before simulating the second tap
    # time.sleep(1)
    #
    # # Simulate screen tap at (500, 550)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    # time.sleep(1)
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.estrongs.android.pop'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    # time.sleep(1)
    #
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.camerasideas.instashot'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    # time.sleep(1)
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.kotobee.readerapp'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    #
    # time.sleep(1)
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.qihoo.security'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    # time.sleep(1)
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:org.scratchjr.android'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    #
    # time.sleep(1)
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.lenovo.anyshare.gps'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    #
    # time.sleep(1)
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.sonymobile.sketch'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    #
    # time.sleep(1)
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:air.fourdWhiteboard.debug'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
    #
    # time.sleep(1)
    #
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:cn.wps.moffice_eng'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
    # time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
