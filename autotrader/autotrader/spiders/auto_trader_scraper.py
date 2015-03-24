from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from autotrader.items import CarItem

class AutoTraderScraper(BaseSpider):
    name = "auto_trader"
    allowed_domains = ["www.autotrader.co.uk"]
    start_urls = [
        "http://www.autotrader.co.uk/search/used/cars/bmw/x1/postcode/eh74nl/radius/1500/sort/default/onesearchad/used%2Cnearlynew%2Cnew"
    ]

    def parse(self, response):
        response_html = HtmlXPathSelector(response)
  
        cars = []        
        result_content_list = response_html.select('//ul[@class="search-page__results"]/li[@class="search-page__result"]/article/div[@class="search-result__r1"]/div[@class="search-result__content"]')
        
        for index, result in enumerate(result_content_list):
            car = CarItem()                
            
            car_title = result.select('./div[@class="search-result__titles"]/h1[@class="search-result__title"]/a/text()')
            car_cost = result.select('./div[@class="search-result__titles"]/div[@class="search-result__price"]/text()')
            engine_size = result.select('./ul[@class="search-result__attributes"]/li[5]/text()')
            car_age = result.select('./ul[@class="search-result__attributes"]/li[1]/text()')
            
            car["title"] = car_title.extract()
            car["cost"] = car_cost.re("[\d,\.]+")
            car["engine"] = engine_size.extract()
            car["age"] = car_age.extract()
            
            cars.append(car)
        return cars
        