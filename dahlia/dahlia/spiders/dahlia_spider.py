import scrapy

from dahlia.items import DahliaItem

class DahliaSpider(scrapy.Spider):
	name = "dahlia"
	allowed_domains = ["johnnyseeds.com"]
	start_urls = [
	"http://www.johnnyseeds.com/v-9-greenhouse-performer.aspx?categoryid=1&pagesize=15&list=1&pagenum=9"
	]

	def parse(self, response):
		for sel in response.xpath('//div[@class="productResultInfo"]'):
			item = DahliaItem()
			item['name'] = sel.xpath('a/span[@class="nameCAT"]/text()').extract()
			item['extendedName'] = sel.xpath('a/span[@class="extendednameCAT"]/text()').extract()
			item['identification'] = sel.xpath('h1/text()').extract()
			item['description'] = sel.xpath('div[@class="productResultDesc"]/div/text()').extract()

			yield item

	# def parse(self, response):
	# 	filename = response.url.split("/")[-2] + '.html'
	# 	with open(filename, 'wb') as f:
	# 		f.write(response.body)


# productResultInfo

# for sel in response.xpath('//div[@id="productResultInfo"]/productResult/productResultInfo'):
