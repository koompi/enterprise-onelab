#!/bin/bash

file="/opt/.services/executables/user_control/user.txt"

name=$(cat "$file")

ssh admin@$name "export DISPLAY=:0 && cd /opt/.client-onelab && ./disable.py"
