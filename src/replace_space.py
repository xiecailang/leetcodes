s = input()
cnt = s.count(' ')
ans = ['']*(cnt*2 + len(s))
i, j = len(s) - 1, len(ans) - 1
while i >= 0 and j >= 0:
    if s[i] == ' ':
        ans[j-2], ans[j-1], ans[j] = '%', '2', '0'
        j -= 3
        i -= 1
    else:
        ans[j] = s[i]
        i -= 1
        j -= 1
print(ans)