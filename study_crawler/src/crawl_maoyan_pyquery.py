'''
Created on Jul 29, 2019

@author: ekexigu
'''

import requests
import json
from requests.exceptions import RequestException
import time
from pyquery import PyQuery

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
    html = PyQuery(text)
    
    sub_htmls = html('dd').items()
    
    index = list()
    title = list()
    actor = list()
    time = list()
    i_score = list()
    f_score = list()
    
    for sub_html in sub_htmls:
        index.append(sub_html('.board-index').text())
        title.append(sub_html('div div div .name a').text())
        actor.append(sub_html('div div div .star').text())
        time.append(sub_html('div div div .releasetime').text())
        i_score.append(sub_html('div div div .score .integer').text())
        f_score.append(sub_html('div div div .score .fraction').text())
    
    for i in range(len(index)):
        yield {'index': index[i],
               'title': title[i],
               'actor': actor[i].strip()[3:],
               'time': time[i].strip()[5:15],
               'score': i_score[i] + f_score[i]}
          
def write_to_file(content):
    with open('C:\\Users\\ekexigu\\Desktop\\temp\\Crawl_Maoyan_Temp\\result_pyquery.txt', 'a', encoding='utf-8') as f:
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