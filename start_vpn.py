import subprocess
import sys

# Check if at least one argument (list of config files) is provided
if len(sys.argv) < 2:
    print("Usage: python start_vpn.py <config_file1> <config_file2> ...")
    sys.exit(1)

# Get the list of configuration files from command-line arguments
config_files = sys.argv[1:]

# Start OpenVPN connections for each configuration file
for config_file in config_files:
    cmd = ["openvpn", "--config", config_file]
    subprocess.Popen(cmd)

# Keep the script running to maintain the VPN connections
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
