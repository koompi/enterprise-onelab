# Setup Content Server on Raspberry Pi Archlinux ARM


## Install Necessary Package

```console
yay -S rsync bind hostapd dhcp nginx-mainline pm2 npm docker docker-compose
sudo usermod -aG docker alarm
```

## Setup Hostapd

```console
sudo mv /etc/hostapd/hostapd.conf{,.default}
sudo nano /etc/hostapd/hostapd.conf
```
```console
interface=wlan0
# SSID to be used in IEEE 802.11 management frames
ssid=Sala
# Driver interface type (hostap/wired/none/nl80211/bsd)
driver=nl80211
# Country code (ISO/IEC 3166-1)
#country_code=US

# Operation mode (a = IEEE 802.11a (5 GHz), b = IEEE 802.11b (2.4 GHz)
hw_mode=g
# Channel number
channel=6
# Maximum number of stations allowed
#max_num_sta=5

# Bit field: bit0 = WPA, bit1 = WPA2
wpa=2
# Bit field: 1=wpa, 2=wep, 3=both
auth_algs=1

# Set of accepted cipher suites; disabling insecure TKIP
wpa_pairwise=CCMP
# Set of accepted key management algorithms
wpa_key_mgmt=WPA-PSK
wpa_passphrase=Koompi-Onelab

# hostapd event logger configuration
logger_stdout=-1
logger_stdout_level=2

ignore_broadcast_ssid=0
macaddr_acl=0

# Uncomment and modify the following section if your device supports 802.11n
## Enable 802.11n support
ieee80211n=1
## QoS support
wmm_enabled=1
## Use "iw list" to show device capabilities and modify ht_capab accordingly
#ht_capab=[HT40+][SHORT-GI-40][TX-STBC][RX-STBC1][DSSS_CCK-40]
```


## Setup Dhcp and IP

```console
sudo mv /etc/dhcpd.conf{,.default}
sudo nano /etc/dhcpd.conf
```
```console
authoritative;
subnet 10.100.100.0 netmask 255.255.255.0 {
  range 10.100.100.10 10.100.100.254;
  option broadcast-address 10.100.100.255;
  option routers 10.100.100.1;
  default-lease-time 600;
  max-lease-time 7200;
  option domain-name "local";
  option domain-name-servers 10.100.100.1;
}
```

```console 
sudo mv /etc/dhcpcd.conf{,.default}
sudo nano /etc/dhcpcd.conf
```
```console
# A sample configuration for dhcpcd.
# See dhcpcd.conf(5) for details.

# Allow users of this group to interact with dhcpcd via the control socket.
#controlgroup wheel

# Inform the DHCP server of our hostname for DDNS.
#hostname

# Use the hardware address of the interface for the Client ID.
#clientid
# or
# Use the same DUID + IAID as set in DHCPv6 for DHCPv4 ClientID as per RFC4361.
# Some non-RFC compliant DHCP servers do not reply with this set.
# In this case, comment out duid and enable clientid above.
duid

# Persist interface configuration when dhcpcd exits.
persistent

# vendorclassid is set to blank to avoid sending the default of
# dhcpcd-<version>:<os>:<machine>:<platform>
vendorclassid

# A list of options to request from the DHCP server.
option domain_name_servers, domain_name, domain_search
option classless_static_routes
# Respect the network MTU. This is applied to DHCP routes.
option interface_mtu

# Request a hostname from the network
option host_name

# Most distributions have NTP support.
#option ntp_servers

# Rapid commit support.
# Safe to enable by default because it requires the equivalent option set
# on the server to actually work.
option rapid_commit

# A ServerID is required by RFC2131.
require dhcp_server_identifier

# Generate SLAAC address using the Hardware Address of the interface
#slaac hwaddr
# OR generate Stable Private IPv6 Addresses based from the DUID
slaac private
noipv4ll

interface wlan0
static ip_address=10.100.100.1/24
```

## Setup DNS

```console
sudo nano /etc/named.conf
```
paste this in
```console
include "/etc/named.conf.master";
```

Next, 
```console
sudo nano /etc/named.conf.master
```
```console
zone "koompi.com" IN {
        type master;
        file "koompi.zone";
        allow-update { none; };
        notify no;
};
```

Next, 
```console
sudo nano /var/named/koompi.zone
```

paste this in

```console
$TTL 7200
; koompi.com
@       IN      SOA     sala.koompi.com. salabackend.koompi.com. (
                                        2018111111 ; Serial
                                        28800      ; Refresh
                                        1800       ; Retry
                                        604800     ; Expire - 1 week
                                        86400 )    ; Negative Cache TTL
                IN      NS      sala
                IN      NS      salabackend
sala            IN      A       10.100.100.1
salabackend     IN      A       10.100.100.1
```

```console
sudo systemctl enable --now hostapd
sudo systemctl enable --now dhcpcd
sudo systemctl enable --now dhcpd
sudo systemctl enable --now named
```


## Setup Web Server

