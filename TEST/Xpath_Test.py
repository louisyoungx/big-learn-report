import time
from scrapy import Selector


def parse():
    body = open('TEST.html').read()
    # 使用scrapy自身的Selector解析文本
    res = Selector(text=body)
    print( res.xpath("//td[@data-field='cardNo']//div/span/text()").extract() )


parse()




def example():
    item = []
    body = open('TEST.html').read()
    # 使用scrapy自身的Selector解析文本
    res = Selector(text=body)
    job = res.xpath("//div[@class='job-primary']")
    item['job_id'] = job.xpath(".//div[@class='primary-box']/@data-jobid").extract_first()
    item['job_name'] = job.xpath(".//span[@class='job-name']/a/text()").extract_first()
    item['job_href'] = job.xpath(".//div[@class='primary-box']/@href").extract_first()
    item['job_area'] = job.xpath(".//span[@class='job-area']/text()").extract_first()
    item['salary'] = job.xpath(".//span[@class='red']/text()").extract_first()
    job_limit = job.xpath(".//div[@class='job-limit clearfix']/p/text()").extract()
    if len(job_limit) == 3:
        item['work_daytime'] = job_limit[0]
        item['work_year'] = job_limit[1]
        item['edu'] = job_limit[2]
    else:
        item['work_daytime'] = "None"
        item['work_year'] = job_limit[0]
        item['edu'] = job_limit[1]
    item['company_name'] = job.xpath(".//div[@class='info-company']//h3[@class='name']/a/text()").extract_first()
    item['industry_field'] = job.xpath(
        ".//div[@class='info-company']//a[@class='false-link']/text()").extract_first()
    item['finance_stage'] = job.xpath(".//div[@class='info-company']//p/text()").extract()[0]
    item['company_size'] = job.xpath(".//div[@class='info-company']//p/text()").extract()[1]
    labels = job.xpath(".//div[@class='tags']//span/text()").extract()
    item['job_labels'] = ''
    for label in labels:
        item['job_labels'] = item['job_labels'] + '/' + str(label)

    welfares = job.xpath(".//div[@class='info-desc']/text()").extract_first()
    if welfares is not None:
        item['welfare'] = welfares.replace("，", "/")
    else:
        item['welfare'] = 'None'
