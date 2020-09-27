# install-Koompi-lab-GUI-rpi4
## 1. Prepare SD Card and install

on linux PC:

```terminal 
lsblk
sudo fdisk /dev/sd**X**
```
### clear partitions on the drive (**o**)

### create first partition (**n**, **p**, **1**, **enter**, **+100M**, **t**, **c**)

### create second partition (**n**, **p**, **2**, **enter**, **enter**), then write and exit (**w**)

    sudo mkfs.vfat /dev/sdX1
    sudo mkfs.ext4 /dev/sdX2

### make folder to mount partitions

    mkdir /mnt/boot/
    mkdir /mnt/root/
    sudo mount /dev/sdx1 /mnt/boot/
    sudo mount /dev/sdx2 /mnt/root/

### download and install arch

    wget http://archlinuxarm.org/os/ArchLinuxARM-rpi-4-latest.tar.gz
    sudo su
    tar zxvf /location/of/file/ArchLinuxARM-rpi-4-latest.tar.gz -C /mnt/root
    mv /mnt/root/boot/* /mnt/boot
    sync

## 2. Init Process

On Raspberry Pi:

login: ``root``

password: ``root``

### set up wifi with netctl

```terminal
wifi-menu -o
```

### set up necessary packkit

```terminal
pacman-key --init
pacman-key --populate archlinuxarm
pacman -Sy archlinux-keyring sudo networkmanager tcl python git glibc --overwrite /usr/include/crypt.h --overwrite /usr/lib/libcrypt.so
echo -e 'alarm ALL=NOPASSWD: ALL' > /etc/sudoers.d/myOverrides
```

### install GUI

```terminal
sudo pacman -S xorg xorg-xinit mesa lightdm lightdm-gtk-greeter lxqt xf86-video-fbdev breeze-icons xf86-video-fbturbo-git base base-devel sddm qt5-base qt5-declarative plasma-framework kwin fcitx fcitx-im kcm-fcitx kvantum-qt5 nm-connection-editor bluedevil networkmanager-qt ttf-khmer ttf-fira-sans ttf-droid firefox pulseaudio pulseaudio-bluetooth kwin xf86-video-qxl --needed
```

### start the neccessary service

```terminal
sudo systemctl enable sddm NetworkManager
```

### setup user GUI config 

```terminal
git clone https://github.com/koompi/onelab.git
sudo cp -r --no-target-directory onelab/config/skel/. /etc/skel/
sudo cp -r --no-target-directory onelab/config/wallpapers/. /usr/share/wallpapers/
sudo cp onelab/config/theme/lightdm-gtk-greeter.conf /etc/lightdm/
```

### create a new enviroment user

```terminal
useradd -mg users -G wheel,power,storage,network -s /bin/bash $USER
```

### Remove old users

in order to completely start fresh, i would recommand to remove old user

```terminal
userdel alarm
```