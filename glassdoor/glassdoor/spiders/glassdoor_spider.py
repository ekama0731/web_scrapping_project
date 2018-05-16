from scrapy import Spider, Request
from glassdoor.items import GlassdoorItem

# New York      1132348    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1132348&jobType=
# Los Angeles   1146821    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1146821&jobType=
# Chicago       1128808    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1128808&jobType=
# Houston       1140171    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1140171&jobType=
# Phoenix       1133904    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1133904&jobType=
# Philadelphia  1152672    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1152672&jobType=
# San Antonio   1140494    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1140494&jobType=
# San Diego     1147311    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1147311&jobType=
# Dallas        1139977    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1139977&jobType=
# San Jose      1147436    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1147436&jobType=
# Austin        1139761    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1139761&jobType=
# Jacksonville  1154093    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1154093&jobType=
# San Francisco 1147401    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1147401&jobType= 
# Indianapolis  1145013    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1145013&jobType=
# Boston        1154532    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1154532&jobType=
# Atlanta       1155583    https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&sc.keyword=&locT=C&locId=1155583&jobType=


class GlassdoorSpider(Spider):
    name = 'glassdoor_spider'
    allowed_urls = ['https://www.glassdoor.com/index.htm']
    # start_urls = ['https://www.glassdoor.com/Job/']
    
    #def parse(self, response):
    cities = ['new-york','los-angeles','chicago','houston','phoenix','philadelphia', 'san-antonia', 'san-diego', 'dallas', 'san-jose', 'austin', 'jacksonville', 'san-francisco', 'indianapolis','boston','atlanta']
    city_ids = [1132348,1146821,1128808,1140171,1133904,1152672,1140494,1147311,1139977,1147436,1139761,1154093,1147401,1154532,1155583]
    print("SETTING UP URL")
    cities = list(zip(cities, city_ids))
    #This is ugly list comprehension, but hey, now I know double list comprehension!
    start_urls = [("https://www.glassdoor.com/Job/" + str(city[0]) +"-jobs-SRCH_IL.0," +str(len(city[0])) +"_IC" +str(city[1]) + "_IP" + str(i) +".htm") for city in cities for i in range(1,31)]

    def parse(self,response):
        print("="*50)
        job_url_id= response.xpath("//ul[@class='jlGrid hover']/li/@data-id").extract() #an example id: 2220873086
 
        links = ["https://www.glassdoor.com/job-listing/-JV_IC1146821_KO0,14_KE15,23.htm?jl=" + job_id for job_id in job_url_id]

        for url in links:
            yield Request(url, callback=self.parse_job_details)

    def parse_job_details(self, response):
        #job_salary = response.xpath...
        print("Starting Parsing on Job")
        job_title = response.xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/h2/text()').extract_first()    

        try:
            company_name = response.xpath('.//span[@class= "strong ib"]/text()').extract_first()[1:]
        except:
            company_name = None
        
        try:
            job_location = response.xpath('//span[@class="subtle ib"]/text()').extract_first()[3:]
        except:
            job_location = None

        try:
            rating = response.xpath('.//span[@class = "compactStars margRtSm"]/text()').extract_first()[1:]
        except:
            rating = None

        try:
            salary_estimate = response.xpath('//*[@id="salWrap"]/h2/text()').extract_first()[1:]
        except: 
            salary_estimate = None

        try:
            salary_low = response.xpath('//*[@id="salWrap"]/div/div[2]/div[1]/text()').extract_first()[1:]
            salary_high = response.xpath('//*[@id="salWrap"]/div/div[2]/div[2]/text()').extract_first()[1:]
        except: 
             salary_high = salary_low = None
        item=GlassdoorItem()
        item['job_title']=job_title
        item['company_name']=company_name
        item['job_location'] = job_location
        item['rating'] = rating
        item['salary_estimate']= salary_estimate
        item['salary_low']=salary_low
        item['salary_high']=salary_high


        employer_id = response.xpath('//*[@id="EmpBasicInfo"]/@data-emp-id').extract_first()
        employer_link = 'https://www.glassdoor.com/Job/overview/companyOverviewBasicInfoAjax.htm?employerId=' + str(employer_id) + '&title=+Overview&linkCompetitors=true'


        print("JOB PAGE DONE")
        yield Request(url= employer_link, callback=self.parse_company_details, meta={"job_title": job_title,
                                                                                "company_name": company_name,
                                                                                "job_location": job_location,
                                                                                "rating":rating,
                                                                                "salary_estimate":salary_estimate,
                                                                                "salary_low":salary_low,
                                                                                "salary_high":salary_high })


    def parse_company_details(self,response):
        print("START COMPANY DETAILS SCRAPING")
        job_title = response.meta['job_title']
        company_name = response.meta['company_name']
        job_location = response.meta['job_location']
        rating = response.meta['rating']
        salary_estimate = response.meta['salary_estimate']
        salary_low = response.meta['salary_low']
        salary_high = response.meta['salary_high']

        labels = response.xpath('//div[@class = "info flexbox row col-hh"]/div/label/text()').extract()
        values = response.xpath('//div[@class = "info flexbox row col-hh"]/div/span/text()').extract()
        info = list(map(str.strip, values))
        company_info = list(zip(labels,info))
        
        item=GlassdoorItem()
        item['job_title']=job_title
        item['company_name']=company_name
        item['job_location'] = job_location
        item['rating'] = rating
        item['salary_estimate']= salary_estimate
        item['salary_low']=salary_low
        item['salary_high']=salary_high
        item['company_info'] = company_info
        print("DONE SCRAPING DETAILS")
        yield item

