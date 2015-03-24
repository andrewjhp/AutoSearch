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
        results = hxs.select('//ul[@class="search-page__results"]/li/article/div[@class="search-result__r1"]')
        
        for result in results:
            car = CarItem()
            car["type"] = "X1"
            car["model"] = "BMW"
            cars.append(car)
            print result
        
        return cars
        
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
