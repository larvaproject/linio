import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from liniocat.spiders.spider import LinioCat

if __name__ == '__main__':
	process = CrawlerProcess(get_project_settings())

	process.crawl(LinioCat)
	process.start()