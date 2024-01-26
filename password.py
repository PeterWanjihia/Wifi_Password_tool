import subprocess
import os

def list_wifi_connections():
    try:
        # Run the command to list available Wi-Fi connections
        result = subprocess.run(["nmcli", "--fields", "SSID", "device", "wifi", "list"], capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Display the list of Wi-Fi connections
            print("Available Wi-Fi Connections:")
            print(result.stdout)
        else:
            print("Error:", result.stderr)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    list_wifi_connections()


