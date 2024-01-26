import os
import subprocess

def fetch_psk(ssid):
    # Save the SSID in a variable
    ssid_filename = ssid + ".nmconnection"

    # Navigate to the folder '/etc/NetworkManager/system-connections'
    connections_directory = "/etc/NetworkManager/system-connections"

    try:
        # Run the ls command to list files in the directory
        ls_command = ["ls", connections_directory]
        ls_output = subprocess.check_output(ls_command, universal_newlines=True)

        # Append the extension nmconnection to the SSID
        ssid_file_path = os.path.join(connections_directory, ssid_filename)

        # Check whether the file name SSID.nmconnection exists in the list
        if ssid_filename in ls_output.splitlines():
            # Open the file using 'sudo cat filename'
            cat_command = ["sudo", "cat", ssid_file_path]
            file_content = subprocess.check_output(cat_command, universal_newlines=True)

            # Check the psk key in the file and extract its value
            psk_start = file_content.find('psk=')
            if psk_start != -1:
                psk_start += len('psk=')
                psk_end = file_content.find('\n', psk_start)
                psk_value = file_content[psk_start:psk_end].strip()

                # Output the value of the psk key
                return psk_value
            else:
                print("PSK key not found in the file.")
        else:
            print(f"File '{ssid_filename}' not found in the directory.")

    except FileNotFoundError:
        print(f"Directory '{connections_directory}' not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user to input the SSID
    target_ssid = input("Enter the SSID for which you want to fetch the password: ")

    # Run the function and print the result
    psk = fetch_psk(target_ssid)
    if psk:
        print(f"The PSK value (password) for SSID '{target_ssid}' is: {psk}")
