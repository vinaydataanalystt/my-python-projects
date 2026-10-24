# email_automation.py
import smtplib
import getpass
from email.message import EmailMessage

def send_email(sender, app_password, receiver, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, app_password)
        server.send_message(msg)
    print("Email sent successfully!")

if __name__ == "__main__":
    sender = input("Your Gmail: ")
    password = getpass.getpass("App password (hidden): ")
    receiver = input("Send to: ")
    subject = input("Subject: ")
    body = input("Message: ")

    try:
        send_email(sender, password, receiver, subject, body)
    except Exception as e:
        print("Failed to send:", e)