# -*- coding: utf-8 -*-
# @Author: zhengbohang
# @Date:   2019-04-20 10:13:37
# @Last Modified by:   zhengbohang
# @Last Modified time: 2019-04-20 17:13:20
# @Email: wenwuhang@pku.edu.cn

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless
driver = webdriver.Chrome(options=chrome_options)

class Attraction:
    def __init__(self,city_id,place_id,rank,title,score,loc):
        self.city_id = city_id
        self.place_id = place_id
        self.rank = rank
        self.title = title
        self.loc = loc
        self.score = score

        self.want = -1
        self.gone = -1

        self.comments = -1
        self.comment_verygood = -1
        self.comment_good = -1
        self.comment_common = -1
        self.comment_bad = -1
        self.comment_verybad = -1

        self.score_scene = -1
        self.score_interest = -1
        self.score_value = -1

        self.comment_love = -1
        self.comment_family = -1
        self.comment_friend = -1
        self.comment_business = -1
        self.comment_single = -1

        self.stage = -1
        self.tel = ''
        self.opentime = ''

        self.info = ''
        self.trans = ''
#        self.basic = {}

    def find_details(self):
        index_url = 'https://you.ctrip.com/sight/{}/{}.html'.format(self.city_id, self.place_id)
    #    index_url = 'https://you.ctrip.com/sight/hangzhou14/49894.html'
        self.driver = webdriver.Chrome(options=chrome_options)
        try:
            self.driver.get(index_url)
        except:
            return
            
        try:
            wannago = self.driver.find_elements_by_css_selector('body > div.content.cf > div.dest_toptitle.detail_tt > div > div.f_right > ul > li')
            self.gone = eval(wannago[0].find_element_by_css_selector('#emWentValueID').text)
            self.want = eval(wannago[1].find_element_by_css_selector('#emWantValueID').text)
        except:
            pass

        try:
            commentblock = self.driver.find_elements_by_css_selector('#weiboCom1 > div.detailtab.cf > ul > li')
            self.comments = eval(commentblock[0].find_element_by_css_selector('a > span').text[1:-1])
            self.comment_verygood = eval(commentblock[1].find_element_by_css_selector('a > span').text[1:-1])
            self.comment_good = eval(commentblock[2].find_element_by_css_selector('a > span').text[1:-1])
            self.comment_common = eval(commentblock[3].find_element_by_css_selector('a > span').text[1:-1])
            self.comment_bad = eval(commentblock[4].find_element_by_css_selector('a > span').text[1:-1])
            self.comment_verybad = eval(commentblock[5].find_element_by_css_selector('a > span').text[1:-1])
        except:
            pass

        try:
            score_block = self.driver.find_elements_by_css_selector('#weiboCom1 > div.comment_count.cf > dl > dd')
            self.score_scene = eval(score_block[0].find_element_by_css_selector('span.score').text)
            self.score_interest = eval(score_block[1].find_element_by_css_selector('span.score').text)
            self.score_value = eval(score_block[2].find_element_by_css_selector('span.score').text)
        except:
            pass

        try:
            commenttype = self.driver.find_elements_by_css_selector('#weiboCom1 > div.comment_count.cf > ul > li')
            self.comment_love = eval(commenttype[0].find_element_by_css_selector('a > span.ct_count').text[:-1])
            self.comment_family = eval(commenttype[1].find_element_by_css_selector('a > span.ct_count').text[:-1])
            self.comment_friend = eval(commenttype[2].find_element_by_css_selector('a > span.ct_count').text[:-1])
            self.comment_business = eval(commenttype[3].find_element_by_css_selector('a > span.ct_count').text[:-1])
            self.comment_single = eval(commenttype[4].find_element_by_css_selector('a > span.ct_count').text[:-1])
        except:
            pass

        try:
            ss = driver.find_elements_by_class_name('s_sight_con')
            if not ss:
                pass
            else:
                for i in range(len(ss)):
                    temp = ss[i].text
                    if not temp:
                        continue
                    if '0' <= temp[0] <= '9':
                        self.tel = temp
                    elif temp[0] == 'A':
                        self.stage = temp
            sideblock = self.driver.find_element_by_css_selector('body > div.ttd2_background > div > div.des_narrow.f_right > div.s_sight_infor')
            self.opentime = sideblock.find_element_by_css_selector('dl > dd').text
        except:
            pass

        try:
            #TODO:basic info to be modified
            self.info = self.driver.find_element_by_css_selector('body > div.ttd2_background > div > div.des_wide.f_left > div.normalbox.boxsight_v1 > div:nth-child(2) > div.toggle_s > div').text.strip()
        except:
            pass
        self.driver.implicitly_wait(2)

    def find_trans(self):
        index_url = 'https://you.ctrip.com/sight/{}/{}-traffic.html'.format(self.city_id, self.place_id)
        try:
            self.driver.get(index_url)
        except:
            self.driver.close()
            return
        try:
            self.trans = self.driver.find_element_by_css_selector('body > div.ttd2_background > div > div.des_wide.f_left > div.normalbox.current > div.detailcon > div').text.strip()
        except:
            pass
        self.driver.implicitly_wait(2)
        self.driver.close()