```console
sudo mkdir -p /etc/nginx/sites-available
sudo mkdir -p /etc/nginx/sites-enabled
sudo mv /etc/nginx/nginx.conf{,.default}
sudo nano /etc/nginx/nginx.conf
```
```console
user http;
worker_processes auto;
worker_cpu_affinity auto;

events {
  multi_accept on;
  worker_connections 1024;
}

http {
  charset utf-8;
  sendfile on;
  tcp_nopush on;
  tcp_nodelay on;
  server_tokens off;
  log_not_found off;
  types_hash_max_size 4096;
  client_max_body_size 16M;

  # MIME
  include mime.types;
  default_type application/octet-stream;

  # logging
  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log warn;

  # load configs
  include /etc/nginx/conf.d/*.conf;
  include /etc/nginx/sites-enabled/*;
}
```


```console
sudo nano /etc/nginx/sites-available/sala.koompi.com.conf
```

Then, paste this in

```console
server {
  listen 80;
  listen 443;
    server_name sala.koompi.com;

    location / {
        proxy_pass http://127.0.0.1:7001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Next,

```console
sudo nano /etc/nginx/sites-available/salabackend.koompi.com.conf
```

Paste this in

```console
server {
  listen 80;
    server_name salabackend.koompi.com;

    location / {
        proxy_pass http://127.0.0.1:7002;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
  listen 443 ssl;
    server_name salabackend.koompi.com;
    return 301 http://$host$request_uri;
    ssl_prefer_server_ciphers   on;  
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; 

    ssl_certificate /etc/nginx/ssl/backend-fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/backend-privkey.pem;

    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options "nosniff";
}
```

Next,

```console
sudo ln -sf /etc/nginx/sites-available/*.conf /etc/nginx/sites-enabled/
sudo systemctl enable --now nginx
```

## Setup Database Server

```console
sudo systemctl enable --now docker
```


```console
version: '3'

services:
  mongodb:
    image: webhippie/mongodb:latest
    container_name: mongodb
    volumes:
      - /home/alarm/docker/db:/var/lib/mongodb
      - /home/alarm/docker/backup:/var/lib/backup
    ports:
      - "27017:27017"
      - "27018:27018"
      - "27019:27019"
    environment:
      - MONGODB_AUTH=true
      - MONGODB_HTTPINTERFACE=false
    restart: always
```
```console
mkdir -p /home/alarm/docker/
mkdir -p /home/alarm/docker/db
mkdir -p /home/alarm/docker/backup
docker-compose up -d
```

## Add-on

### Fix unstable SSD connection

```console
echo \
'#!/bin/bash
UUID=
$MOUNT=
while true;
do


        [[ "$(ls $MOUNT 2>/dev/null >> /dev/null; echo $?)" == 2 ]] && \
        pm2 stop 1 >> /dev/null && \
        pm2 stop 0 >> /dev/null && \
        sudo umount -f $MOUNT && \
        sudo mount -U $UUID $MOUNT && \
        pm2 start 1 >> /dev/null && \
        pm2 start 1 >> /dev/null

        sleep 10;

done
' | sudo tee /usr/bin/fixsala.sh
sudo chmod +x /usr/bin/fixsala.sh

echo \
'[Unit]
Description=Remount SSD and Restart PM2

[Service]
Type=oneshot
ExecStart=/usr/bin/fixsala.sh
RemainAfterExit=yes


[Install]
WantedBy=multi-user.target
' | sudo tee /usr/lib/systemd/system/fixsala.service
```

**Note:** ***Please Input the localtion of the mount point and the UUID of the drive in the variables above***


### Fix Mongodb Lock after reboot

```console
echo \
'#!/bin/bash

docker stop mongodb
rm -rf /home/alarm/docker/db/mongod.lock
docker start mongodb' | sudo tee /usr/bin/fixmongodb.sh
sudo chmod +x /usr/bin/fixmongodb.sh

echo \
'[Unit]
Description=Remove Mongodb lock and Restart Docker
After=docker.service

[Service]
Type=oneshot
ExecStart=/usr/bin/fixmongodb.sh
RemainAfterExit=yes


[Install]
WantedBy=multi-user.target' | sudo tee /usr/lib/systemd/system/fixmongodb.service
```

### Sync Content

```console
#!/bin/bash

AWSKEY=
SRV=
AWSBACKEND=
AWSDB=
SRVDB=
SRVBACKEND=
collections=()
USERNAME=
PASSWORD=


rsync -av -e "ssh -i $AWSKEY" $SRV:$AWSBACKEND $SRVBACKEND
rsync -av -e "ssh -i $AWSKEY" $SRV:$AWSDB $SRVDB


for((i=0; i<${#collections[@]};i++)){

  docker exec -it mongodb mongoimport \
  --db koompi-academy \
  --collection ${collections[$i]} \
  --authenticationDatabase admin \
  --username $USERNAME\
  --password $PASSWORD  \
  --upsert \
  --file /var/lib/mongodb/${collections[$i]}\
  --jsonArray

}

pm2 restart 1
```

**Note:** ***Please Input the all the varaibles needed***


## Extra

A firewall could be used to increase the security of the web browser by allowing only the nginx listen port out to network using **```iptables```**.