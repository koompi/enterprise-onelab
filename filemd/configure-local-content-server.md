# Setup Content Server on Raspberry Pi Archlinux ARM

## On Local DNS Server

If you haven't gotten to installed bind yet, please do

```console
sudo pacman -S bind
```

Then if you did, start configuring local dns we shalt

```console
sudo nano /etc/named.conf
```

In there you can add this before logging function

```console
zone "academy.koompilab.org" IN {
        type master;
        file "academy.koompilab.zone";
        allow-update { none; };
        notify no;
};
```

Then we can go and create a zone file

```console
nano /var/named/academy.koompilab.zone
```

Then paste in and replace the domain name ``academy.koompilab.org.`` and the `172.16.1.30` IP with the appropriate one you need to use and the actual IP of the server. But in this case, we want this domain name and IP.

```console
$TTL 7200
; academy.koompilab.org
@       IN      SOA     academy.koompilab.org. academy.koompilab.org. (
                                        2018111111 ; Serial
                                        28800      ; Refresh
                                        1800       ; Retry
                                        604800     ; Expire - 1 week
                                        86400 )    ; Negative Cache TTL
                IN      NS      academy
academy         IN      A       172.16.1.30
www             IN      A       172.16.1.30
```

### Restart the named service

```console
sudo systemctl restart named
```

## On the local web server

On the local web server, we should start with the installation of NGINX (pronounce engine X).

```console
sudo pacman -S nginx-mainline
```

Then we can try starting it, for error checking purposes.

```console
sudo systemctl start nginx
```

The default page served at http://127.0.0.1 is ``/usr/share/nginx/html/index.html``.

Then we can go to configure the nginx configuration

```console
nano /etc/nginx/nginx.conf
```

Then we can paste in this

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

Then we can go to create the neccessary directories and files for the actual domain

```console
sudo mkdir -p /etc/nginx/sites-available
sudo mkdir -p /etc/nginx/sites-enabled
sudo nano /etc/nginx/sites-available/academy.koompilab.org.conf
```

Then we can paste in and modify the neccessary argument for the web application

```console
server {
    listen 80;
        server_name academy.koompilab.org;

        location / {
            proxy_pass http://127.0.0.1:3000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
     }
}
```
Then we can go finish the configuration with

```console
sudo ln -sf /etc/nginx/sites-available/academy.koompilab.org.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

Everything should be working now in browser. Should you see only the default screen of the web nginx, try clear the browser cache. Else, contact me, the author.


## Extra

A firewall could be used to increase the security of the web browser by allowing only the nginx listen port out to network using **```iptables```**.