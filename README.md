# 🖥️ System Health Monitoring Agent

## 📌 Project Overview

The **System Health Monitoring Agent** is a Linux-based monitoring service developed in **Python** that continuously tracks critical system resources such as **CPU usage, memory usage, and disk usage**.  
It runs as a **background service managed by systemd**, automatically starting on system boot, logging system health metrics, and generating alerts when predefined thresholds are exceeded.

This project demonstrates practical **system engineering and Linux service management skills**, including monitoring, logging, alerting, and daemonized application deployment.

---

## 🛠️ Technologies Used

- **Python 3** – Core programming language
- **psutil** – System resource monitoring
- **Linux** – Target operating system
- **systemd** – Service management and auto-start on boot
- **SMTP (optional)** – Email-based alert notifications
- **Git & GitHub** – Version control and collaboration
- **Python Virtual Environment (venv)** – Dependency isolation

---

## 🔁 Project Workflow

1. The system boots and `systemd` starts the monitoring service automatically.
2. The main monitoring loop executes at regular intervals.
3. System metrics (CPU, memory, disk usage) are collected.
4. Metrics are logged for auditing and troubleshooting.
5. Collected values are compared against configured thresholds.
6. If a threshold is exceeded:
   - An alert is generated
   - Optional email notification is sent
7. On system shutdown, the service receives a termination signal and exits gracefully after logging the shutdown event.

---

## 🧠 Architecture Overview

The project follows a **modular architecture with clear separation of concerns**.  
Each component is responsible for a specific task, making the system scalable and easy to maintain.

systemd
│
▼
monitor.py
│
├── metrics.py → Collects system metrics
├── alerts.py → Evaluates thresholds and raises alerts
├── logger.py → Handles logging
├── mailer.py → Sends email alerts (optional)
└── session_tracker.py → Tracks service start/stop events


## 📂 Repository Structure

```

System-Health-Monitoring-Agent/
├── alerts.py            # Alert evaluation logic
├── config.py            # Thresholds & configuration
├── logger.py            # Centralized logging setup
├── mailer.py            # Email notification logic
├── metrics.py           # System metrics collection
├── monitor.py           # Main monitoring loop
├── session_tracker.py   # Session start/stop tracking
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignore venv, logs, cache
└── README.md            # Project documentation

````

---


## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Srikumaran5557/System-Health-Monitoring-Agent.git
cd System-Health-Monitoring-Agent
```

### 2️⃣ Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Manually

```bash
python monitor.py
```

This is useful for testing before enabling the service.

---

## 🔄 Run on System Boot (systemd)

### 1️⃣ Create service file

```bash
sudo nano /etc/systemd/system/system-health-monitor.service
```

### 2️⃣ Service configuration

```ini
[Unit]
Description=System Health Monitoring Agent
After=network.target

[Service]
ExecStart=/opt/system-health-monitor/venv/bin/python /opt/system-health-monitor/monitor.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

### 3️⃣ Enable and start service

```bash
sudo systemctl daemon-reload
sudo systemctl enable system-health-monitor
sudo systemctl start system-health-monitor
```

### 4️⃣ Check service status

```bash
systemctl status system-health-monitor
```

---

## 🧾 Logging

* Runtime logs are written using Python logging
* systemd logs can be viewed using:

```bash
journalctl -u system-health-monitor
```

---

## 📬 Email Alerts (Optional)

The agent supports email notifications for alerts.

* Uses SMTP (e.g., Gmail App Password)
* Credentials should be stored securely (not hardcoded)
* Can be extended to support Slack / webhook alerts

---

