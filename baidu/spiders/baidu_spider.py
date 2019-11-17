# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from baidu.items import BaiduItem

class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu_spider' #爬虫名称
    start_urls = ['http://gl-core.paic.com.cn/account/index.html#/login'] # 爬取地址

    #使用selenium driver
    def get_selenium_driver(self):
        options = Options()
        options.add_argument('--headless')
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        driver = webdriver.Chrome(chrome_options=options, executable_path='./plugin/chromedriver.exe')
        return driver

    def __init__(self):
        self.driver = self.get_selenium_driver()

    def parse(self, response):
        print(response.text)

        # 模拟浏览器
        self.driver.get("http://www.baidu.com")
        # 根据id找到百度的输入框
        input_element = self.driver.find_element_by_id('kw')
        # 模拟输入搜索内容
        input_element.send_keys("爬虫")
        # 根据id找到百度的确认按钮
        click_button = self.driver.find_element_by_id('su')
        #模拟点击事件
        click_button.click()
        # 等5s
        self.driver.implicitly_wait(5)
        # 根据classname获取列表数据
        result_list = self.driver.find_elements_by_class_name('result')
        for result in result_list:
            item = BaiduItem()
            print("列表标题："+result.text)
            print("===========================================================================")
            item["name"] = result.text
            yield item

