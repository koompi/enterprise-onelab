# Install GUI for Koompi lab Rpi4

### **``Warning:``** This all must be done **in order only** for it to work

## Install GUI

### Install an AUR Helper

```console
git clone https://github.com/koompi/enterprise-onelab.git
git clone https://aur.archlinux.org/yay.git
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

## Create a new enviroment user

### Create User

```console
useradd -mg users -G wheel,power,storage,network -s /bin/bash $USER
```

### Set Password

```console
passwd $USERS
```

## Remove old users

in order to completely start fresh, i would recommand to remove old user

```console
userdel alarm
```

## Make Pi monitor fullscreen

```console
echo -e "disable_overscan=1
hdmi_drive=2
dtparam=audio=on" >> /boot/config.txt
```

## Reboot to new system

```console
reboot
```

## Extra installation

```console
yay -S kde-cli-tools kwinplasma-workspace lxqt-kcm-integration-extra-git
```

## Log out and log back in

You may use the interface to log out or force restart the login service

```console
sudo systemctl restart lightdm
```