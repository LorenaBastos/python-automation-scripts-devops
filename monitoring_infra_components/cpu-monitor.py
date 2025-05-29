import psutil

# CPU Usage in 4 seconds
#print("CPU Usage:", psutil.cpu_percent(4), "%")


# This function sends an alert if CPU usage exceeds a threshold within a specified time interval.
def send_alert(cpu_usage, threshold):
    if cpu_usage > threshold:
        print("Alert: CPU usage is high!")
    else:
        print("CPU usage is normal.")


if __name__ == "__main__":
    
    cpu_usage = psutil.cpu_percent(interval=1)
    threshold = 80  # Set your threshold here
    print(f"CPU Usage: {cpu_usage}%")
    send_alert(cpu_usage, threshold)