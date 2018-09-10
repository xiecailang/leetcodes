#字符串A的字符是否都包含在B中
'''
a, b = input(), input()
print('true' if set(b) & set(a) == set(b) else 'false')
'''

class node:
    def __init__(self, c, n):
        self.c = c
        self.n = n
def isNumber(c):
    try:
        float(c)
        return True
    except:
        return False

str_ = list(input())
sub = ''
nodes = []
for i in range(len(str_)):
    if ord(str_[i]) >= ord('0') and ord(str_[i]) <= ord('9'):
        n_s = str_[i]
        num = int(n_s)
        for j in range(i+1, len(str_)):
            n_s = '%s%c' % (n_s, str_[j])
            if isNumber(n_s):
                num = int(n_s)
            else:
                i = j
                break
        nodes.append(node(sub, num))
        sub = ''
    else:
        sub = '%s%c' % (sub, str_[i])
nodes.sort(key=lambda x:(x.n, sum([ord(i) for i in x.c])))
ans = ''
for s in nodes:
    ans = '%s%s' % (ans, s.c * s.n)
print(ans)


#26进制相加
a = list(input())
b = list(input())
a = a[::-1]
b = b[::-1]
sub_len = abs(len(a) - len(b))
if len(a) < len(b):
    for j in range(sub_len):
        a.append('a')
else:
    for j in range(sub_len):
        b.append('a')
move = 'a'
i = 0
c = []
while i < len(a) and i < len(b):
    sum_ab = ord(move) - ord('a') + ord(a[i]) - ord('a') + ord(b[i]) - ord('a')
    c.append(chr(sum_ab % 26 + ord('a')))
    move = 'b' if sum_ab >= 26 else 'a'
    i += 1
if move == 'b':
    c.append('b')
c = c[::-1]
print("".join(c))
