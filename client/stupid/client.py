import requests
import sys
import time


def repeat_api_request(url, requests_per_second=1):
    start_time = time.time()
    while True:
        request_api(url)
        time.sleep(1/requests_per_second)

def request_api(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print("request successful!")
    else:
        print("request failed!")

if __name__ == "__main__":
    url = sys.argv[1]
    rate = int(sys.argv[2])
    repeat_api_request(url, rate)
