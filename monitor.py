# monitor.py
import time
import logging
import os

from metrics import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_network_usage
)
from alerts import check_alerts
from config import CHECK_INTERVAL
from logger import setup_logger

from session_tracker import (
    get_previous_boot_time,
    extract_previous_session_logs,
    save_current_boot_time
)

from mailer import send_log_email

def handle_previous_session():
    prev_boot = get_previous_boot_time()
    if prev_boot:
        logs = extract_previous_session_logs(prev_boot)
        send_log_email(logs)

    save_current_boot_time()

def main():
    setup_logger()
    logging.info("System Health Monitoring Agent started")

    handle_previous_session()

    while True:
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        disk = get_disk_usage()
        network = get_network_usage()

        logging.info(
            f"CPU={cpu}%, MEM={memory}%, DISK={disk}%, "
            f"SENT={network['bytes_sent']} bytes, "
            f"RECV={network['bytes_recv']} bytes"
        )

        alerts = check_alerts(cpu, memory, disk)

        for alert in alerts:
            print(alert)
            logging.warning(alert)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()

