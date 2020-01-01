# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 03:11:42 2020

@author: bhakti.p.kulkarni
"""


import numpy as np

answ = np.zeros((9,9), dtype = int)




answ[0,0] = 5
answ[0,4] = 1
answ[0,8] = 4
answ[1,0] = 2
answ[1,1] = 7
answ[1,2] = 4
answ[1,6] = 6
answ[2,1] = 8
answ[2,3] = 9
answ[2,5] = 4
answ[3,0] = 8
answ[3,1] = 1
answ[3,3] = 4
answ[3,4] = 6
answ[3,6] = 3
answ[3,8] = 2
answ[4,2] = 2
answ[4,4] = 3
answ[4,6] = 1
answ[5,0] = 7
answ[5,2] = 6
answ[5,4] = 9
answ[5,5] = 1
answ[5,7] = 5
answ[5,8] = 8
answ[6,3] = 5
answ[6,5] = 3
answ[6,7] = 1
answ[7,2] = 5
answ[7,6] = 9
answ[7,7] = 2
answ[7,8] = 7
answ[8,0] = 1
answ[8,4] = 2
answ[8,8] = 3

print (answ)

possib_value = {0,1,2,3,4,5,6,7,8,9}

counter = 0
for counter in range (4):
    for row in range (9):
        for col in range (9):
            if answ[row, col] == 0:
                temp = set()
                for ele in answ[:,col]:
                    temp.add(ele)
                
                for ele in answ[row,:]:
                    temp.add(ele)
            
                r3 = int(row/3)
                c3 = int(col/3)
                    
                if r3 == 0 and c3 == 0:
                    for box in answ[0:3,0:3]:
                        for ele in box:
                            temp.add(ele)
                elif r3 == 0 and c3 == 1:
                    for box in answ[0:3,3:6]:
                        for ele in box:
                            temp.add(ele)
                elif r3 == 0 and c3 == 2:
                    for box in answ[0:3,6:9]:
                        for ele in box:
                            temp.add(ele)
                elif r3 == 1 and c3 == 0:
                    for box in answ[3:6,0:3]:
                        for ele in box:
                            temp.add(ele)
                elif r3 == 1 and c3 == 1:
                    for box in answ[3:6,3:6]:
                        for ele in box:
                            temp.add(ele)
                elif r3 == 1 and c3 == 2:
                    for box in answ[3:6,6:9]:
                        for ele in box:
                            temp.add(ele)
                elif r3 == 2 and c3 == 0:
                    for box in answ[6:9,0:3]:
                        for ele in box:
                            temp.add(ele)
                elif r3 == 2 and c3 == 1:
                    for box in answ[6:9,3:6]:
                        for ele in box:
                            temp.add(ele)
                elif r3 == 2 and c3 == 2:
                    for box in answ[6:9,6:9]:
                        for ele in box:
                            temp.add(ele)
                
                
                remain_val = possib_value - temp
                #print (row, col, temp, remain_val)
                
                if len(remain_val) == 1:
                    answ[row,col] = remain_val.pop()
            
    print (counter, answ)
            
