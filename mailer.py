import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

SENDER_EMAIL = "arulkumaran5557@gmail.com"
APP_PASSWORD = "lhdy tpkr vzgd freq"
RECEIVER_EMAIL = "srikumaran5557@gmail.com"

def send_log_email(log_content):
    if not log_content.strip():
        return

    msg = EmailMessage()
    msg["Subject"] = "System Health Log – Previous Session"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg.set_content(log_content)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
