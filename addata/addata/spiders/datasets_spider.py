import scrapy


test_number = 1 

page_urls = f'https://addata.gov.ae/search/type/dataset?sort_by=changed&page=0%2C{test_number}'

class DatasetsSpider(scrapy.Spider):
    name = "data"

    def start_requests(self):
        urls = [
            'https://addata.gov.ae/search/type/dataset'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for section in response.xpath('/html/body/div[3]/div/div/section/div/div/div/div/div[2]/div/div/div/div/div[4]/div'):


            test_element = """
            
            <div class="views-row views-row-1 views-row-odd views-row-first">
    <article class="node-search-result row" xmlns="https://www.w3.org/1999/html">
  <div class="col-md-2 col-lg-1 col-xs-2 icon-container">
    <span class="icon-dkan facet-icon icon-dkan-dataset"></span>  </div>
  <div class="col-md-10 col-lg-11 col-xs-10 search-result search-result-dataset">
    <h2 class="node-title"><a href="/dataset/instant-trade-licenses-abu-dhabi-2021" title="Instant Trade Licenses in Abu Dhabi 2021">Instant Trade Licenses in Abu Dhabi 2021</a></h2>
          <div class="group-membership"><a href="/search/og_group_ref/2533/type/dataset?language=">Department of Economic Development</a></div>
        <div class="field field-name-field-topic field-type-taxonomy-term-reference field-label-hidden"><div class="field-items"><div class="field-item even"><div class="field field-name-field-topic-icon field-type-font-icon-select-icon field-label-above"><div class="field-items"><div class="field-item even"><span class="font-icon-select-1 font-icon-select-1-e91e"></span></div></div></div><a class="name" href="https://addata.gov.ae/search/field_topic/economy-2855">Economy</a></div></div></div>    <ul class="dataset-list"></ul>
          <div class="node-description"> <p>The immediate license Abu Dhabi to facilitate the practice of business 
without the required approvals.
 </p></div>
        <div class="data-and-resources"><div class="form-item form-type-item form-group">
  <div class="item-list"><ul class="resource-list clearfix"><li class="first last"><a href="/dataset/instant-trade-licenses-abu-dhabi-2021" class="label" title="Resources: Instant Trade Licenses in Abu Dhabi 2021" data-format="excel">excel</a></li>
</ul></div>
</div>
</div>      </div>
</article>

  </div>
            
            """

            print(section)




