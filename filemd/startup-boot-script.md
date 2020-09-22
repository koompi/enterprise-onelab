# Make Script Boot@Startup

## Implementation
To begin, we should have a script that we want to make it startup at boot. Such as this project case, we want to boot spice up at startup and ad it go full screen. So, we make a script that does so in /usr/bin/. You need root permission for this directory.

```bash
echo -e 'remote-viewer spice://$IP:$PORT -f' >  /usr/bin/startupscript.sh
```


make sure that your linux uses Systemd. And then we need to create a file in the directory /etc/systemd/system/. And Make sure, you are root or have root permission

```bash
vim /etc/systemd/system/bootscript.service
```

Or if you prefered nano

```bash
nano /etc/systemd/system/bootscript.service
```

And then paste this in

```bash
[Unit]
Description=Script
After=graphical.target
Conflicts=getty@tty1.service

[Service]
Type=idle
ExecStart=/usr/bin/startupscript.sh

[Install]
WantedBy=graphical.target
```

Next, we need to enable it to start at boot. you need root permission.

```bash
systemctl enable bootscript.service
```

and then it can started at the next reboot.
