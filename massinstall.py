import os

# Change directory to the folder containing the APKs

def massinstall():
    os.chdir('Apps')

    # Get a list of all the APKs in the folder
    apk_list = [apk for apk in os.listdir() if apk.endswith('.apk')]

    # Install each APK one by one
    for apk in apk_list:
        os.system(f'adb install -r "{apk}"')

massinstall()
