# How to Make Destop File for Icons

**```This is example with making a icon for Python IDLE```**

## Install dependency for IDLE

```console
yay -S tk --needed
```

## Clone from this repo

```console
git clone https://github.com/koompi/enterprise-onelab.git --depth 1
```


## Get into Sudo

```console
sudo su
```

## Copy Icons into Directory and Make a desktop file

```console
cd enterprise-onelab
sudo cp desktop-icons/pythonidle.png /usr/share/applications/
echo \
'[Desktop Entry]
Name=Python IDLE
Comment=Python IDE called IDLE
GenericName=Text Editor
Exec=/sbin/idle
Icon=/usr/share/applications/pythonidle.png
Type=Application
StartupNotify=false
StartupWMClass=code
Categories=Utility;TextEditor;Development;IDE;
MimeType=text/plain;inode/directory;
Actions=new-empty-window;
Keywords=idle;' > /usr/share/applications/python-idle.desktop
```
