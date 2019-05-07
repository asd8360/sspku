# -*- coding: utf-8 -*-
# @Author: zhengbohang
# @Date:   2019-04-20 10:13:37
# @Last Modified by:   zhengbohang
# @Last Modified time: 2019-04-20 17:13:40
# @Email: wenwuhang@pku.edu.cn


import paths
from attraction import Attraction
from joblib import Parallel, delayed

JOBS = 3

if __name__ == '__main__':
    with open(paths.atts,'r',encoding='utf-8-sig') as f:
        text = f.readlines()

    def func(line):
        blocks = line.strip().split(',')
        city_id = blocks[0]
        rank = blocks[1]
        place_id = blocks[2]
        title = blocks[3]
        loc = blocks[4]
        score = blocks[5]
        attraction = Attraction(city_id,place_id,rank,title,score,loc)
        attraction.find_details()
        attraction.find_trans()
        with open(paths.details, 'a+', encoding='utf-8') as f:
            f.write(str(attraction.__dict__)+'|\n')
            print('{} has been saved.\n'.format(attraction.title))
        return

    Parallel(n_jobs=JOBS, require='sharedmem')(delayed(func)(text[i+500*7+97]) for i in range(len(text)))




