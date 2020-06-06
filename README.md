# ovpn-surfshark
Tools and scripts to easier use Surfshark with OpenVPN

## Setup
- replace credentials from https://account.surfshark.com/setup/manual with placeholders in `service-credentials.txt`
- run `./download-configs.sh`

## Usage
- run `sudo openvpn de-ber.prod.surfshark.com_udp.ovpn` without beeing prompted for your service credentials

## TODO
- add killswitch on/off script 
- integrate Surfshark API to retreive service credentials automatically