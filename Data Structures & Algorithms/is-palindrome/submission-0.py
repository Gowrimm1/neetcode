class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str=""
        for ch in s:
            if ch.isalnum():
                new_str+=ch.lower()
        if new_str!=new_str[::-1]:
            return False
        return True