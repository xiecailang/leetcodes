class Solution:
    def longestPalindrome(self, s):
        new_str = '#'
        len_ = [1]
        for c in s:
            new_str += '%c#' % c
            len_.append(0)
            len_.append(0)
        print(len_)
        print(new_str)
        for i in range(1, len(new_str)):
            pre, rear = i-1, i+1
            sub_count = 1
            while pre >=0 and rear < len(new_str):
                if(new_str[pre] == new_str[rear]):
                    sub_count += 1
                    pre -= 1
                    rear += 1
                else:
                    break
            len_[i] = sub_count
        print(len_)
        max_index = len_.index(max(len_))   
        max_len = max(len_)
        res_str = s[int((2 * max_index - (max_index + max_len - 1))/2) : int((max_index + max_len - 1)/2)]
        return res_str

solution = Solution()
print(solution.longestPalindrome('hello'))