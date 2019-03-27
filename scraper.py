# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.PhantomJS(service_args=['--load-images=no'])
        self.driver.get(url)
    def get_source(self):
        return self.driver.page_source.encode('utf-8')
    def get_text_by_xpath(self, path):
        target = self.driver.find_element(By.XPATH, path).text
        return target
    def get_value_by_xpath(self, path):
        target = self.driver.find_element(By.XPATH, path).get_attribute("value")
        return target
    def get_href_by_xpath(self, path):
        target = self.driver.find_element(By.XPATH, path).get_attribute("href")
        return target
    def get_src_by_xpath(self, path):
        target = self.driver.find_element(By.XPATH, path).get_attribute("src")
        return target
    def close(self):
        self.driver.close()
