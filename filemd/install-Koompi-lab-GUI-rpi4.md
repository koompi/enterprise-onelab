# Install GUI for Koompi lab Rpi4
## 1. Prepare SD Card and install

on linux PC:

```console 
lsblk
sudo fdisk /dev/sd**X**
```
### clear partitions on the drive (**o**)

### create first partition (**n**, **p**, **1**, **enter**, **+100M**, **t**, **c**)

### create second partition (**n**, **p**, **2**, **enter**, **enter**), then write and exit (**w**)

```console
sudo mkfs.vfat /dev/sdX1
sudo mkfs.ext4 /dev/sdX2
```

### make folder to mount partitions
```console
mkdir /mnt/boot/
mkdir /mnt/root/
sudo mount /dev/sdx1 /mnt/boot/
sudo mount /dev/sdx2 /mnt/root/
````
### download and install arch
```console
wget http://archlinuxarm.org/os/ArchLinuxARM-rpi-4-latest.tar.gz
sudo su
tar zxvf /location/of/file/ArchLinuxARM-rpi-4-latest.tar.gz -C /mnt/root
mv /mnt/root/boot/* /mnt/boot
sync
```
## 2. Init Process

On Raspberry Pi:

login: ``root``

password: ``root``

### set up wifi with netctl

```console
wifi-menu -o
```

### set up necessary packkit

```console
pacman-key --init
pacman-key --populate archlinuxarm
pacman -Sy archlinux-keyring sudo networkmanager tcl python git glibc --overwrite /usr/include/crypt.h --overwrite /usr/lib/libcrypt.so
echo -e 'alarm ALL=NOPASSWD: ALL' > /etc/sudoers.d/myOverrides
```

## 3. Install GUI

### install GUI

```console
sudo pacman -S xorg xorg-xinit mesa lightdm lightdm-gtk-greeter lxqt xf86-video-fbdev breeze-icons xf86-video-fbturbo-git base base-devel qt5-base qt5-declarative plasma-framework kwin fcitx fcitx-im kcm-fcitx kvantum-qt5 nm-connection-editor bluedevil networkmanager-qt ttf-khmer ttf-fira-sans ttf-droid firefox pulseaudio pulseaudio-bluetooth kwin xf86-video-qxl --needed
```

The above is the instalation from normal repository, but it isn't enough, so we need some more from AUR

```console
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
yay install nm-tray-git lxqt-kcm-integration-extra.git
```

### start the neccessary service

```console
sudo systemctl enable lightdm NetworkManager
```

### setup user GUI config 

```console
git clone https://github.com/koompi/onelab.git
tar zxf onelab/config/skel/skel.tar.gz -C /etc/skel/
sudo cp -r --no-target-directory onelab/config/wallpapers/. /usr/share/wallpapers/
sudo cp onelab/config/theme/lightdm-gtk-greeter.conf /etc/lightdm/
mkdir -p /etc/lightdm/lightdm.conf.d
echo -e "[SeatDefaults]
greeter-hide-users=true
greeter-show-manual-login=true
allow-guest=false" >> /etc/lightdm/lightdm.conf.d/50-my-custom-config.conf
```

### create a new enviroment user

```console
useradd -mg users -G wheel,power,storage,network -s /bin/bash $USER
```

### Remove old users

in order to completely start fresh, i would recommand to remove old user

```console
userdel alarm
```

### Make Pi monitor fullscreen

```console
echo -e "disable_overscan=1
hdmi_drive=2
dtparam=audio=on" >> /boot/config.txt
```

### Reboot to new system

```console
reboot
```