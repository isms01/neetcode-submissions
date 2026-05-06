class Solution:
    def counting(self, string: str) -> dict:
        counting = {}
        for ch in string:
            if ch not in counting:
                counting[ch] = 1
            else:
                counting[ch] += 1
        return counting

    def isAnagram(self, s: str, t: str) -> bool:
        count_s_char = self.counting(s)
        count_t_char = self.counting(t)
        return count_s_char == count_t_char