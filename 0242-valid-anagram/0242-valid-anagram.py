class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1 = {}
        hashmap_2 = {}
        for i in s:
            if i not in hashmap_1:
                hashmap_1[i] = 1
            else:
                hashmap_1[i] += 1
                
        for j in t:
            if j not in hashmap_2:
                hashmap_2[j] = 1
            else:
                hashmap_2[j] += 1
        if len(s) != len(t):
            return False
        for key,val in hashmap_1.items():
            if key not in hashmap_2:
                return False
            if hashmap_1[key] != hashmap_2[key]:
                return False
                break
        return True
        