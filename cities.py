# -*- coding: utf-8 -*-
# @Author: zhengbohang
# @Date:   2019-04-19 20:38:37
# @Last Modified by:   zhengbohang
# @Last Modified time: 2019-04-20 17:13:32
# @Email: wenwuhang@pku.edu.cn


from selenium import webdriver
import re
import paths

#browser.implicitly_wait(3)
city_ids = []
driver = webdriver.Chrome()
#driver.maximize_window()

index_url = 'https://you.ctrip.com/sitelist/china110000.html'
driver.get(index_url)
block = driver.find_element_by_css_selector('body > div.ttd2_background.ttd3_media > div > div.des_wide.f_right > div')
hots = block.find_elements_by_css_selector('div.hot_destlist.cf > ul > li')
commons = block.find_elements_by_css_selector('ul > li')
#for i in range(len(hots)):
#    url = hots[i].find_element_by_css_selector('a').get_attribute('href')
#    city_id = re.split('/|\.',url)[-2]
#    city_ids.append(city_id)
for i in range(len(commons)):
    url = commons[i].find_element_by_css_selector('a').get_attribute('href')
    city_id = re.split('/|\.',url)[-2]
    city_ids.append(city_id)

with open(paths.cities,'a+',encoding='utf-8') as f:
    f.write(str(city_ids))
