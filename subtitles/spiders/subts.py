import scrapy
class SubtSpider(scrapy.Spider):
    name = '0subtitles'
    start_url = ['http://subs.com.ru/list.php?c=serials&d=1']
    def parse(self, response):
        print('-------------------start-------------------')
        for href in response.css('tr.odd>td>div>a::attr(href)').extract():
            url = response.urljoin(href)
            print(url)
            #yield {'url':url                 }