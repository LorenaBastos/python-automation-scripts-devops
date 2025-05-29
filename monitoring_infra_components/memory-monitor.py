import psutil

# Memory Usage
""" memory = psutil.virtual_memory()
print("Memory Usage:")
print(f"Total: {memory.total / (1024 ** 3):.2f} GB")
print(f"Available: {memory.available / (1024 ** 3):.2f} GB")
print(f"Used: {memory.used / (1024 ** 3):.2f} GB")
print(f"Percentage: {memory.percent}%") """

# This script monitors the memory usage of the system and sends an alert if it exceeds a specified threshold.

def send_alert(memory_usage, threshold):
    if memory_usage > threshold:
        print("Alert: Memory usage is high!")
    else:
        print("Memory usage is normal.")

threshold = 80  # Set your threshold here
if __name__ == "__main__":
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    print(f"Memory Usage: {memory_usage}%")
    send_alert(memory_usage, threshold)
