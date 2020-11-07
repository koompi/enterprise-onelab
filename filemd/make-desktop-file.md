# How to Make Destop File for Icons

**``This is example with making a icon for Python IDLE``**

## Install dependency for IDLE

```console
yay -S tk --needed
```

## Copy Icons into Directory

```console
cd enterprise-onelab
sudo cp desktop-icons/pythonidle.png /usr/share/applications/
```

## Create a desktop file

```console
sudo nano /usr/share/applications/python-idle.desktop
```

```console
[Desktop Entry]
Name=Python IDLE
Comment=Python IDE called IDLE
GenericName=Text Editor
Exec=/sbin/idle
Icon=/usr/local/applications/pythonidle.png
Type=Application
StartupNotify=false
StartupWMClass=code
Categories=Utility;TextEditor;Development;IDE;
MimeType=text/plain;inode/directory;
Actions=new-empty-window;
Keywords=idle;
```

## Reboot

```console
reboot
```