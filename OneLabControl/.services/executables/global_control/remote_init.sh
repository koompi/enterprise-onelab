
#!/bin/bash

path=/opt/.services/remote_update/data.txt


read -r line < $path && ssh -f admin@192.168.0.$line "export DISPLAY=:0 && cd /opt/.client-onelab && sudo -S <<< 123 ./remote.sh && exit" && sleep 1 &&  remote-viewer vnc://192.168.0.$line:5900
