#!/bin/bash
declare -a arr=(
'sudo ntfs-3g /dev/sda3 /home/kai/mnt/win'
'sudo mount /dev/sda4 /home/kai/mnt/pho'
'sudo ntfs-3g /dev/sda5 /home/kai/mnt/aps'
'sudo umount /home/kai/mnt/win' 
'sudo umount /home/kai/mnt/aps'
'sudo umount /home/kai/mnt/pho')
if [ $# -eq 0 ]; then 
echo "win[0/3],pho[1/4],aps[2/4]]"
fi
while [ $# -gt 0 ]
do
exec ${arr[$1]}
done

