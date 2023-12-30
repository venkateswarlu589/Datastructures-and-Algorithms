class Solution:
    def makeEqual(self, words):
        char_count = defaultdict(int)

        # Count the occurrences of each character
        for word in words:
            for char in word:
                char_count[char] += 1

        n = len(words)

        # Check if each character's count is a multiple of the number of strings
        for count in char_count.values():
            if count % n != 0:
                return False

        return True
