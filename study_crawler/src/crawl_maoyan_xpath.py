'''
Created on Jul 29, 2019

@author: ekexigu
'''

import requests
import json
from requests.exceptions import RequestException
import time
from lxml import etree

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
    html = etree.HTML(text)
    index = html.xpath('//dd/i/text()')
    title = html.xpath('//dd/div/div/div/p[@class="name"]/a/text()')
    actor = html.xpath('//dd/div/div/div/p[@class="star"]/text()')
    time = html.xpath('//dd/div/div/div/p[@class="releasetime"]/text()')
    i_score = html.xpath('//dd/div/div/div/p[@class="score"]/i[@class="integer"]/text()')
    f_score = html.xpath('//dd/div/div/div/p[@class="score"]/i[@class="fraction"]/text()')
    
    for i in range(len(index)):
        yield {'index': index[i],
               'title': title[i],
               'actor': actor[i].strip()[3:],
               'time': time[i].strip()[5:15],
               'score': i_score[i] + f_score[i]}
           
def write_to_file(content):
    with open('C:\\Users\\ekexigu\\Desktop\\temp\\Crawl_Maoyan_Temp\\result_xpath.txt', 'a', encoding='utf-8') as f:
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