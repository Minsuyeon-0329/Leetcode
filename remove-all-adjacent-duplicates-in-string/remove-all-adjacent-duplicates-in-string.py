class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in s:
            if not stack:
                stack.append(i)
            else:
                top=stack[-1]
                if i == top:
                    stack.pop()
                else:
                    stack.append(i)
        return ''.join(stack)