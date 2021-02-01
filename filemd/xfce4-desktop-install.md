# How to install XFCE4 Desktop on ArchLinux ARM

#### First you will need to have an pr-prepared archlinux-arm system ready to be used. You can see how to do that here

## ```NOTE:``` 
<p> Once you're connected to the internet you need to install 'sudo' so that we can continue the installation as normal user.</p>


#### Installing sudo
```# pacman -S sudo```


#### Adding default user 'alarm' to sudoer's group
```# echo 'alarm ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers```


#### Entering alarm
```# su alarm```


#### Installing all of the base dependencies
```$ sudo pacman -S base-devel --needed```


#### Installing the graphical UI and all related depenencies.
```$ sudo pacman -S xorg xorg-xinit mesa lightdm lightdm-gtk-greeter xf86-video-fbdev networkmanager xfce4 xfce4-goodies chromium --noconfirm --needed```


#### Enabling & starting all of the related services.
```$ sudo systemctl enable lightdm NetworkManager```


#### Now you're done. You'll want to reboot your machine and login to your new GUI
```$ reboot```

