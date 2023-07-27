import scrapy
from scrapy.crawler import CrawlerProcess

print('''
 _____ _            ______ _ _             _____                 _           
|_   _| |           | ___ (_) |           /  ___|               | |          
  | | | |_ ___ _   _| |_/ /_| |_ ___ _   _\ `--. _ __  _   _  __| | ___ _ __ 
  | | | __/ __| | | | ___ \ | __/ __| | | |`--. \ '_ \| | | |/ _` |/ _ \ '__|
 _| |_| |_\__ \ |_| | |_/ / | |_\__ \ |_| /\__/ / |_) | |_| | (_| |  __/ |   
 \___/ \__|___/\__, \____/|_|\__|___/\__, \____/| .__/ \__, |\__,_|\___|_|   
                __/ |                 __/ |     | |     __/ |                
               |___/                 |___/      |_|    |___/                 

                                                            @Cont3nted :D
''')

user_input = input("Enter a url: ")

class ItsyBitsySpider(scrapy.Spider):
    name = 'ItsyBitstSpider'

    def start_requests(self):
        url = user_input
        yield scrapy.Request( url = url, callback = self.parse )
        print("Starting")

    def parse(self, response):
        response.xpath('./*').extract()
        #simple example: write out html html
        print(response)
        html_file = "./extracted_data/extracted.html"
        with open(html_file, 'wb') as fout:
            fout.write(response.body)

#Intiate the CrawlerProcess
process = CrawlerProcess()
#Tell the process which spider to use
process.crawl(ItsyBitsySpider)
#Start the crawling process
process.start()
