# logger.py
import logging

def setup_logger():
    logging.basicConfig(
        filename="system_monitor.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
