# Notes 
A guide on what to know before creating your spider.

  - [XPath](#h2-id%22xpath-416%22xpathh2)
    - [Slashes & Brackets](#slashes--brackets)
    - [Attributes](#attributes)
    - [Contains Function](#contains-function)
  - [CSS Locators](#css-locators)
    - [Attributes in CSS](#attributes-in-css)
  - [Selector](#selector)
    - [Selectors with CSS](#selectors-with-css)
    - [Text Extraction for XPath](#text-extraction-for-xpath)
    - [Text Extraction for CSS Locator](#text-extraction-for-css-locator)
  - [Response](#response-object)
  - [Creating a basic Spider](#creating-a-spider)
    - [Start Request](#start-requests-and-basic-parsing)
    - [Advancing Parsing](#advance-parsing)



## Goal
--------------------
The purpose of this notes is to help you understand the fundementals of scrapy
and ultimately scrap websites!

## What I have learn
-----------------------

* XPath
* Selector
* CSS Locators
  
 Disclaimer !!! These notes below are up to my personal understanding, if you spot anything wrong please let me know :)

## XPath
--------------
Before we start writing our spider program using scrapy. We need to understand what is XPaths and CSS locator.

What is XPath used for?

XPath is a query language use for selecting nodes from an XML document. In this case we use it to navigate HTML  elements before scrapping it.

 XPath can be used in other scrapping libraries too. e.g BeautifulSoup,Selenium and many more...

XPath Syntax:

### Slashes & Brackets

`xpath = '/html/body/div[3]'`



* Single foward-slash / used to move forward one generation. ( It's similar to navigatiing directories on your command line )
* Tag-names between slashes give direction to which element(s).
* Brackets [] after a tag name tell us which of the selected siblings to choose from.
  

`xpath = '//table'`

* Direct to all table elements within the entire HTML code:

Example of directing to a specific element 

`xpath = '/html/body/div[3]/table'`

* Direct to all table elements which are descendants of the 3rd child of the body element

The astericks character '*' is a wildcard character that indicates that we want to ignore the tag type.
  
### Attributes
* "@" represents attribute 
  * @class
  * @id
  * @href

Example of using attribute:

`xpath = '//div[@class="example-class"]'`

### Contains Function

Xpath Contains Notation:

**_contains(@attri-name,"string-expr")_**

The "contains" function searches the attributes of that specific attribute name and matches with those where the string is a sub-string of the full attribute.

You can use `XPath = './*' ` to direct to the children of the currently selected element

For more information on XPaths you can visit the websites below
https://www.w3schools.com/xml/xpath_syntax.asp
https://devhints.io/xpath
https://www.guru99.com/xpath-selenium.html



## CSS Locators
_____________________

CSS Locators functionaility is like XPath however the syntax are different.

__CSS Syntax__

* `/` replace by `>` (except the first character)
  *  XPath : `\html\body\div`
  *  CSS Locator: `html > body > div`
  
*  `//` replaced by a blank space (except the first character)
   *  XPath: `//div/span//p`
   *  CSS Locator: ` div > span p`
  
* `[N]` replaced by `:nth-of-type(N)`
  * XPath: `//div/p[2]`
  * CSS Locator: ` div > p:nth-of-type(2)`

### Attributes in CSS
* To find an element by class, use a `.`
  * Example: `p.class-1` selects all paragraph elements belonging to `class-1`
  * More examples:
    * Select paragraph elements within class class1. The div element id is use "uid" using # symbol: 
      * `css_locator = 'div#uid > p.class1`

* `css_locator = 'div#uid > a::attr(href)`
  * `a::attr` is used to select desired attributes


## Scrapy
For the official documentation, you can refer to link below

https://docs.scrapy.org/en/latest/

### Selector Object

Selector is an object in the scrapy library which helps you to extract data from websites by selecting certain parts of HTML document specified by XPath or CSS expressions.

__Setting Up a Selector__

` from scrapy import Selector `

```
html= "
<html>
<head></head>
    <body>
        <div class="example-class">
            <p>This is a website</p>
        </div>
    </body>
</html>"
```
`sel = Selector(text = html)`

* Creating a scrapy Selector Object using a string with the HTML
* The selector `sel` has selected the entire html document

__Selecting Selectors__

* We can use the `xpath` call within a `Selector` to create new `Selector`s  of specific pieces of the html code
* The return is a `SelectorList` of `Selector` objects

__Extracting Data from a SelectorList__

Using the `extract()` method, we can extract the strings out where each of the strings is the data from the Selector which were in the SelectorList

### Selectors with CSS

* Example of using selectors with CSS
` sel.css("html > body")`

Selectors documentation: https://docs.scrapy.org/en/latest/topics/selectors.html


### Text Extraction for XPath

To extract the following text from the html below

```
<p id ="example">
    This is a sample text 
    Click Me <a href="http://extract-text.com">Text</a>
</p>
```

* You can use `text()` method with the XPath.

     `sel.xpath('//p[@id="p-example"]/text()').extract()`
* By using the `/` before the text method, we will direct to all chunks of text that are within that element, but not within other childs. Similarly if you want to point to all chunks of text within that element and its child you can use `//`

### Text Extraction for CSS Locator

For CSS Locator, use `::text`
```
<p id ="example">
    This is a sample text 
    Click Me <a href="http://extract-text.com">Text</a>
</p>
```


`sel.css('p#example::text').extract()`

Add a space before the `::` to point to all chunks of text within that element.



### Response Object

* We want to use the Response object instead of the Selector Object because it helps keep track of which URL the HTML code is loaded from.
  
* The Response Object helps us to move from one site to another, so that we can "crawl" the web while scraping.

* The `response` keeps track of the URL variable 
    
      response.url

* The `follow()` method let us follow a new link

      response.follow(next_url)

Examples on how to use response
* `xpath` methods works like a Selector
  
      response.xpath('//div/span[@class=example-class)'

* `css` method works like a Selector

      response.css('div> span.example-class' )

* Chaining works like a Selector

      response.xpath('//div').css('span.example-class')

* Data Extraction works like a selectory

      response.xpath('//div').css('span.example-class').extract()
      
      response.xpath('//div').css('span/example-class').extract_first()

## Creating a spider
After understanding what is XPaths, CSS locators and Some of the Scrapy functions (Selectors & Response). 

We can now create a basic spider!

Import the Scrapy library

  
    import scrapy
    from scrapy.crawler import CrawlerProcess


Main body of your spider. you can program how you want to scrap the website

    class SpiderClassName(scrapy.Spider):
        name = "spider_name"
        # Program your spider in here

Running the Spider

      #Intiate the CrawlerProcess
      process = CrawlerProcess()
      
      #Tell the process which spider to use
      process.crawl(spider_name)

      #Start the crawling process

      process.start()

After setting up, we can define the class to scrap the web certain sites.


### Start Requests and Basic Parsing

In order for scrapy to run, we need a `start_requests` method to define which site or sites we want to scrap and where to send the information after scraping. 

       def start_requests(self):
          urls = ['Website Link Here']
         
We will create for loop, to take each url within the urls list to be scrap. (Note that the for loop is not needed if you only scrap 1 url)

`yield` command is a python call which acts like a return function, it returns values when the `start_requests ` is called. The object we are yielding is a `scrapy.Request` object.

What `scrapy.Request` does is send a response (the same response variable we are familiar with) pre-loaded with the HTML code from the url argument of the `scrapy.Request` call, to the parsing function defined in the callback argument

        for url in urls
            yield scrapy.Request( url = url, callback = self.parse )


Lastly, we need to have at least one method to parse the website we scrape. we can call the parsing method (or methods) anything we want as long as we correctly identify the method within the `starts_request` function.

The parse method has `response` as its second input variable, this is the variable passed from the `scrapy.Request` call.

        def parse( self, response):
          #simple example: write out the html
          html_file = 'extracted.html'
          with open(html_file, 'wb') as fout:
            fout.write(response.body)

And if we look at the whole spider class, what we see is that the start_request call will pre-load a response variable with the HTML code from the `urls` variable and send it to the method we named parse:

      class ItsyBitsySpider(scrapy.Spider):

        name = 'ItsyBitstSpider'

        def start_requests(self):
          urls = ['Website Link Here']
          for url in urls
            yield scrapy.Request( url = url, callback = self.parse )

        def parse( self, response):
          #simple example: write out the html
          html_file = 'extracted.html'
          with open(html_file, 'wb') as fout:
            fout.write(response.body)

### Advance Parsing

Most of the scraping functions is done in the parsing function. After understanding the basics we can use modify our parse method.

What can we do with the extracted site data beside saving it a local file?

Save URL Links
* extract links and save these links in a newline in the file

      def parse(self, response):

        //You can used XPath and CSS
        links = response.___().extract()
        
        filepath = ''
        with open( filepath, 'w') as f:
          f.writelines([link + '/n' for link in links])

Crawl difference sites

Instead of parsing the links to a file, you can parse it another parsing method to crawl the pages.

The first parse method, we use a for loop to loop over the links we extracted from the site, then we send the spider to follow each of those links and scrape those sites with the second parse method.

Notice that when we send our spider from the first parser to the second, we used the `yield` command again but, instead of creating a `scrapy.Request` call we use the `follow` method in the response variable itself.

The `follow` method works similarly to the `scrapy.Request` call, where we need to input the url we want to use to load a response variable and use the callback argument to point the spider to which parsing method we are going to use next.

        def parse( self, response):
            //you can use XPath or CSS
            links = response.__('___').extract()
            for link in links:
              yield response.follow(url = link, callback = self.parse2)
        
        //second parse method to extract the sites
        def parse2 (self, response):
           //You can used XPath and CSS
            links = response.___().extract()
            
            filepath = ''
            with open( filepath, 'w') as f:
              f.writelines([link + '/n' for link in links])



        


      





