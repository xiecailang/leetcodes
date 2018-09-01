#整理房间
def isSquar(n1, n2, n3, n4):
    x = [n1[0], n2[0], n3[0], n4[0]]
    y = [n1[1], n2[1], n3[1], n4[1]]
    x.sort()
    y.sort()
    if x[0] == x[1] and x[2] == x[3] and x[0] != x[2] and y[0] == y[1] and y[2] == y[3] and y[0] != y[2]:
        return True
    return False

def rotate(n1, p1):
    return [p1[0]+p1[1] - n1[1], p1[1] - p1[0]+n1[0]]

n = int(input())
nodes = []
for i in range(n):
    nodes.append([int(j) for j in input().split()])
steps = [0] * n
for i in range(n*4):
    n1 = [nodes[i][0], nodes[i][1]]
    n2 = [nodes[i+1][0], nodes[i+1][1]]
    n3 = [nodes[i+2][0], nodes[i+2][1]]
    n4 = [nodes[i+3][0], nodes[i+3][1]]

    p1 = [nodes[i][2], nodes[i][3]]
    p2 = [nodes[i+1][2], nodes[i+1][3]]
    p3 = [nodes[i+2][2], nodes[i+2][3]]
    p4 = [nodes[i+3][2], nodes[i+3][3]]

    if isSquar(n1, n2, n3 , n4):
        continue
    for j in range(4):
        n1 = rotate(n1, p1)
        steps[i] += 1
        if isSquar(n1, n2, n3 , n4):
            break
        for k in range(4):
            n2 = rotate(n2, p2)
            steps[i] += 1
            if isSquar(n1, n2, n3 , n4):
                break
            for p in range(4):
                n3 = rotate(n3, p3)
                steps[i] += 1
                if isSquar(n1, n2, n3 , n4):
                    break
                for p in range(4):
                    n4 = rotate(n4, p4)
                    steps[i] += 1
                    if isSquar(n1, n2, n3 , n4):
                        break
        