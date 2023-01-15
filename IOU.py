#!/usr/bin/env python
# coding: utf-8

# In[5]:


import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import os
import json
import glob


# In[328]:


# geopandas
target = input('주소를 입력해주세요 : ')
df = pd.read_excel('{}/IOU 확인용2.xlsx'.format(target),header = 0)
df['IOU_predict'] = 0
df['Parts'] = 0

for i in df.index:
    df['answer'][i] = df['answer'][i].replace('\n',"").replace(' ',"").replace('(',"").replace(')',"")
    df['predict'][i] = df['predict'][i].replace(' ',"").replace('(',"").replace(')',"")
    
odd = [i for i in range(0,8) if i%2==0]
even = [i for i in range(0,8) if i%2==1]

for i in df.index:
    for val in ['answer', 'predict']:
        temp = df[val][i].split(",")
        globals()['{}_point'.format(val)] = [[float(temp[k]),float(temp[j])] for k, j in zip(odd, even)]

    polys1 = gpd.GeoSeries(Polygon([answer_point[0],answer_point[1],answer_point[2],answer_point[3]]))
    polys2 = gpd.GeoSeries(Polygon([predict_point[0],predict_point[1],predict_point[2],predict_point[3]]))
    df1 = gpd.GeoDataFrame({'geometry': polys1, 'df1':[1]})
    df2 = gpd.GeoDataFrame({'geometry': polys2, 'df2':[2]})
    
    #합집합
    res_union = gpd.overlay(df1, df2, how='union')
    res_union = res_union.reset_index()
    res_union['index'] = res_union['index'].astype(str)
    
    #교집합
    res_intersection = gpd.overlay(df1, df2, how='intersection')
    
    #여집합 (합-교)
    printres_symdiff = gpd.overlay(df1, df2, how='symmetric_difference')
    
    all_area = res_union['geometry'].area.sum()
    center = res_intersection['geometry'].area.sum()
    parts = printres_symdiff['geometry'].area.sum()
    
    iou = center/all_area
    not_overlap = parts/all_area

    df.loc[i,'IOU_predict'] = round(iou,2)
    df.loc[i,'Parts']=round(not_overlap,2)
    
df['difference'] = df['IOU'] - df['IOU_predict']
df.to_csv('{}/IOU_test.csv'.format(target))