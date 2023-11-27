class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        stack = []
        for i in range(len(words)):
            y = words[i]
            if x in y:
                stack.append(i)
        return stack
                
        