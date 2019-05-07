# -*- coding: utf-8 -*-
"""
Created on Wed May  8 02:09:55 2019

@author: zheng
"""

import pandas as pd
import csv
 
csv.field_size_limit(500 * 1024 * 1024)
if __name__ == '__main__':
    with open(r'C:\Users\zheng\Desktop\爬虫\爬虫\store\attractions.txt',\
              encoding='utf-8-sig') as f:
        df = f.readlines()
    mat2 = []
    for line in df:
        mat = line.strip().split(',')
        mat2.append(mat)
    columns = ['city_id','rank','place_id','title','loc','score']
    df = pd.DataFrame(mat2,columns=columns)
    df.reset_index().to_csv('attrs.csv',index=False)
    
#    df = pd.read_csv(r'C:\Users\zheng\Desktop\爬虫\爬虫\store\attractions.txt',\
#                     engine='python',header=None,encoding='utf-8')