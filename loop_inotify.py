#!/usr/bin/env python3
import fcntl
import os
import subprocess
import sys
import time
from threading import Timer

from inotify_simple import INotify, flags

LOCK_FILE = "/tmp/tmux_rename_inotify.lock"
FLAG_FILE = os.path.expanduser("~/.tmux_rename_flag")
DEBOUNCE_SECONDS = 0.3

# 防止重复运行
lock_fp = open(LOCK_FILE, "w")
try:
    fcntl.lockf(lock_fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    sys.exit(0)

pending = False


def trigger_rename():
    global pending
    if not pending:
        pending = True
        Timer(DEBOUNCE_SECONDS, fire).start()


def fire():
    global pending
    pending = False
    subprocess.Popen(
        [
            "tmux",
            "run-shell",
            "python3 ~/.config/tmux/plugins/tmux-window-name/scripts/rename_session_windows.py",
        ]
    )


def watch_file():
    os.makedirs(os.path.dirname(FLAG_FILE), exist_ok=True)
    if not os.path.exists(FLAG_FILE):
        with open(FLAG_FILE, "w"):
            pass

    inotify = INotify()
    watch_flags = flags.MODIFY | flags.CLOSE_WRITE
    wd = inotify.add_watch(FLAG_FILE, watch_flags)

    while True:
        for event in inotify.read():
            if event.mask & (flags.MODIFY | flags.CLOSE_WRITE):
                trigger_rename()


if __name__ == "__main__":
    try:
        watch_file()
    except KeyboardInterrupt:
        pass
