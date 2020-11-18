# Install OS on Raspberry

## Preboot Operations

First, plug a new memory card in to the a linux laptop. Then, we must run this command to find what is the name of the new memory card that was just plugged in.

**Note: The Memory Card Must Be At least 32GB**

```console
sudo fdisk -l
```

You should see similar output to below

```console
Disk /dev/sda: XXX.XX GiB, XXXXXXXXXXX bytes, XXXXXXXXXX sectors
Disk model: XXX            
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: XXXXXX-XXXXXXX-XXXXXXXX

Device        Start       End   Sectors   Size Type
/dev/sda1      2048   XXXXXXX   XXXXXXX   XXXX Microsoft basic data
/dev/sda2   XXXXXXX  XXXXXXXX  XXXXXXXX     XX Linux swap
/dev/sda3  XXXXXXXX XXXXXXXXX XXXXXXXXX XXX.XX Linux filesystem


Disk /dev/sdb: 29.02 GiB, XXXXXXXXX bytes, XXXXXXXXX sectors
Disk model: Storage Device  
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: XXXXXXXXXXX
```

As we can see, the disk that is used by the current OS is **sda** and the newly plugged in memory card is **sdb**

Once the ID of the new SD Card is known, then we start to create the new partiton.

```console
git clone https://github.com/koompi/enterprise-onelab.git --depth 1
sudo sfdisk /dev/sdb < enterprise-onelab/script/partitionscript
```

Then, we start mounting operation

```console
sudo su
```
```console
sudo mkfs.vfat -F32 /dev/sdb1
sudo mkswap /dev/sdb3
sudo mkfs.ext4 -F /dev/sdb2
sudo chown $(id -u -n) /mnt -R
sudo chmod 770 /mnt -R
mkdir -p /mnt/boot
mkdir -p /mnt/root
sudo mount /dev/sdb1 /mnt/boot
sudo mount /dev/sdb2 /mnt/root
```

## Install Operations

First, we must download the OS from KOOMPI Repo

```console
curl -o KoompiARM-10-11-2020.tar.gz https://repo.koompi.org/arm-iso/KoompiARM-10-11-2020.tar.gz
```
```console
curl -o boot.tar.gz https://repo.koompi.org/arm-iso/boot.tar.gz
```

***Should there be any error, just simply rerun the command again***

Then, we can start install the OS on to our SD Card

```console
sudo tar -xzvpf $(pwd)/KoompiARM-10-11-2020.tar.gz -C /mnt/root
sudo tar -xzvpf $(pwd)/boot.tar.gz -C /mnt/boot
sudo sync
```

Then, we can unmount it and it should be ready to go

```console
sudo umount /dev/sdb1
sudo umount /dev/sdb2
```