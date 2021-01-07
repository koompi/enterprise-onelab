# Setup Content Server on Raspberry Pi Archlinux ARM


## Install Necessary Package

```console
yay -S rsync bind hostapd dhcp nginx-mainline pm2 npm
```

## Setup Hostapd

```console
sudo mv /etc/hostapd/hostapd.conf{,.default}
echo \
'interface=wlan0
# SSID to be used in IEEE 802.11 management frames
ssid=Sala
# Driver interface type (hostap/wired/none/nl80211/bsd)
driver=nl80211
# Country code (ISO/IEC 3166-1)
country_code=US

# Operation mode (a = IEEE 802.11a (5 GHz), b = IEEE 802.11b (2.4 GHz)
hw_mode=g
# Channel number
channel=7
# Maximum number of stations allowed
max_num_sta=5

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

# Uncomment and modify the following section if your device supports 802.11n
## Enable 802.11n support
ieee80211n=1
## QoS support
#wmm_enabled=1
## Use "iw list" to show device capabilities and modify ht_capab accordingly
#ht_capab=[HT40+][SHORT-GI-40][TX-STBC][RX-STBC1][DSSS_CCK-40]' | sudo tee /etc/hostapd/hostapd.conf
```

## Setup Dhcp and IP

```console
sudo mv /etc/dhcpd.conf{,.default}
echo \
'authoritative;
option domain-name-servers 10.100.100.1;
option subnet-mask 255.255.255.0;
option routers 10.100.100.1;
subnet 10.100.100.0 netmask 255.255.255.0 {
    range 10.100.100.10 10.100.100.254;
    max-lease-time 600;
    allow unknown-clients;
}' | sudo tee /etc/dhcpd.conf
    
sudo mv /etc/dhcpcd.conf{,.default}
echo \
\# A sample configuration for dhcpcd.
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
static ip_address=10.100.100.1/24' | sudo tee /etc/dhcpcd.conf
```

## Setup DNS

```console
echo 'include "/etc/named.conf.master";' | sudo tee -a /etc/named.conf >> /dev/null

echo \
'zone "koompilab.org" IN {
        type master;
        file "koompilab.zone";
        allow-update { none; };
        notify no;
};' | sudo tee -a /etc/named.conf.master

echo \
'$TTL 7200
; koompilab.org
@       IN      SOA     sala.koompilab.org. salabackend.koompilab.org. (
                                        2018111111 ; Serial
                                        28800      ; Refresh
                                        1800       ; Retry
                                        604800     ; Expire - 1 week
                                        86400 )    ; Negative Cache TTL
                IN      NS      sala
                IN      NS      salabackend
sala            IN      A       10.100.100.1
salabackend     IN      A       10.100.100.1' | sudo tee -a /var/named/koompilab.zone
```

## Setup Web Server

```console
sudo mv /etc/nginx/nginx.conf{,.default}
echo \
'user http;
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
}' | sudo tee -a /etc/nginx/nginx.conf
sudo mkdir -p /etc/nginx/sites-available
sudo mkdir -p /etc/nginx/sites-enabled
echo \
'server {
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
}' | sudo tee /etc/nginx/sites-available/sala.koompilab.org.conf

echo \
'server {
    listen 80;
    listen 443;
        server_name sala.koompi.com;

        location / {
            proxy_pass http://127.0.0.1:7002;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
    }
}' | sudo tee /etc/nginx/sites-available/salabackend.koompilab.org.conf
sudo ln -sf /etc/nginx/sites-available/*.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

## Extra

A firewall could be used to increase the security of the web browser by allowing only the nginx listen port out to network using **```iptables```**.