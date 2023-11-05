class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        right = 0
        result = 0
        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right],0)
            if (right-left+1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1
            result = max(result,right-left + 1)
        return result