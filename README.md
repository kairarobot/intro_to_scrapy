#Introduction to Web Scraping using Scrapy
PyGotham 2016 Talk Proposal

## Description:
Have you wanted to grab data from websites and automatically categorize it into a formatted list? Or maybe you want to opt out of registering for API keys and want data straight out of a web page? This is an introduction to web scraping and we will cover building bots through Scrapy to crawl a few sample web pages and have it extract information that we want. 

We’ll break down the steps in creating your own bot, and you’ll start your way into web scraping.

##Abstract:
This is a live-coding session and everyone is welcome to code along. We will install Scrapy and use Sublime Text to edit and write our code. Bring your laptops! After a little introduction, we will start building a bot that scrapes all the species of pine trees. You’ll have a whole collection of conifers by the end.

The concepts in this session will make a little more sense if you have programmed before, but even if you don’t, that’s okay. You will get the most out of it if you review the code and build another web crawler bot afterwards. The material will include object-oriented programming, parsing HTML through XPath, HTML and CSS structure, and exporting CSV files.


##Outline:
#####Length: 25 minutes

####I. Introduction to web scraping and installing Scrapy (Total: 5 minutes)

#####A. What is web scraping? (3 minutes)
* Web scraping is a technique used for extracting information from websites. Its main goal is to transform unstructured content from the web, usually in an HTML format, into a structured dataset that can be saved and examined in a spreadsheet or database. 
* Examples: human copy-and-paste, UNIX grep paired with regex, HTTP requests, computer vision web analyzers, or web-scraping softwares

#####B. Real world examples of web scraping (1 minute)
* Aggregating prices of video games: putting together a list of prices for products that you are interested in is a thrifty way to find the best deals
	+ http://www.gamestop.com/browse/games/xbox-one?nav=16k,28-xu0,131e0-ffff2418
* Grabbing the daily weather: researchers can integrate weather data into their observations without measuring the weather with hardware tools
	+ https://weather.com/weather/today/l/07601:4:US
* Acquiring a list of conifers: this is the information we will be extracting, which is a list of known conifers in the world
	+ http://www.greatplantpicks.org/plantlists/by_plant_type/conifer

#####C. Installing Scrapy (2 minutes)
* <em>Requirements:</em>
	+ Python 2.7 – Scrapy does not have full support of Python 3 at the moment, and installing Scrapy in 2.7 is the most stable
	+  pip – Python package management system
	+  lxml – Most Linux distribution already have lxml install
	+  OpenSSL – Comes preinstalled in all operating systems except Windows
```
	$ pip install Scrapy
```
* http://doc.scrapy.org/en/latest/intro/install.html


####II. Scrapy tools and basic structure (Total: 5 minutes)

#####A. What is Scrapy?	 (1 minutes)
* “Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival” (scrapy.org).
	
#####B. List of Scrapy command-line tool (2 minutes)
```
$ scrapy <command> -h 
```
* Global commands:
	+ startproject
	+ settings
	+ runspider
	+ shell
	+ fetch
	+ view
	+ version

* Project-only commands
	+ crawl
	+ check
	+ list
	+ edit
	+ parse
	+ genspider
	+ bench

#####C. Structure of Scrapy (2 minutes)

```
tutorial/
    scrapy.cfg            # project root directory 
    testing/              # Python module where the project is contained
        __init__.py
        items.py          # defines item objects for structured data
        pipelines.py      # performs an action over item objects
        settings.py       # allows for further component customization
        spiders/          # directory with your spiders
            __init__.py
```



####III. Building a Scrapy bot to extract conifer plants (Total: 15 minutes)

#####A. Creating a new project (1 minute)
* Go to a directory you prefer
* Create a new scrapy project
```
	$ scrapy startproject conifers
```

#####B. Defining field items in <b>items.py</b> (4 minutes)
* Check the website with conifers again: http://www.greatplantpicks.org/plantlists/by_plant_type/conifer
* Notice the names and scientific names? We'll extract those.
* Open up <b>items.py</b> 
* We will add <b>name</b>, <b>genus</b>, and <b>species</b> as fields to our item
```
	import scrapy
	
	class ConifersItem(scrapy.Item):
	    name = scrapy.Field()
	    genus = scrapy.Field()
	    species = scrapy.Field()
	    pass
```
#####C. Building the bot (4 minutes)
* Open up spiders directory and it contains no spiders at the moment
* We will add a spider now
* Create a new file and name it <b>conifers_spider.py</b> inside the spiders directory
* Let's clone the web page first
```
	import scrapy
	from conifers.items import ConifersItem
	
	class ConifersSpider(scrapy.Spider):
		name = "conifers"
		allowed_domains = ["greatplantpicks.org"]
		start_urls = [
		"http://www.greatplantpicks.org/plantlists/by_plant_type/conifer"]
	
		def parse(self, response):
			filename = response.url.split("/")[-2] + '.html'
			with open(filename, 'wb') as f:
				f.write(response.body)
```
* Save <b>conifers.py</b>
* Now, go back to the project root directory
* Run your bot
```
	$ scrapy crawl conifers
```
* You should now see <b>by_plant_type.html</b> in your directory
* Go back to <b>conifers_spider.py</b> and comment out the function parse


#####D. Extracting HTML elements using XPath and CSS selectors (4 minutes)
* We want to retrieve <em>only</em> the common names and scientific names
* To do this, we need to refer to create an item for each one and generate all these objects
* Add this new parse function with the old still commented
```
	def parse(self, response):
		for sel in response.xpath('//tbody/tr'):
			item = ConifersItem()
			item['name'] = sel.xpath('td[@class="common-name"]/a/text()').extract()
			item['genus'] = sel.xpath('td[@class="plantname"]/a/span[@class="genus"]/text()').extract()
			item['species'] = sel.xpath('td[@class="plantname"]/a/span[@class="species"]/text()').extract()
			yield item
```
* Go back to root project directory  and run the bot

#####E. Running the bot we built and exporting the data as a csv and JSON file (2 minutes)
* Let's export is as JSON file first
```
	$ scrapy crawl confiers -o trees_json.json
```
* Great, now let's export it as a csv!
```
	$ scrapy crawl confiers -o trees_csv.csv
```
* Now you have exracted all the conifers-- happy trails!

##Additional Notes:

#### Example of a Scrapy bot [dahlia](git clone https://github.com/Zovfreullia/intro_to_scrapy/tree/master/dahlia)

#####A. Running the bot 
* I made a bot that extracted seed names and product identification numbers from [Johnny Seeds](http://www.johnnyseeds.com/v-9-greenhouse-performer.aspx?categoryid=1&source=W_veg_ddShopBy#)
* Download the <b>bot</b>
```
	$ git clone https://github.com/Zovfreullia/intro_to_scrapy/tree/master/dahlia
```
* Go into the directory 
```
	$ cd dahlia
```
* Run the file
```
	$ scrapy crawl dahlia
```

#####B.	Looking through the code
* The <b>settings.py</b> is set to default
```
	BOT_NAME = 'dahlia'
	
	SPIDER_MODULES = ['dahlia.spiders']
	NEWSPIDER_MODULE = 'dahlia.spiders'
```
* <b>items.py</b> defines the fields for our items
```
	import scrapy
	
	class DahliaItem(scrapy.Item):
	    name = scrapy.Field()
	    extendedName = scrapy.Field()
	    identification = scrapy.Field()
	    description = scrapy.Field()
```
* <b>dahlia_spider.py</b> crawls through the web using fields from items.py
```
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
```
