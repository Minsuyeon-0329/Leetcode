class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack=[]
        res=[]
        for i in s:
            if i.isalnum():
                stack.append(i.lower())
        for i in range(len(stack)//2):
            if stack[i] == stack[-(i+1)]:
                res.append(i)
            else:
                return False
        return True