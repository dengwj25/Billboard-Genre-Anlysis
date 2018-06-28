from scrapy import Spider
from billboard.items import BillboardItem
from scrapy import Request

class BillboardSpider(Spider):
	name = "billboard_spider"
	allowed_urls = ["https://en.wikipedia.org/wiki/"]
	start_urls = ["https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"+ str(i) for i in range(2012,2013)]


	def parse(self,response):
		# rows = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr')
		rows = response.xpath('//table[1]/tr')
		
		for i in range(1,101):
			song = rows[i].xpath('./td[1]/a/text()').extract()	
			artist = rows[i].xpath('./td[2]/a/text()').extract()
			song_link = rows[i].xpath('./td[1]/a/@href').extract_first()
			song_link = 'https://en.wikipedia.org'+song_link
			year = response.xpath('//h1/text()').extract_first()[-4:]
			print(song_link)
			yield Request(song_link, callback = self.parse_song, meta={'song':song ,'artist':artist,'year':year})			


	def parse_song(self, response):
		song = response.meta['song']
		artist = response.meta['artist']
		year = response.meta['year']
		
		release = response.xpath('//tr[contains(th/text(),"Released")]/td/text()').extract()

		format = response.xpath('//tr[contains(th/text(),"Format")]/td//text()').extract()
		
		recorded= response.xpath('//tr[contains(th/text(),"Recorded")]/td/text()').extract()
		
		genre=	response.xpath('//tr[contains(th/a/text(),"Genre")]/td//text()').extract()
				
		length = response.xpath('//*[@id="mw-content-text"]/div/table[1]//tr[contains(th/text(),"Length")]//text()').extract()
				
		songwriter = response.xpath('//tr[contains(th/span/a/text(),"Songwriter(s)")]/td//text()').extract()
		
		producer= response.xpath('//tr[contains(th/span/a/text(),"Producer(s)")]/td//text()').extract()
		

		item = BillboardItem()
		item['song'] = song
		item['artist'] = artist
		item['year'] = year
		item['release'] = release
		item['format'] = format
		item['recorded'] =  recorded
		item['genre'] = genre 
		item['length'] = length
		item['songwriter'] =songwriter
		item['producer'] = producer
			
		yield item

