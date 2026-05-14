class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq_s = ""
        max_num = 0
        for l in range(len(s)):
            r = l
            while r < len(s):
                if s[r] in seq_s:
                    max_num = max(max_num, len(seq_s))
                    seq_s = ""
                    break
                else:
                    seq_s += s[r]
                    r += 1    
            max_num = max(max_num, len(seq_s))                                                      
        return max_num
            