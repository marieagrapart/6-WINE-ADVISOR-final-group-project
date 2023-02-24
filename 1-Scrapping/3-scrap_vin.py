import os
import scrapy
import random
import logging

from scrapy.crawler import CrawlerProcess

# Récupération des hôtels
class QuotesSpider1(scrapy.Spider):
    name = "spider1"

    target = ["Fromages", "Viandes rouges", "Abats", "Apéritif", "Charcuteries", "Desserts", 
                "Fruits de mer", "Gibiers", "Légumes", "Pâtes", "Poissons", "Salades", "Lapin", 
                "Oeuf", "Viandes blanches", "Soupes", "Entrée"] 
    
    urls = []
    
    for i in target:
        urls.append(f"https://www.quelvin.com/rechacccrus.asp?Plat={i}&C=+Plat%2ENomSA+like+%27%25poulet%25%27&Lien=0&Tri=&Ordre=")
    
    start_urls = urls 
    
    def parse(self, response):
    
        keys = response.css('tr')
        print(keys)
        target = response.xpath('//*[@id="wrap"]/div/div/div/div/div[1]/section[2]/div[1]/h1/b/text()').get()
        
        yield {
                "target" : target,
                "vin" : response.xpath('//td[2]/a[2]/text()').getall(),
                "type" : response.xpath('//td[3]/img/@src').getall(),
                "region" : response.xpath('//td[4]/text()').getall()
                }
                                 
filename = "vins.json"

if filename in os.listdir():
        os.remove( filename)
        
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    'Chrome/97.0',
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


