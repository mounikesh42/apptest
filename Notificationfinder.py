import subprocess

# Replace with the package names of the apps you want to check
package_name_list = ["cn.wps.moffice_eng"]

for package_name in package_name_list:
    try:
        # Query the app's notification settings
        query_cmd = f"cmd notification list {package_name}"
        output = subprocess.check_output(["adb", "shell", query_cmd]).decode()
        print(output)

        # Parse the output for notification status
        if "allowNotifications=true" in output:
            print(f"Notifications for {package_name} are ON")
        elif "allowNotifications=false" in output:
            print(f"Notifications for {package_name} are OFF")
        else:
            print(f"Could not determine notification status for {package_name}")

    except Exception as e:
        print(f"Error checking notifications for {package_name}: {e}")
