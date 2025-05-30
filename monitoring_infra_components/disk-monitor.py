# Script to monitor disk usage
import os
import smtplib
import ssl
import psutil
import sys

""" def check_disk_usage(path):
    disk = psutil.disk_usage(path)
    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)
    percent_used = disk.percent

    print(f"Total: {total_gb:.2f} GB")
    print(f"Used: {used_gb:.2f} GB")
    print(f"Free: {free_gb:.2f} GB")
    print(f"Percent Used: {percent_used:.1f}%") """


# usage = check_disk_usage(sys.argv[0])

def high_disk_usage_alert_email(smtp_server, port, sender_email, receiver_email, message, password,disk_usage, threshold):
    disk_percent_used = disk_usage.percent
    
    if disk_percent_used > threshold:
            # Create a secure SSL context
            context = ssl.create_default_context()
            # Connect to the SMTP server and send the email
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            print("Email sent successfully!")
    else:
        print("CPU usage is normal.")


if __name__ == "__main__":
    
    # CPU Usage metrics
    path = '/'  # Specify the path you want to monitor
    disk_usage = psutil.disk_usage(path)
    threshold = 80  # Set your threshold here
    # print(f"Disk Usage: {disk_usage.percent}%")

    # Email alert configuration
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.environ['sender_email_address']  
    receiver_email = os.environ['receiver_email_address'] 
    password = input(os.environ['email_password'])  # Get password from environment variable
    message = """\
    Subject: Hi there

    Alert: Disk usage is high!"""
    high_disk_usage_alert_email(smtp_server, port, sender_email, receiver_email, message, password,disk_usage, threshold)