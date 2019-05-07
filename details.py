# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 08:58:03 2019

@author: zheng
"""

from selenium import webdriver
import re
import paths
from attraction import Attraction

def find_details():
    city_ids = []
    place_ids = []
    with open(paths.atts,'r',encoding='utf-8') as f:
        line = f.readline()
        city_id = line.strip().split(',')[0]
        place_id = line.strip().split(',')[2]
        city_ids.append(city_id)
        place_ids.append(place_id)
    
    for city_id,place_id in zip(city_ids,place_ids):
        index_url = 'https://you.ctrip.com/sight/{}/{}.html'.format(city_id,place_id)
    #    index_url = 'https://you.ctrip.com/sight/hangzhou14/49894.html'
        driver = webdriver.Chrome()
        driver.get(index_url)
        wannago = driver.find_elements_by_css_selector('body > div.content.cf > div.dest_toptitle.detail_tt > div > div.f_right > ul > li')
        gone = eval(wannago[0].find_element_by_css_selector('#emWentValueID').text)
        want = eval(wannago[1].find_element_by_css_selector('#emWantValueID').text)
    
if __name__ == '__main__':
    index_url = 'https://you.ctrip.com/sight/hangzhou14/49894.html'
    driver = webdriver.Chrome()
    driver.get(index_url)
    wannago = driver.find_elements_by_css_selector('body > div.content.cf > div.dest_toptitle.detail_tt > div > div.f_right > ul > li')
    gone = eval(wannago[0].find_element_by_css_selector('#emWentValueID').text)
    want = eval(wannago[1].find_element_by_css_selector('#emWantValueID').text)
    