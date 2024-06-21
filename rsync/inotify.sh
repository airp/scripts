#!/bin/bash

inotify_cmd="inotifywait -mrq -e modify,create,attrib,move,delete /home/airp/Documents/upload"

$inotify_cmd | while read directory event file
##while判断是否接收到监控记录
do
    if [ $(pgrep rsync | wc -l) -le 0 ] ; then
        python3 /home/airp/Documents/scripts/rsync/inotify.py
    fi
done

