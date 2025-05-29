# Script to monitor disk usage
import psutil
import sys

def check_disk_usage(path):
    disk = psutil.disk_usage(path)
    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)
    percent_used = disk.percent

    print(f"Total: {total_gb:.2f} GB")
    print(f"Used: {used_gb:.2f} GB")
    print(f"Free: {free_gb:.2f} GB")
    print(f"Percent Used: {percent_used:.1f}%")


usage = check_disk_usage(sys.argv[0])