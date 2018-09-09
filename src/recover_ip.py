#ip还原
s_ = input()
cnt = 0
def is_valid(s):
    if len(s) > 3 or (len(s) > 0 and s[0] == '0'):
        return False
    return 0 <= int(s) <= 255

def devide(s, k):
    global cnt
    if k == 0:
        if s == '':
            cnt += 1
        return
    for i in range(1,4):
        if i <= len(s):
            if is_valid(s[:i]):
                devide(s[i:], k - 1)
            if s[0] == '0':
                break

devide(s_, 4)
print(cnt)

    
    