#查找单词
def findword(word, data, i, j, m, n):
    if len(word) == 0:
        return True
    if i < 0 or j < 0 or i > m - 1 or j > n - 1 or word[0] != data[i][j]:
        return False
    tmp = data[i][j]
    data[i][j] = '#'
    ans = findword(word[1:], data, i+1, j, m, n) or findword(word[1:], data, i-1, j, m, n) or findword(word[1:], data, i, j-1, m, n) or findword(word[1:], data, i, j+1, m, n)
    data[i][j] = tmp
    return ans

[m, n, k] = [int(i) for i in input().split()]
words = [w for w in input().split()]
dic = []
for i in range(m):
    dic.append([c for c in input().split()])
for w in words:
    for i in range(m):
        for j in range(n):
            if dic[i][j] == w[0]:
                if findword(w, dic, i, j, m, n):
                    print(w)