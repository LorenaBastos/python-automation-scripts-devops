# health_check.py
import requests
 
 
def fetch_url():
    response = requests.get('http://www.ccxp.com.br')
    status_code = response.status_code
    response_time = response.elapsed.total_seconds()
    if status_code == 200 and response_time < 3:
        return print(f'The status code: {status_code}, Response time: {response_time}')
    else:
        return print(f'We are in trouble Huston')
    
if __name__ == "__main__":
    fetch_url()
 