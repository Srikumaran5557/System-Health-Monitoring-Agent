# alerts.py
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD

def check_alerts(cpu, memory, disk):
    alerts = []

    if cpu > CPU_THRESHOLD:
        alerts.append(f"⚠️ High CPU usage: {cpu}%")

    if memory > MEMORY_THRESHOLD:
        alerts.append(f"⚠️ High Memory usage: {memory}%")

    if disk > DISK_THRESHOLD:
        alerts.append(f"⚠️ High Disk usage: {disk}%")

    return alerts
