#!/usr/local/bin/python3
# coding:utf-8
import os

# rsync在shell脚本中执行, --exclude不生效
rsync_cmd='rsync -avz --delete --exclude-from "/home/airp/Documents/scripts/rsync/exclude.txt" /home/airp/Documents/upload/ 192.168.0.221::source/'
rsync_cmd_2='rsync -avz --delete --exclude-from "/home/airp/Documents/scripts/rsync/exclude.txt" /home/airp/Documents/upload/ 13.200.189.91::source/'

res = os.system(rsync_cmd)
print(res)
res_2 = os.system(rsync_cmd_2)
print(res_2)

