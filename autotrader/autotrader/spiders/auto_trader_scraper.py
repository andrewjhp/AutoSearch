from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from autotrader.items import CarItem

class AutoTraderScraper(BaseSpider):
    name = "auto_trader"
    allowed_domains = ["www.autotrader.co.uk"]
    start_urls = [
        "http://www.autotrader.co.uk/search/used/cars/postcode/eh74nl/radius/1500/onesearchad/used%2Cnearlynew%2Cnew/quicksearch/true"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        cars = []        
        results = hxs.select('//ul[@class="search-page__results"]/li/article/div[@class="search-result__r1"]/div[@class="search-result__content"]')
                
        for index, result in enumerate(results):
            #print results
            car = CarItem()
            
            car_title = result.select('./div[@class="search-result__titles"]/h1[@class="search-result__title"]/a/text()')
            #car_attrs = result.select('./ul[@class="search-result__attributes"]/li').extract()
            
            #print car_title
            print car_title
            car["type"] = car_title
            #car["model"] = car_attrs[1]
            
            cars.append(car)
        
        return cars
        
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
