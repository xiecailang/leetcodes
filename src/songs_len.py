#小q的歌单
k = 5
a,x,b,y = 2,3,3,3
c= [([0] * 105) for i in range(105)]
c[0][0] = 1
mod_ = 1000000007
for i in range(1,101,1):
    c[i][0] = 1
    for j in range(1,101,1):
        c[i][j] =(c[i - 1][j - 1]+c[i - 1][j])
ans = 0
for i in range(x):
    if i*a <= k and (k - a*i)%b ==0 and int((k - a*i)/b) <= y:
        ans += c[x][i]*c[y][int((k - a*i)/b)] 
print(ans%mod_)
