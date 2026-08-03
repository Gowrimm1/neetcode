class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = {}
        max_len = -1
        
        for i, char in enumerate(s):
            if char in first_index:
                # Calculate characters BETWEEN current index and the first time we saw this char
                max_len = max(max_len, i - first_index[char] - 1)
            else:
                # Store only the FIRST occurrence to maximize distance
                first_index[char] = i
                
        return max_len