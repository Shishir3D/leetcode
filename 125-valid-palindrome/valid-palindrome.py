class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        nums = "0123456789"
        valid_str = ""
        for i in s.lower():
            if i in alphabets or i in nums:
                valid_str = valid_str + i
        
        reverse_str = ""

        for j in range(len(valid_str)-1, -1, -1):
            reverse_str = reverse_str + valid_str[j]
        
        return reverse_str == valid_str
        
        