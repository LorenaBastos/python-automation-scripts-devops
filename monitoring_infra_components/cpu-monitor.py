import psutil
import smtplib, ssl
import os

# CPU Usage in 4 seconds
#print("CPU Usage:", psutil.cpu_percent(4), "%")

# This function sends an alert if CPU usage exceeds a threshold within a specified time interval.
""" def high_cpu_usage(cpu_usage, threshold):
    if cpu_usage > threshold:
        print("Alert: CPU usage is high!")
    else:
        print("CPU usage is normal.") """



def high_cpu_alert_email(smtp_server, port, sender_email, receiver_email, message, password,cpu_usage, threshold):
    if cpu_usage > threshold:
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
    cpu_usage = psutil.cpu_percent(interval=1)
    threshold = 80  # Set your threshold here
    print(f"CPU Usage: {cpu_usage}%")

    # Email alert configuration
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.environ['sender_email_address']  
    receiver_email = os.environ['receiver_email_address'] 
    password = input(os.environ['email_password'])  # Get password from environment variable
    message = """\
    Subject: Hi there

    Alert: CPU usage is high!"""
    high_cpu_alert_email(smtp_server, port, sender_email, receiver_email, message, password,cpu_usage, threshold)