#k近邻算法
import numpy as np
#曼哈顿距离
def distance(x1, x2, p):
    if p < np.inf:
        return np.power(np.sum(np.power(np.abs(x1 - x2), p)), 1/p)
    else:
        return np.max(abs(x1 - x2))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_kd_tree(data, depth):
    #sorted(data, key = lambda x:x[di])
    if data.size == 0:
        return None
    di = depth % data.shape[1]#维度 = 深度 mod 总维度
    data = data[data[:, di].argsort()]#按维度排序
    mid_index = int(len(data)/2)#中位数
    head = Node(data[mid_index])
    if data.shape[0] == 1:
        return head 
    #递归构造左右子树
    head.left = build_kd_tree(data[0:mid_index], depth+1)
    head.right = build_kd_tree(data[mid_index+1:len(data)], depth+1)
    return head

def print_tree(head):
    if head == None:
        return None
    print(head.val, end=', ')
    print_tree(head.left)
    print_tree(head.right)

def in_circle(target, source, r):
    distance = np.sqrt(np.sum([i**2 for i in [target - source]]))
    if distance < r:
        return True
    else:
        return False

def find_closest(head, depth, node, closest_node, parent_node):
    parent_node.append(head)
    if head == None or (head.left == None and head.right == None):
        return head
    di = depth % data.shape[1]
    
    is_left = True
    #寻找叶子节点，设叶子节点为最近点
    if node.val[di] <= head.val[di]:
        closest_node = find_closest(head.left, depth+1, node,closest_node, parent_node)        
    else:
        is_left = False
        closest_node = find_closest(head.right, depth + 1, node, closest_node, parent_node)
    #比较当前点和叶子，如果当前点距离更近，则当前点为最近点
    if distance(head.val, node.val, 2) < distance(closest_node.val, node.val, 2):
        parent_node.pop()
        closest_node = head
    #如果当前是父节点，返回
    if len(parent_node) == 1:
        return closest_node
    #查找当前点的父节点的另一个子节点是否更近
    r = distance(closest_node.val, node.val, 2)
    parent = parent_node[len(parent_node) - 2]
    if is_left:
        right = parent.right
        r_dis = distance(right.val, closest_node.val, 2)
        if r_dis < r:
            parent_node.pop()
            find_closest(right, depth, node, closest_node, parent_node)
        else:
            return closest_node
    else:
        left = parent.left
        l_dis = distance(left.val, closest_node.val, 2)
        if l_dis < r:
            parent_node.pop()
            find_closest(left, depth, node, closest_node, parent_node)
        else:
            parent_node.pop()
            return closest_node

    
#x1, x2, x3 = np.array([2, 3]), np.array([5, 4]), np.array([9, 6], np.array([4, 7], np.array([8, 1], np.array([7, 2])
data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
head = build_kd_tree(data, 0)
node = Node([4, 6])
parent_node = []
closest_node = Node(float('inf'))
closest_node = find_closest(head, 0, node, closest_node, parent_node)

#print_tree(head.val)
import matplotlib.pyplot as plt
x = []
y = []
for d in data:
    x.append(d[0])
    y.append(d[1])
    
t_x = node.val[0]
t_y = node.val[1]

n_x = closest_node.val[0]
n_y = closest_node.val[1]

plt.scatter(x, y)
plt.scatter(t_x, t_y, color='red')
plt.scatter(n_x, n_y, color='green')
plt.show()
print(closest_node)
