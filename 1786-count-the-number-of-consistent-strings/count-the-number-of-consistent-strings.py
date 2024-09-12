class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        words_count = 0
        word_allowed = True

        for word in words:
            for letter in word:
                if letter not in allowed:
                    word_allowed = False
                    break
            if word_allowed:
                words_count += 1
            word_allowed = True
        
        return words_count