# ovpn-surfshark
Tools and scripts to easier use Surfshark with OpenVPN

## Setup
- replace your credentials with placeholders in `service-credentials.txt`
- run `./download-configs.sh`

## Usage
- run `sudo openvpn de-ber.prod.surfshark.com_udp.ovpn` without beeing prompted for your service credentials
- run `sudo python start_vpn.py <config_file1> <config_file2>` to start multiple interfaces simultaneously

## TODO
- add killswitch on/off script 
- integrate Surfshark API to retreive service credentials automatically