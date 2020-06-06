#!/bin/bash

# download configs
wget https://account.surfshark.com/api/v1/server/configurations
unzip -o configurations
rm configurations

# add service credentials file
for ovpn in *.ovpn
do
    sed -i 's/.*auth-user-pass.*/auth-user-pass service-credentials.txt/g' ${ovpn}
done