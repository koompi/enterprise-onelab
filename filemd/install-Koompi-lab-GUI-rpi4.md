# Install GUI for Koompi lab Rpi4

### **``Warning:``** This all must be done **in order only** for it to work

## Install GUI

### Install an AUR Helper

If you come straight from finish boot without yet looking at **``Boot Archlinuxarm on Raspberry PI4``** readme, consider do this. Else, skip.

```console
sudo pacman -S base-devel
```

## Now we can begin

```console
git clone https://github.com/koompi/enterprise-onelab.git --depth 1
git clone https://aur.archlinux.org/yay.git --depth 1
cd yay && makepkg -si && cd -
```

### Actual Install

```console
yay -S xorg xorg-xinit mesa lightdm lightdm-gtk-greeter lxqt xf86-video-fbdev breeze-icons xf86-video-fbturbo-git qt5-base qt5-declarative plasma-framework kwin fcitx fcitx-im kcm-fcitx kvantum-qt5 nm-connection-editor bluedevil networkmanager-qt ttf-khmer ttf-fira-sans ttf-droid firefox pulseaudio pulseaudio-bluetooth chromium xf86-video-qxl accountsservice konsole screen ark libreoffice-fresh nano-syntax-highlighting cmake qt5-tools nm-tray-git kvantum-theme-fluent-git --needed --noconfirm
```

### **``Note:``** From this parts, Linux needs root permission, either via **sudo** or **su** 

## Start the neccessary service

```console
sudo systemctl enable lightdm NetworkManager
```

## Setup user GUI config 

```console
sudo su
tar zxf enterprise-onelab/config/skel/skel.tar.gz -C /etc/skel/
sudo cp -r --no-target-directory enterprise-onelab/config/wallpapers/. /usr/share/wallpapers/
sudo cp enterprise-onelab/config/theme/lightdm-gtk-greeter.conf /etc/lightdm/
sudo cp enterprise-onelab/config/icons/* /usr/share/icons/
sudo mkdir -p /etc/lightdm/lightdm.conf.d
echo -e "[SeatDefaults]
greeter-hide-users=true
greeter-show-manual-login=true
allow-guest=false" >> /etc/lightdm/lightdm.conf.d/50-my-custom-config.conf
echo -e 'include "/usr/share/nano-syntax-highlighting/*.nanorc"' >> /etc/nanorc
echo -e '#!/bin/bash\nsleep 10\nkillall fcitx' > /usr/bin/kill-fcitx
sudo chmod +x /usr/bin/kill-fcitx
```

## Make Pi monitor fullscreen

```console
echo -e "disable_overscan=1
hdmi_drive=2
dtparam=audio=on" >> /boot/config.txt
```

## Create a new enviroment user

### Create User and Set Password

``Note:`` Please ONLY CHANGE the ``$USER`` to the actual name of the USER (admin, user01...)

```console
sudo useradd -mg users -G wheel,power,storage,network -s /bin/bash $USER
sudo passwd $USERS
```

### Remove old users

in order to completely start fresh, i would recommand to remove old user

```console
userdel alarm
```

## Reboot to new system

```console
reboot
```

``Note:`` This part is currently error (20/10/2020)

## Extra installation

```console
yay -S kde-cli-tools kwinplasma-workspace lxqt-kcm-integration-extra-git
```

## Log out and log back in

You may use the interface to log out or force restart the login service

```console
sudo systemctl restart lightdm
```
