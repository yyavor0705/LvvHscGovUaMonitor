import scrapy


class Monitor(scrapy.Spider):
    name = "hsc"

    def start_requests(self):
        url = 'https://equeue.hsc.gov.ua/api/queue/dict/days?branchId=O.1dbcb7f0-4268-4c30-b91b-21ff5bf8f428&jobId=fd46ea46-8869-4f85-9ea0-e4c314955dee'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        print("++++++++++++")
        print(response)
