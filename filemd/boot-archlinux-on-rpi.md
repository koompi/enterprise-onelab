# Boot Archlinuxarm on Raspberrypi 4
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

### make folder and mount partitions

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
cp -r /mnt/root/boot/* /mnt/boot
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
pacman -Sy archlinux-keyring base-devel bash-completion networkmanager dhclient tcl python git glibc --needed --overwrite /usr/include/crypt.h --overwrite /usr/lib/libcrypt.so
echo -e '%wheel ALL=(ALL) ALL' > /etc/sudoers.d/myOverrides
```

### Start the network service

```console
sudo systemctl enable NetworkManager
sudo systemctl start NetworkManager
```

### Stop Junk Service

```console
sudo systemctl disable systemd-networkd-wait-online.service
```

### `(Optional)` Connect to wifi with NetworkManager

```console
sudo nmcli device wifi connect "$WIFI_SSID" password $PASSWORD
```

In case you have already set up wifi and want to reconnect to it, use this

```console
sudo nmcli connect up "$WIFI_SSID"
```

#### **```Note:```** Do not drop the Double Quotes

