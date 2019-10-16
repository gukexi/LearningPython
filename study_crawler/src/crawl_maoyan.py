'''
Created on Jul 29, 2019

@author: ekexigu
'''

import requests  
import re
import json
from requests.exceptions import RequestException
import time

def get_one_page(url):  
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        response = requests.get(url, headers=headers)  
        if response.status_code == 200:  
            return response.text  
        return None
    except RequestException:
        return None  

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?name.*?movieId.*?>(.*?)</a>.*?star.*?\s+(.*?)\s+</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {'index': item[0],
               'title': item[1],
               'actor': item[2][3:] if len(item[2]) > 3 else '',
               'time': item[3][5:15] if len(item[3]) >5 else '',
               'score': item[4] + item[5]}
        
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        
def main(offset):  
    url = 'http://maoyan.com/board/4?offset=' + str(offset)  
    html = get_one_page(url)  
    for item in parse_one_page(html):
        write_to_file(item)
        
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)