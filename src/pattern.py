class Solution:
    def compile_nfa(self, p):
        p_index = 0
        nfa = ''
        while p_index < len(p):
            if p_index + 1 < len(p):
                if p[p_index + 1] == '*':
                    nfa = '%s%c%c' % (nfa, 'N', p[p_index])
                    p_index += 2
                else:
                    nfa = '%s%c%c' % (nfa, '1', p[p_index])
                    p_index += 1
            else:
                nfa = '%s%c%c' % (nfa, '1', p[p_index])
                break
        return nfa

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_index = 0
        nfa_index = 0
        nfa = self.compile_nfa(p)
        sign = True
        print(nfa)
        while nfa_index < len(nfa):
            if nfa[nfa_index] == '1':
                c = nfa[nfa_index + 1]
                if c == '.' or s[s_index] == nfa[nfa_index + 1]:
                    s_index += 1
                    nfa_index += 2
                else:
                    sign = False
                    break
            if nfa[nfa_index] == 'N':
                c = nfa[nfa_index + 1]
                if c == '.':
                    

                    
        


solution = Solution()
print(solution.isMatch('ab', 'c*a*.'))