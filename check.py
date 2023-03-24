import subprocess

# Run the 'adb shell dumpsys notification' command to get the notification state for the package
notification_output = subprocess.check_output(["adb", "shell", "dumpsys", "notification"])

# Check if the package has notifications enabled
if "pkg=com.qihoo.security" in notification_output.decode("utf-8") and "enabled=true" in notification_output.decode("utf-8"):
    print("com.qihoo.security: notifications enabled")
else:
    print("com.qihoo.security: notifications disabled")
    
