import os
import psutil
from datetime import datetime

BOOT_FILE = "last_boot_time.txt"
LOG_FILE = "system_monitor.log"

def get_current_boot_time():
    return datetime.fromtimestamp(psutil.boot_time())

def save_current_boot_time():
    boot_time = get_current_boot_time()
    with open(BOOT_FILE, "w") as f:
        f.write(boot_time.isoformat())

def get_previous_boot_time():
    if not os.path.exists(BOOT_FILE):
        return None
    with open(BOOT_FILE, "r") as f:
        return datetime.fromisoformat(f.read().strip())

def extract_previous_session_logs(previous_boot_time):
    if not previous_boot_time or not os.path.exists(LOG_FILE):
        return ""

    logs = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                timestamp_str = line.split(" - ")[0]
                log_time = datetime.fromisoformat(timestamp_str)
                if log_time < previous_boot_time:
                    logs.append(line)
            except Exception:
                continue

    return "".join(logs)
