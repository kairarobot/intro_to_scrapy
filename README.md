#Introduction to Web Scraping using Scrapy
PyGotham 2016 Talk Proposal

## Description:
Have you wanted to grab data from websites and automatically categorize it into a formatted list? Or possibly you don't want to go through the trouble of registering for API keys and just want data straight out of a web page without having to copy and paste several times? This is an introduction to web scraping and we will cover building bots through Scrapy to crawl a few sample web pages and have it extract information that we want. 

Even if you have never used a web crawler before or are not familiar with Python, come learn how to scrape data from webpages. We’ll break down the steps in creating your own bot, and you’ll start your way into web scraping!  

##Abstract:
This is a live-coding session and everyone is welcome to code along. We will install Scrapy and use Sublime Text to edit and write our code. Bring your laptops! We’ll work through a web crawler I’ve built for scraping product IDs and names from an online seed catalogue. After a little introduction, we will start building a bot that scrapes all the species of pine trees. You’ll have a whole collection of conifers by the end.

The concepts in this session will make a little more sense if you have programmed before, but even if you don’t, that’s okay. You will get the most out of it if you review the code and build another web crawler bot afterwards. The material will include object-oriented programming, parsing HTML through XPath, HTML and CSS structure, and exporting CSV files.


##Outline
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
	+ http://www.forestryimages.org/browse/catsubject.cfm?cat=58

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

####III. Example of a Scrapy bot (Total: 5 minutes)

#####A. Running the bot (1 minute)
* I made a bot that extracted seed names and product identification numbers from [Johnny Seeds](http://www.johnnyseeds.com/v-9-greenhouse-performer.aspx?categoryid=1&source=W_veg_ddShopBy#)
* I did not configure additional changes in the settings.py file. I stayed with the default.

```
BOT_NAME = 'dahlia'

SPIDER_MODULES = ['dahlia.spiders']
NEWSPIDER_MODULE = 'dahlia.spiders'
```

```
$ scrapy crawl [bot_name]
```
#####B.	Looking through the code (4 minutes)

####IV. Building a Scrapy bot to extract conifer plants (10 minutes)

#####A. Creating a new project

#####B. Writing a model to structure data properties

#####C. Extracting HTML elements using XPath and CSS selectors

#####D. Running the bot we built and exporting the data as a csv file

