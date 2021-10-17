class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={')':'(',
          ']':'[',
          '}':'{'}
        for i in s: 
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                if stack:
                    top=stack.pop()
                    if top != d[i]:
                        return False
                else:
                    return False
        return len(stack)==0