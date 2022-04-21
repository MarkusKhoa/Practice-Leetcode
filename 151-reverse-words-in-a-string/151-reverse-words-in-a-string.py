class Solution(object):
    def reverseWords(self, s):
        s = " ".join(s.split())
        arr_s = s.split()
        n = len(arr_s)
        if len(arr_s) > 1:
            for i in range(len(arr_s) / 2):
                temp = arr_s[i]
                arr_s[i] = arr_s[n-i-1]
                arr_s[n-i-1] = temp
        
        new_str = " ".join(arr_s)
        return new_str