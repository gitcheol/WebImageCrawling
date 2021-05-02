import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import category
import os
 
class WebImageCrawler:
    def __init__(self, platform, counter):
        self.platform = platform
        self.counter = counter
        self.resultPath = "./imgs"
        self.driver = None
        self.baseUrl = {
            "daum":"https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q="
        }
    
    # crawl images step by step
    def crawl_imgs(self):
        self.check_driver()
        self.make_result_dir()
        categories = self.get_categories()
        self.get_img(categories)

    # check the chrome driver
    def check_driver(self):
        try:
            self.driver = webdriver.Chrome('./chromedriver')
        except:
            print("check the chrome driver path")

    # make the result dir 
    def make_result_dir(self):
        resultPath = self.resultPath
        if not os.path.exists(resultPath):
            os.makedirs(resultPath)

    # get the WebImage from url
    def get_img(self, categories):
        for item in categories:
            url = self.baseUrl[self.platform] + item
            self.driver.get(url)

            # get the thumnail info
            req = self.driver.page_source
            soup = BeautifulSoup(req, 'html.parser')
            thumbnails = soup.select("#imgList > div > a > img")

            # download the imgs 
            counter = 0 
            for thumbnail in thumbnails:    
                src = thumbnail["src"]  
                fname = self.generate_random_name()
                dload.save(src, self.resultPath + "/" +fname) 
                counter+=1
                if counter == self.counter: 
                    break
            
        self.driver.quit() 
        return

    def get_categories(self):
        cat = category.imagenet_catecory.values()
        catecories = []
        for items in cat:
            item = items.split(", ")
            for i in item:
                catecories.append(i) 
        return catecories

    def generate_random_name(self, format = '.jpg'):
        chr_list = [chr(alpha) for alpha in range(97, 123)]
        fname = ''.join(random.sample(chr_list, 10)) + format
        return fname