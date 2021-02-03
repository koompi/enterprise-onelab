#!/bin/bash

# Color variables
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo ">>> ${green}INSTALLING DEPENDENCIES"

sudo -S <<< 2152 pacman -S python-pyqt5

cp 'Link to Application.desktop'

echo ">>> ${green}MOVING FILES INTO OPERATIONAL LOCATIONS"

sudo -S <<< 2152 cp .services /opt
