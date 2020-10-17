# Make Script Boot@Startup

## Implementation
To begin, we should have a script that we want to make it startup at boot. Such as this project case, we want to boot spice up at startup and ad it go full screen. So, we make a script that does so in /usr/bin/. You need root permission for this directory.

```console
echo -e '#!/bin/bash\nremote-viewer spice://$IP:$PORT -f' >  /usr/bin/startupscript.sh
```

And then you need to add execute permission to this script file

```console
sudo chmod +x /usr/bin/startupscript.sh
```

make sure that your linux uses Systemd. And then we need to create a file in the directory /etc/systemd/system/. And Make sure, you are root or have root permission

```console
vim /etc/systemd/system/bootscript.service
```

Or if you prefered nano

```console
nano /etc/systemd/system/bootscript.service
```

And then paste this in

```console
[Unit]
Description=Bootup Spice
After=graphical.target

[Service]
Type=idle
ExecStart=/usr/bin/startupscript.sh

[Install]
WantedBy=graphical.target
```

`Note` : This is another sample for another project

```console
[Unit]
Description=Create dns directory for samba domain

[Service]
Type=oneshot
ExecStart=/usr/bin/namedhelper.sh
RemainAfterExit=yes


[Install]
WantedBy=multi-user.target
```


Next, we need to enable it to start at boot. you need root permission.

```console
systemctl enable bootscript.service
```

and then it can started at the next reboot.
