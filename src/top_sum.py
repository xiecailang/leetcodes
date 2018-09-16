#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


def topk(nums):
    dic1 = list(set(nums))
    dic2 = [nums.count(i) for i in set(nums)]
    dic1.sort(key = nums.index)
    dic2.sort(key = nums.index)
    max_1 = dic1[dic2.index(max(dic2))]
    dic2.pop(max(dic2))
    max_2 = dic1[dic2.index(max(dic2))]
    return max_1 + max_2


#******************************结束写代码******************************


_nums_cnt = 0
_nums_cnt = int(input())
_nums_i=0
_nums = []
while _nums_i < _nums_cnt:
    _nums_item = int(input())
    _nums.append(_nums_item)
    _nums_i+=1

  
res = topk(_nums)

print(str(res) + "\n")