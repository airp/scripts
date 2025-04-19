#!/bin/bash

# 设置同步目录
sync_dir="/home/airp/Sync/Library"

# 设置日志目录
log_dir="/home/airp/Sync/log"

# 设置OneDrive目录
od_dir="od:Library"

# 创建日志文件目录（如果不存在）
mkdir -p "$log_dir"

# 设置同步日志文件名，包含日期
rclone_log_file="$log_dir/rclone-$(date +%Y-%m-%d).log"

# 使用 rclone 同步本地目录到 OneDrive，设置同步日志文件名
rclone --config /home/airp/.config/rclone/rclone.conf sync "$sync_dir" "$od_dir" --log-file="$rclone_log_file"

# 检查同步是否成功
if [ $? -eq 0 ]; then
  # 在同步日志文件中记录同步完成信息
  echo "$(date +%Y-%m-%d_%H:%M:%S) - Sync to OneDrive completed successfully." >>"$rclone_log_file"
else
  # 在同步日志文件中记录同步失败信息
  echo "$(date +%Y-%m-%d_%H:%M:%S) - Sync to OneDrive failed." >>"$rclone_log_file"
fi
