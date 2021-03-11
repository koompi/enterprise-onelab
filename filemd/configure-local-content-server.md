# Setup Content Server on Raspberry Pi Archlinux ARM


## Install Necessary Package

```console
yay -S rsync bind hostapd dhcp nginx-mainline pm2 npm bridge-utils
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
  autoindex on;
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
sudo brctl addbr virbr0
sudo nano /etc/systemd/network/virbr0.network
```
Then Type in this.
```console
[Match]
Name=virbr0
Virtualization=false

[Network]
Address=10.100.200.1/24
LinkLocalAddressing=yes
IPMasquerade=yes
IPForward=yes
LLDP=yes
EmitLLDP=customer-bridge
```

Then,
```console
sudo nano /etc/systemd/network/virbr0.netdev
```
Then Type in this.

```console
[NetDev]
Name=virbr0
Kind=bridge
```

Then, start the service and enable it

```console
systemctl enable --now systemd-networkd
sudo iptables -A FORWARD -i virbr0 -o eth0 -j ACCEPT
sudo iptables-save -f /etc/iptables/iptables.rules
```

Then,

```console
cd DirectoryOfTheStorage
mkdir mongodb
sudo pacstrap -c mongodb/ coreutils shadows pacman systemd iproute2 iputils nano procps-ng
sudo systemd-nspawn -D mongodb
```
Then, inside the container

```console
passwd
useradd -m isaac
passwd isaac
logout
```

Then,
```console
sudo nano /etc/systemd/system/systemd-nspawn@mongodb.service
```

Then, type in this

```console
#  SPDX-License-Identifier: LGPL-2.1-or-later
#
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

[Unit]
Description=Container %i
Documentation=man:systemd-nspawn(1)
Wants=modprobe@tun.service modprobe@loop.service modprobe@dm-mod.service
PartOf=machines.target
Before=machines.target
After=network.target systemd-resolved.service modprobe@tun.service modprobe@loop.service modprobe@dm-mod.service
RequiresMountsFor=/var/lib/machines/%i

[Service]
# Make sure the DeviceAllow= lines below can properly resolve the 'block-loop' expression (and others)
ExecStart=systemd-nspawn --quiet --keep-unit --boot --link-journal=try-guest --network-bridge=virbr0 -U --settings=override --machine=%i
KillMode=mixed
Type=notify
RestartForceExitStatus=133
SuccessExitStatus=133
Slice=machine.slice
Delegate=yes
TasksMax=16384
WatchdogSec=3min

# Enforce a strict device policy, similar to the one nspawn configures when it
# allocates its own scope unit. Make sure to keep these policies in sync if you
# change them!
DevicePolicy=closed
DeviceAllow=/dev/net/tun rwm
DeviceAllow=char-pts rw

# nspawn itself needs access to /dev/loop-control and /dev/loop, to implement
# the --image= option. Add these here, too.
DeviceAllow=/dev/loop-control rw
DeviceAllow=block-loop rw
DeviceAllow=block-blkext rw

# nspawn can set up LUKS encrypted loopback files, in which case it needs
# access to /dev/mapper/control and the block devices /dev/mapper/*.
DeviceAllow=/dev/mapper/control rw
DeviceAllow=block-device-mapper rw

[Install]
WantedBy=machines.target
```

Then, login into it

```console
sudo machinectl login mongodb
```

Inside the container, type this

```console
nano /etc/systemd/network/host0.network
```

Then, type in this

```console
#  SPDX-License-Identifier: LGPL-2.1-or-later
#
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

# This network file matches the container-side of the virtual Ethernet link
# created by systemd-nspawn's --network-veth switch. See systemd-nspawn(1) for
# details.

[Match]
Virtualization=container
Name=host0

[Network]
Address=10.100.200.2/24
Gateway=10.100.200.1
DNS=10.100.200.1
LinkLocalAddressing=yes
LLDP=yes
EmitLLDP=customer-bridge

[DHCP]
UseTimezone=yes
```

Then, start the service

```console
systemctl enable --now systemd-networkd
```

Then, install mongodb

