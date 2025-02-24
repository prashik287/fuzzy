import pprint

import requests
from bs4 import BeautifulSoup


class Fuzzer:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.target = f"http://{self.host}:{self.port}"

    def display_target(self):
        pprint.pprint(f"Target Set {self.target}")

    def start_fuzz(self):
        endpoints = ['admin','/api/user/register','/api/user/login','/api/user/jd','/api/user/info']
        for endpoint in endpoints:
            response = requests.get(f'{self.target}/{endpoint}/')
            pprint.pprint(response)
            if response.status_code == 403:
                pprint.pprint(f"Endpoint {endpoint} is Authenticated")
            if response.status_code == 200:
                pprint.pprint(f"Endpoint {endpoint} is Accessible")
            if response.status_code == 404:
                pprint.pprint(f"Endpoint {endpoint} is Not Found")
            else:
                pprint.pprint(f"Response : {response.status_code}")
                pprint.pprint(f"Endpoint {endpoint} is Not Accessible")







def main():
    host=input("Ip address: ")
    port=int(input("Port: "))
    fuzzer = Fuzzer(host,port)
    fuzzer.display_target()
    fuzzer.start_fuzz()




