#!/bin/bash

path=/opt/.services/executables/user_control/user.txt


read -r line < $path 

remote-viewer vnc://$line:5900
