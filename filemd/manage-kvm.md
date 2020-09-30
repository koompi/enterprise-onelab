# Manage KVM

## Management

To start the VM

```console
sudo virsh start $MACHINE
```

To stop the VM

```console
sudo virsh destroy $MACHINE
```

To suspend/freeze the VM

```console
sudo virsh suspend $MACHINE
```

To continue VM operation

```console
sudo virsh resume $MACHINE
```

To screenshot VM screen

```console
sudo virsh screenshot $MACHINE $LOCATION2SAVE
```

To change the cpu count of a machine

```consle
sudo virsh setvcpus --count $CPUCOUNT $MACHINE
```

To change the ram of a machine

```console
sudo virsh setmem $MACHINE $RAMCOUNT
```

To allow multiple spice session

```console
sudo virt-xml $MACHINE --edit --confirm --qemu-commandline 'env=SPICE_DEBUG_ALLOW_MC=1'
```

To allow image compression for over-network spice session for better performance

```console
sudo virt-xml $MACHINE --edit --confirm --graphics image.compression='auto_glz' --graphics zlib.compression='auto' --graphics clipboard.copypaste='yes'
sudo virt-xml $MACHINE --edit --confirm --graphics streaming.mode='filter'
```


