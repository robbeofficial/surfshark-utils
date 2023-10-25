import requests
import sys

# read args
private_key = None
target_dir = "/etc/wireguard/"

if len(sys.argv) < 2:
    print("Usage: python fetch-wireguard-configs.py PRIVATE_KEY [TARGET_DIR]")
    sys.exit(1)
elif len(sys.argv) < 3:
    private_key = sys.argv[1]
elif len(sys.argv) < 4:
    out_dir = sys.argv[2]

clusters_endpoint = "https://api.surfshark.com/v4/server/clusters/"
cluster_types = ["generic", "double", "static", "obfuscated"]

config_template = """[Interface]
PrivateKey = {privKey}
Address = 10.14.0.2/16
DNS = 162.252.172.57, 149.154.159.92

[Peer]
PublicKey = {pubKey}
AllowedIPs = 0.0.0.0/0
Endpoint = {connectionName}:51820"""

# fetch clusters
clusters = requests.get(clusters_endpoint + "generic").json()

# write wireguard configs
for cluster in clusters:
    fname = cluster["connectionName"].split('.')[0] + ".conf"
    with open(target_dir + "/" + fname, 'w') as fp:
        fp.write(config_template.format(**cluster, privKey=private_key))