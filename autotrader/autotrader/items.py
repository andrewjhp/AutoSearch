# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CarItem(Item):
    # define the fields for your item here like:
    title = Field()
    engine = Field()
    age = Field()
    cost = Field()
    mileage = Field() #[CM] added mileage, gearbox and fuel
    gearbox = Field()
    fuel = Field()
