# -*- coding: utf-8 -*-
# @Author: zhengbohang
# @Date:   2019-04-19 19:10:26
# @Last Modified by:   zhengbohang
# @Last Modified time: 2019-04-20 17:13:52
# @Email: wenwuhang@pku.edu.cn

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re
import paths
from attraction import Attraction
#browser.implicitly_wait(3)

def find_basic(city_id):
    attractions = []
    driver = webdriver.Chrome()
    #driver.maximize_window()
    page = 0 #提示作用
    titles = []
    nums = []
    currank = 0

    index_url = 'https://you.ctrip.com/sight/{}/s0-p1.html'.format(city_id)

    driver.get(index_url)
    pages = eval(driver.find_element_by_css_selector('body > div.ttd2_background > div > div.des_wide.f_right >\
                                                div > div.list_wide_mod2 > div.ttd_pager.cf > div > span > b').text)
    for pagenum in range(pages):
        pagenum += 1
        index_url = 'https://you.ctrip.com/sight/{}/s0-p{}.html'.format(city_id,pagenum)
        driver.get(index_url)
        block = driver.find_element_by_class_name('list_wide_mod2')
        places = block.find_elements_by_class_name('rdetailbox')

        for i in range(len(places)):
            att = Attraction(city_id)
            dl = places[i].find_element_by_css_selector('dl')
            dt = dl.find_element_by_css_selector('dt')
            a = dt.find_element_by_css_selector('a')
            url = a.get_attribute('href')
            att.title = a.get_attribute('title')
            att.place_id = re.split('\.|/', url)[-2]
            titles.append(att.title)
            att.loc = dl.find_element_by_class_name('ellipsis').text
            currank += 1
            if currank > 500:
                driver.close()
                return
            att.rank = currank
    #        if currank < 100:
    #            att.rank = eval(dt.find_element_by_css_selector('s').text.replace('第','').replace('名',''))
            comments = places[i].find_element_by_class_name('r_comment')
            try:
                att.score = eval(comments.find_element_by_css_selector('li:nth-child(1) > a > strong').text)
            except:
                pass
            print(att.city_id,att.rank,att.place_id,att.title,att.loc,att.score,)
            attractions.append(att)
            #TODO: 评价
            driver.implicitly_wait(0.5)
            with open(paths.atts, 'a+', encoding='utf-8') as f:
                f.write('{},{},{},{},{},{}\n'.format(att.city_id,att.rank,att.place_id,att.title,att.loc,att.score))

if __name__ == '__main__':
    city_ids = []
    with open(paths.cities,'r',encoding='utf-8') as f:
        city_ids = eval(f.read())
    for city_id in city_ids[100:]:
        find_basic(city_id)

