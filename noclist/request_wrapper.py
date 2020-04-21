import requests
import sys
from requests.adapters import HTTPAdapter
import time

class RequestWrapper():
    DEFAULT_TIMEOUT = 5
    MAX_RETRIES = 3
    
    def __init__(self, base_url = "http://localhost:8888", timeout = DEFAULT_TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
    
    """
    Get request with exponential back-off retry (sleeps 1, 2, 4... seconds) with at max 2 retries for 3 attempts
    """
    def get_with_retry(self, endpoint, headers=None):
        result = ""
        for attempts in range(self.MAX_RETRIES):
            try:
                result = requests.get(url=self.base_url + endpoint, headers= headers)
                if result.status_code == 200:
                    break
                result.raise_for_status()
            except (requests.exceptions.RequestException, ConnectionResetError) as e:
                if attempts == self.MAX_RETRIES -1 : 
                    print(e, file=sys.stderr)
                    raise SystemExit(1) from None
                else:
                    time.sleep(2 ** (attempts-1))
                    continue
        return result
            