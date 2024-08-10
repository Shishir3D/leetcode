class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using two pointer approach
        lpointer, rpointer = 0, len(s) - 1

        while lpointer < rpointer:
            while lpointer < rpointer and self.isAlphaNumeric(s[lpointer]) == False:
                lpointer += 1
            while rpointer > lpointer and self.isAlphaNumeric(s[rpointer]) == False:
                rpointer -= 1

            if (s[lpointer].lower() != s[rpointer].lower()):
                return False
            
            lpointer, rpointer = lpointer + 1, rpointer -1
        
        return True


    def isAlphaNumeric(self, charr):
        charr = charr.lower()
        return ((ord("a") <= ord(charr) and ord(charr) <= ord("z")) or
                ord("0") <= ord(charr) <= ord("9"))
        
        
        