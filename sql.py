# -*- coding: utf-8 -*-
"""
Created on Wed May  8 00:15:39 2019

@author: zheng
"""

import pymysql

con = pymysql.connect(host='localhost',user='root',\
                      passwd='210102',charset='utf8')

cur = con.cursor()
#cur.execute('create database test_db character set utf8;')
cur.execute('use test_db;')

sql_create_table = """CREATE TABLE `CTRIP` (
`index`  varchar(255) NOT NULL ,
`city_id`  text CHARACTER SET utf8 NOT NULL ,
`place_id`  text CHARACTER SET utf8 NOT NULL ,
`rank`  text CHARACTER SET utf8 NOT NULL ,
`title`  text CHARACTER SET utf8 NOT NULL ,
`loc`  text CHARACTER SET utf8 NOT NULL ,
`score`  text CHARACTER SET utf8 NOT NULL ,
`want`  int(8) NULL ,
`gone`  int(8) NULL ,
`comments`  int(8) NULL ,
`comment_verygood`  int(8) NULL ,
`comment_good`  int(8) NULL ,
`comment_common`  int(8) NULL ,
`comment_bad`  int(8) NULL ,
`comment_verybad`  int(8) NULL ,
`score_scene`  double(8,0) NULL ,
`score_interest`  double(8,0) NULL ,
`score_value`  double(8,0) NULL ,
`comment_love` int(8) NULL,
`comment_family` int(8) NULL,
`comment_friend` int(8) NULL,
`comment_business` int(8) NULL,
`comment_single` int(8) NULL,
`stage` text CHARACTER SET utf8 NULL,
`tel` text CHARACTER SET utf8 NULL,
`opentime` text CHARACTER SET utf8 NULL,
`info` text CHARACTER SET utf8 NULL,
`trans` text CHARACTER SET utf8 NULL,

PRIMARY KEY (`index`)
)
"""

#sql_create_table = """CREATE TABLE CTRIP (
#`index` INT NOT NULL AUTO_INCREMENT,\
#`city_id` text CHARACTER SET utf8 NULL,\
#`place_id` text CHARACTER SET utf8 NULL,\
#`rank` text CHARACTER SET utf8 NULL,\
#`title` text CHARACTER SET utf8 NULL,\
#`loc text` CHARACTER SET utf8 NULL,\
#`score text` CHARACTER SET utf8 NULL,\
#`want` int(8) NULL,\
#`gone` int(8) NULL,\
#`comments` int(8) NULL,\
#`comment_verygood`  int(8) NULL,\
#`comment_good` int(8) NULL,
#`comment_common` int(8) NULL,
#`comment_bad` int(8) NULL,
#`comment_verybad` int(8) NULL,
#`score_scene` double(8,0) NULL,
#`score_interest` double(8,0) NULL,
#`score_value` double(8,0) NULL,
#`comment_love` int(8) NULL,
#`comment_family` int(8) NULL,
#`comment_friend` int(8) NULL,
#`comment_business` int(8) NULL,
#`comment_single` int(8) NULL,
#stage text CHARACTER SET utf8 NULL,
#tel text CHARACTER SET utf8 NULL,
#opentime text CHARACTER SET utf8 NULL,
#info text CHARACTER SET utf8 NULL,
#trans text CHARACTER SET utf8 NULL,
#PRIMARY KEY(index)
#)
#"""
cur.execute(sql_create_table)