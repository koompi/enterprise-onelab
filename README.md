# ONELAB

This is a project dedicated to One School Once Lab 

## Implementation

To begin, you need to install some various packages to work for vm

```bash
sudo pacman -S  virt-install qemu libguestfs vde2 spice bridge-utils virt-viewer ebtables iptables dmidecode
```

Next we need to add some modules

```bash
sudo modprobe virtio-net
sudo modprobe virtio-blk
sudo modprobe virtio-scsi
sudo modprobe virtio-balloon
sudo modprobe tun
```

Afterward we can start the related service, and perhaps enable it for starting at boot


```bash
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
sudo virsh net-start default
sudo virsh net-autostart default
```

Next we need to add the selected users to group kvm and change some permission here and there

```bash
sudo chgrp $USER /var/lib/libvirt
sudo chmod 775 /var/lib/libvirt
sudo chmod -aG kvm $USER
```

If the $USER is currently log in, it must be logged out.

Now we can start install some vm

```bash
virt-install --name test1 --ram 1024 --vcpu 1 --cdrom=/var/lib/libvirt/boot/pi-enterprise_server_0.1_Beta.iso --disk path=/var/lib/libvirt/images/test1.qcow2,size=8,format=qcow2,bus=virtio --graphics spice,listen=0.0.0.0,password=pass01 --noautoconsole --os-type=linux --os-variant=generic
```

So a machine that goes by the name of "test1" with 1Gigabits of Ram, 8Gigabits of Storage and 1 CPU counts will be created and saved at "/var/lib/libvirt/images/test1.qcow2" and it can be access via spice at localhost or $IP of the machine at port 5900 (Because it is the first machine that got started) and the password will be "pass01"


## Management

To start the vm

```bash
virsh start $MACHINE
```

To stop the vm

```bash
virsh destroy $MACHINE
```

To suspend/freeze the vm

```bash
virsh suspend $MACHINE
```

To continue its operation

```bash
virsh resume $MACHINE
```


