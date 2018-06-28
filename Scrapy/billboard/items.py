import scrapy


class BillboardItem(scrapy.Item):
	song = scrapy.Field()
	artist = scrapy.Field()
	year =scrapy.Field()
	release = scrapy.Field()
	format= scrapy.Field()
	recorded= scrapy.Field()
	genre = scrapy.Field()
	length =  scrapy.Field()
	songwriter= scrapy.Field()
	producer= scrapy.Field()