```console
pacman -U http://tardis.tiny-vps.com/aarm/packages/b/boost-libs/boost-libs-1.62.0-4-armv7h.pkg.tar.xz --noconfirm &&
pacman -U http://tardis.tiny-vps.com/aarm/packages/y/yaml-cpp/yaml-cpp-0.5.3-3-armv7h.pkg.tar.xz --noconfirm &&
pacman -U http://tardis.tiny-vps.com/aarm/packages/o/openssl-1.0/openssl-1.0-1.0.2.k-3-armv7h.pkg.tar.xz --noconfirm &&
pacman -U http://tardis.tiny-vps.com/aarm/packages/i/icu/icu-58.2-2-armv7h.pkg.tar.xz --noconfirm &&
pacman -U http://tardis.tiny-vps.com/aarm/packages/s/snappy/snappy-1.1.3-2-armv7h.pkg.tar.xz --noconfirm &&
pacman -U http://tardis.tiny-vps.com/aarm/packages/g/gcc-libs/gcc-libs-6.2.1-1-armv7h.pkg.tar.xz --noconfirm &&
pacman -U http://tardis.tiny-vps.com/aarm/packages/m/mongodb/mongodb-3.2.10-2-armv7h.pkg.tar.xz --noconfirm &&
pacman -U http://tardis.tiny-vps.com/aarm/packages/m/mongodb-tools/mongodb-tools-3.2.5-1-armv7h.pkg.tar.xz --noconfirm 
```

Then, configure Mongodb

```console
mv /etc/mongodb/mongodb.conf{,.default}
nano /etc/mongodb/mongodb.conf
```

Then type this this

```console
# mongodb.conf

# Where to store the data.
dbpath=/var/lib/mongodb

#where to log
logpath=/var/log/mongodb/mongodb.log

logappend=true

bind_ip = 127.0.0.1
#port = 27017

# Enable journaling, http://www.mongodb.org/display/DOCS/Journaling
journal=true

# Enables periodic logging of CPU utilization and I/O wait
#cpu = true

# Turn on/off security.  Off is currently the default
#noauth = true
auth = true

# Verbose logging output.
#verbose = true

# Inspect all client data for validity on receipt (useful for
# developing drivers)
#objcheck = true

# Enable db quota management
#quota = true

# Set diagnostic logging level where n is
#   0=off (default)
#   1=W
#   2=R
#   3=both
#   7=W+some reads
#diaglog = 0

# Diagnostic/debugging option
#nocursors = true

# Ignore query hints
#nohints = true

# Disable the HTTP interface (Defaults to localhost:27018).
nohttpinterface = true

# Turns off server-side scripting.  This will result in greatly limited
# functionality
#noscripting = true

# Turns off table scans.  Any query that would do a table scan fails.
#notablescan = true

# Disable data file preallocation.
#noprealloc = true

# Specify .ns file size for new databases.
# nssize = <size>

# Accout token for Mongo monitoring server.
#mms-token = <token>

# Server name for Mongo monitoring server.
#mms-name = <server-name>

# Ping interval for Mongo monitoring server.
#mms-interval = <seconds>

# Replication Options

# in replicated mongo databases, specify here whether this is a slave or master
#slave = true
#source = master.example.com
# Slave only: specify a single database to replicate
#only = master.example.com
# or
#master = true
#source = slave.example.com

# Address of a server to pair with.
#pairwith = <server:port>
# Address of arbiter server.
#arbiter = <server:port>
# Automatically resync if slave data is stale
#autoresync
# Custom size for replication operation log.
#oplogSize = <MB>
# Size limit for in-memory storage of op ids.
#opIdMem = <bytes>

# SSL options
# Enable SSL on normal ports
#sslOnNormalPorts = true
# SSL Key file and password
#sslPEMKeyFile = /etc/ssl/mongodb.pem
#sslPEMKeyPassword = pass
```

Then, start the service

```console
echo 'net.ipv4.ip_forward=1
net.ipv4.conf.host0.route_localnet=1' |tee /etc/sysctl.d/30-ipforward.conf
iptables -t nat -I PREROUTING -p tcp -d 10.100.200.2/24 --dport 27017 -j DNAT --to-destination 127.0.0.1:27017
iptables-save -f /etc/iptables/iptables.rules
systemctl enable --now mongodb iptables
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
  
  mongoimport\
  --db koompi-academy \
  --collection ${collections[$i]} \
  --authenticationDatabase admin \
  --username $USERNAME \
  --password $PASSWORD  \
  --upsert \
  --file $SRVDB/${collections[$i]}.json \
  --jsonArray

}

pm2 restart 1
```

### Manage Admin Account on Mongodb

#### Create Admin

```console
use admin
db.createUser(
  {
    user: "USERNAME",
    pwd: "PASSWORD", // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)
```

#### Login Admin

```console
mongo --port 27017  --authenticationDatabase "admin" -u "USERNAME" -p 
```

**Note:** ***Please Input the all the varaibles needed***


## Extra

A firewall could be used to increase the security of the web browser by allowing only the nginx listen port out to network using **```iptables```**.