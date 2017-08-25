import scrapy


class SubtitlesSpider(scrapy.Spider):
    name = "subtitles"
    output_dir = "output/"
    page_num = 876
    url_templ = 'http://subs.com.ru/list.php?c=rus&d=%s'

    def start_requests(self):
        page_file = self.output_dir + 'page_file'
        for i in range(1, self.page_num+1):
            url = self.url_templ % i
            yield scrapy.Request(url=url, callback=self.parse)
            with open(page_file, "wt") as f:
                f.write(str(i))

    def parse(self, response):

        for href in response.css('tr.odd>td>div>a::attr(href)').extract():
            self.log('---------------------------------------------------------------------------------')
            url = response.urljoin(href) + '&a=dl'
            yield scrapy.Request(url, callback=self.save_subtitle)

    def save_subtitle(self, response):
        self.log('*******************************************************************************')
        with open(self.output_dir + response.url.split('/')[-1], "wb") as f:
            f.write(response.body)