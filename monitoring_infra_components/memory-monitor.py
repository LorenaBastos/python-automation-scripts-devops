import os
import ssl
import psutil
import smtplib

# Memory Usage
""" memory = psutil.virtual_memory()
print("Memory Usage:")
print(f"Total: {memory.total / (1024 ** 3):.2f} GB")
print(f"Available: {memory.available / (1024 ** 3):.2f} GB")
print(f"Used: {memory.used / (1024 ** 3):.2f} GB")
print(f"Percentage: {memory.percent}%") """

# This script monitors the memory usage of the system and sends an alert if it exceeds a specified threshold.

""" def send_alert(memory_usage, threshold):
    if memory_usage > threshold:
        print("Alert: Memory usage is high!")
    else:
        print("Memory usage is normal.") """
    


def high_memory_alert_email(smtp_server, port, sender_email, receiver_email, message, password,memory_usage, threshold):
    if memory_usage > threshold:
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
    
    # Memory Usage metrics
    threshold = 80
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    print(f"Memory Usage: {memory_usage}%")

    # Email alert configuration
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.environ['sender_email_address']  
    receiver_email = os.environ['receiver_email_address'] 
    password = input(os.environ['email_password'])  # Get password from environment variable
    message = """\
    Subject: Hi there

    Alert: Memory usage is high!"""
    high_memory_alert_email(smtp_server, port, sender_email, receiver_email, message, password,memory_usage, threshold)



