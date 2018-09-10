#决策树
#特征空间
A = ['age', 'work', 'house', 'credit']
A_detail = {'age': 3, 'work': 2, 'house':2, 'credit':3}
C = [0, 1]
src_data = [{'age': 0, 'work': 0, 'house':0, 'credit':0}, {'age': 0, 'work': 0, 'house':0, 'credit':1},{'age': 0, 'work': 1, 'house':0, 'credit':1},{'age': 0, 'work': 1, 'house':1, 'credit':0},{'age': 0, 'work': 0, 'house':0, 'credit':0},
{'age': 1, 'work': 0, 'house':0, 'credit':0},{'age': 1, 'work': 0, 'house':0, 'credit':1},{'age': 1, 'work': 1, 'house':1, 'credit':1},{'age': 1, 'work': 0, 'house':1, 'credit':2},{'age': 1, 'work': 0, 'house':1, 'credit':2},
{'age': 2, 'work': 0, 'house':1, 'credit':2},{'age': 2, 'work': 0, 'house':1, 'credit':1},{'age': 2, 'work': 1, 'house':0, 'credit':1},{'age': 2, 'work': 1, 'house':0, 'credit':2},{'age': 2, 'work': 0, 'house':0, 'credit':0}]
src_label = [0,0,1,1,0,0,0,1,1,1,1,1,1,1,0]
uni_label = list(set(src_label))
#数据集经验熵H(D)
h = 0
import math
for i in set(src_label):
    h += src_label.count(i)/len(src_data)*math.log2(src_label.count(i)/len(src_data))
h = -h
import re
#特征A对数据集经验条件熵H(D|A)
def get_conditional_entropy(data, labels, feature):
    #使用特征将子集划分
    t_sum = 0
    h_a = 0
    for i in range(A_detail[feature]):
        sub_sum = 0
        d_i = [index for index,d in enumerate(data) if d[feature] == i]
        labels_i = [src_label[index] for index in d_i]
        d_i_len = len(d_i)
        h_a += d_i_len/len(src_data)*math.log2(d_i_len/len(src_data))
        for j in range(len(uni_label)):
            d_jk = labels_i.count(j)
            if d_jk != 0:
                sub_sum += d_jk/d_i_len*math.log2(d_jk/d_i_len)
        t_sum += d_i_len/len(src_data)*sub_sum
    return -t_sum, -h_a
gain_set = {}
gain_ratio = {}
for s in A:
    gain_set[s], h_a = get_conditional_entropy(src_data, src_label, s)
    gain_set[s] = h - gain_set[s]
    gain_ratio[s] = gain_set[s]/h_a

#ID3构建决策树
import numpy as np
from collections import Counter
class Node:
    def __init__(self):
        self.data = None
        self.feature = None
        self.mark = None
        self.son = []
def print_tree(head):
    p = head
    print('[%s,%d]' % (head.feature if head.feature != None else 'None', head.mark if head.mark != None else -1 ), end = ';')
    if len(head.son) > 0:
        for i in range(len(head.son)):
            print_tree(head.son[i])
#广度优先
from queue import Queue
def print_tree_hor(head):
    q = Queue()
    q.put(head)
    cur = head
    last = cur
    nlast = None
    while not q.empty():
        cur = q.get()
        print(len(cur.data), '[%s,%d]' % (cur.feature if cur.feature != None else 'None', cur.mark if cur.mark != None else -1 ), end = '    ')
        if len(cur.son) > 0:
            for h in cur.son:
                q.put(h)
                nlast = h
        if cur == last:
            print()
            last = nlast
def create_tree(data, labels, feature, gain, ep):
    #数据集属于同一类，直接返回标记
    head = Node()
    head.data = data
    if len(set(labels)) == 1:
        head.mark = labels[0]
        return head
    #特征集为空集，找data中实例数最大的一类作为标记
    if len(feature) == 0:
        if len(labels) > 0:
            head.mark = dict(zip(*np.unique(labels, return_counts = True)))
        return head
        #head.mark = max(labels.count(i) for i in list(set(labels)))
    #选择信息增益最大的进行分割
    max_gain = gain[0]
    max_feature = feature[0]
    if max_gain < ep:
        head.mark = dict(zip(*np.unique(labels, return_counts = True)))
        return head
    else:
        head.feature = max_feature
        for i in range(A_detail[max_feature]):
            d_i = [index for index,d in enumerate(data) if d[max_feature] == i]
            labels_i = [labels[index] for index in d_i]
            son_data = [data[index] for index in d_i]
            head.son.append(create_tree(son_data, labels_i, feature[1:], gain[1:], ep))
        return head

#将gain排序，生成数组
import operator
sort_gain = sorted(gain_set.items(), key = operator.itemgetter(1), reverse = True)
sort_gain_ratio = sorted(gain_ratio.items(), key = operator.itemgetter(1), reverse = True)

#ID3算法，gain作为特征选择依据
gain_lst = [i[1] for i in sort_gain]
feature_lst = [i[0] for i in sort_gain]
head = create_tree(src_data, src_label, feature_lst, gain_lst, ep=0)
print_tree_hor(head)
#C4.5算法，gain_ratio作为特征选择依据
gain_ratio_lst = [i[1] for i in sort_gain_ratio]
ratio_feature_lst = [i[0] for i in sort_gain_ratio]
head_ratio = create_tree(src_data, src_label, ratio_feature_lst, gain_ratio_lst, ep=0)
print_tree_hor(head_ratio)

