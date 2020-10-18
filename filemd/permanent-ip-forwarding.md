# Enable Internet forward from Wifi to Ethernet

## Configure forwarding rules

Get access to root. This could be done with sudo, but i wouldn't recommend it, because bugs might appear.

```console
sudo su
```

Or

```console
su
```

And then we need to enable ip forwarding in linux kernel

```console
sysctl net.ipv4.ip_forward=1
echo '\
net.ipv4.ip_forward=1
net.ipv6.conf.default.forwarding=1
net.ipv6.conf.all.forwarding=1' >> /etc/sysctl.d/30-ipforward.conf
```

## Enable Nat

```console
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
```

## Make it permanent

```console
iptables-save -f /etc/iptables/iptables.rules
systemctl enable iptables
systemctl start iptables
```

## Setup Necessary Option

You might need to configure an ip for the local interface in a range. For example, this machine ethernet interface might be 172.16.1.1/24

```console
nmtui
```

You might also need to setup local DNS server, or have all clients point to another dns server that is valid