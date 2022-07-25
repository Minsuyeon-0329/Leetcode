class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        s = [word for word in s if word != '']
        return len(s[-1])