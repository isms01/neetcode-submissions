class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if s[-1] == "?":
        #    s = s.rstrip("?")
        #if s[-1] == ".":
        #    s = s.rstrip(".")
        #s_list = s.split(" ")
        s_list = [ch for ch in s if ch.isalnum()]
        integ_s = "".join(s_list)
        lower_case_integ_s = integ_s.lower()
        print(lower_case_integ_s)
        if lower_case_integ_s == lower_case_integ_s[::-1]:
            return True
        else:
            return False