'''
Created on Jul 29, 2019

@author: ekexigu
'''

import requests
import json
from requests.exceptions import RequestException
import time
from bs4 import BeautifulSoup

def get_one_page(url):  
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        response = requests.get(url, headers=headers)  
        if response.status_code == 200:  
            return response.text  
        return None
    except RequestException:
        return None  

def parse_one_page(text):
    html = BeautifulSoup(text, 'lxml')
    
    index = html.find_all(name='i', class_='board-index')
    title = html.find_all(name='a', class_='image-link')
    actor = html.find_all(name='p', class_='star')
    time = html.find_all(name='p', class_='releasetime')
    i_score = html.find_all(name='i', class_='integer')
    f_score = html.find_all(name='i', class_='fraction')
    
    for i in range(len(index)):
        yield {'index': index[i].string,
               'title': title[i]['title'],
               'actor': actor[i].string.strip()[3:],
               'time': time[i].string.strip()[5:15],
               'score': i_score[i].string + f_score[i].string}
           
def write_to_file(content):
    with open('C:\\Users\\ekexigu\\Desktop\\temp\\Crawl_Maoyan_Temp\\result_bs.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        
def main(offset):  
    url = 'http://maoyan.com/board/4?offset=' + str(offset)  
    text = get_one_page(url)  
    for item in parse_one_page(text):
        write_to_file(item)
        
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)