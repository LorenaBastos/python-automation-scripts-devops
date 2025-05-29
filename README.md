# python-automation-scripts-devops
Repository for storing useful automation scripts made using Python language.

## :mag_right: System Health Monitor
A lightweight Python-based tool for monitoring CPU, memory, disk usage, and application health checks on your system. Ideal for local development environments, small servers, or as a foundational component for more extensive monitoring solutions.

 ## :rocket: Features
- CPU Usage: Track real-time CPU utilization.
- Memory Usage: Monitor RAM usage (total, used, free).
- Disk Usage: Keep an eye on disk space consumption for specified partitions.
- Health Checks: Configure custom HTTP/S endpoint checks to verify application availability.
- Simple & Lightweight: Built purely in Python with minimal dependencies.
- Extensible: Easy to modify and extend for additional monitoring needs.

## :computer: Installation

1. **Clone the repository:**

``` git clone https://github.com/your-username/system-health-monitor.git
cd system-health-monitor
```

2. **Create and activate a virtual environment (recommended):**

``` python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```
3. **Install dependencies:**

```
pip install -r requirements.txt
```