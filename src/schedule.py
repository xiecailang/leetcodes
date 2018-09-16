'''
我是一个大帅哥，因此有很多粉丝想和我合影，想请我吃饭，也有很多签售会演唱会等着我，总之我很忙。可是，我的秘书非常不靠谱，他总是把一些日程安排在重复的时间上，比如我今天的日程是: 早上 8:00-10:00 粉丝见面会 早上 9:00-9:30 粉丝早餐会

下午 1:30-5:00 午睡(是的，这很重要) 晚上 8:00-9:30 婚礼表演嘉宾 所以，由于粉丝见面会更重要，我不得不取消粉丝早餐会了，因为他们在同一时间进行。那么问题来 了，现在我需要一套算法，当我输入一天的行程，我需要这个算法告诉我，今天至少要取消多少个行程 才能让每个日程之间时间不重叠。skrskr~
'''
#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************

def is_finish(mark):
    for key in mark.keys():
        if len(mark[key]) > 1:
            return False
    return True 

def  schedule(data):
    mark = {}
    cnt = {}
    for i in range(len(data)):
        start = int(data[i][0]*10.0)
        end = int(data[i][1]*10.0)
        if i not in cnt:
            cnt[i] = 0
        for j in range(start, end, 1):
            if j not in mark:
                mark[j] = [i]           
            else:
                mark[j].append(i)
            cnt[i] += 1
            
    for key in list(mark):
        if len(mark[key]) < 2:            
            if mark[key][0] in cnt:
                cnt.pop(mark[key][0])
            mark.pop(key)
    ans = 0
    while len(cnt) > 0 and not is_finish(mark):
        max_key = max(cnt, key= cnt.get)
        cnt.pop(max_key)
        for key in mark.keys():
            mark[key].remove(max_key)
        ans += 1
    return ans
    
#******************************结束写代码******************************


_data_cnt = 0
_data_cnt = int(input())
_data_i=0
_data = []
while _data_i < _data_cnt/2:
    start = float(input())
    end = float(input())
    _data.append([start, end])
    _data_i+=1

  
res = schedule(_data)

print(str(res) + "\n")