class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = defaultdict(list)

    # Iterate through each string in the input array
        for s in strs:
        # Sort the characters of the string and use it as a key
            sorted_str = ''.join(sorted(s))
        # Append the original string to the corresponding group
            anagram_groups[sorted_str].append(s)

    # Convert the values of the defaultdict to a list to get the final result
        result = list(anagram_groups.values())
    
        return result