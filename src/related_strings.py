'''
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
示例 1:
输入:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出: [0,9]
解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2:
输入:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
输出: []
'''
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0:
            return []
        dic_words = {}
        tar_words = {}
        len_ = len(words[0])
        ans = []
        for w in words:
            if w in dic_words:
                dic_words[w] += 1
            else:
                dic_words[w] = 1
            if len(w) != len_:
                return []
        for j in range(len_):
            cnt = 0
            left = j
            tar_words.clear()
            for i in range(j, len(s), len_):
                t = s[i:i+len_]
                
                if t in dic_words:
                    tar_words[t] = 1 if t not in tar_words else tar_words[t] + 1
                    if tar_words[t] <= dic_words[t]:
                        cnt += 1
                    else:
                        #左移边界
                        for k in range(left, i, len_):
                            k_w = s[k:k+len_]
                            if k_w == t:
                                left = k + len_
                                tar_words[k_w] -= 1
                                break
                            tar_words[k_w] -= 1
                            if tar_words[k_w] == 0:
                                tar_words.pop(k_w)
                            cnt -= 1
                        
                else:
                    cnt = 0
                    left = i+len_
                    tar_words.clear()
                if cnt == len(words):
                    ans.append(left)
                    s_word = s[left:left + len_]
                    tar_words[s_word] -= 1
                    if tar_words[s_word] == 0:
                        tar_words.pop(s_word)
                    cnt -= 1
                    left += len_
        return ans
s = input()
words = [s for s in input().split()]
so = Solution()
print(so.findSubstring(s, words))

                        
