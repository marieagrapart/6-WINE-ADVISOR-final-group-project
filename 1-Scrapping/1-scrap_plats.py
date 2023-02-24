import os
import scrapy
import logging
import random

from scrapy.crawler import CrawlerProcess

# Récupération des hôtels
class QuotesSpider1(scrapy.Spider):
    name = "spider1"

    liste_urls = []
    
    for i in range(1,100):
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/creme/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/dessert-glace/{i}"),	
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/dessert-glace/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/tarte/{i}"),	        
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/tarte/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/plat-vegetarien/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/andouilette/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/abats/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/pates-riz-semoule/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/soupe/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/viande/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/oeufs/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/poisson/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/plat-vegetarien/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/autres-crudites/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/fruits-de-mer/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/terrine-pate/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/aperitif-dinatoire/{i}"),
        liste_urls.append(f"https://www.marmiton.org/recettes/index/categorie/bouchee-ou-amuse-bouche/{i}")

    start_urls = liste_urls 
    
    def parse(self, response):
        print(response)

        yield {
                "target" : response.css('h1.main-title::text').get(),
                "plat": response.css("h4.recipe-card__title::text").getall(), 
                "url": response.css("a.recipe-card-link::attr(href)").getall() 
                }
                                 
filename = "plats.json"

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