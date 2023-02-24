import os
import scrapy
import logging
import random

import pandas as pd

from scrapy.crawler import CrawlerProcess

# Récupération des hôtels
class QuotesSpider1(scrapy.Spider):
    name = "spider1"

    plats = pd.read_json("plats.json")
    plats = plats.apply(pd.Series.explode)

    #file = pd.read_csv('data.csv')
    file = plats["url"]
    liste_url = [element for element in file]
    start_urls = liste_url
    
    def parse(self, response):
        print(response)
        
        yield {
                "plat" : response.css('h1.SHRD__sc-10plygc-0.itJBWW::text').get(),
                "recette" : response.xpath('/html/head/meta[18]').extract(),    
                }
                                 
filename = "recettes.json"

if filename in os.listdir():
        os.remove( filename)

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
]

process = CrawlerProcess(settings = {
    'USER_AGENT': user_agent_list[random.randint(0, len(user_agent_list)-1)],
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        filename : {"format": "json"},
    },
    "AUTOTHROTTLE_ENABLED": True
})

process.crawl(QuotesSpider1)
process.start()