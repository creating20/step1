# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:30:24 2019

@author: 格格巫
"""

import xlrd
data=xlrd.open_workbook('C:\\Users\\格格巫\\Desktop\\test.xlsx')
table=data.sheet_by_index(0)
nrows=table.nrows
ncols=table.ncols
print(nrows,ncols)
k=table.row_values(0)
D=[]
m=[]
for i in range(1,nrows):
    lst=table.row_values(i)
    v1=[]
    v1.extend([k[0],lst[0]])
    v2=[]
    v2.extend([k[1],lst[1]])
    m=([v1,v2])
   
    d=dict(m)
    D.append(d)
    
print(D)
print(D[0].keys('var1s'))
    
    