class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        idx = 0

        while idx < len(s):
            ch = s[idx]

            if ch == ')':
                tmp_stack = []
                while stack[-1] != '(':
                    tmp_stack.append(stack.pop())
                stack.pop()
                
                stack.append(self.calculate_helper(tmp_stack[::-1]))
                idx += 1
            else:
                if ch.isnumeric():
                    i = idx
                    while idx < len(s) and s[idx].isnumeric():
                        idx += 1
                    stack.append(int(s[i: idx]))
                else:
                    stack.append(ch)
                    idx += 1

        return self.calculate_helper(stack)

    def calculate_helper(self, s):
        if len(s) == 1:
            return s[0]

        idx = 0
        stack = []
        priority_signs = {'/', '*'}
        while idx < len(s):
            ch = s[idx]
            if ch in priority_signs:
                pre = stack.pop()
                idx += 1
                nxt = s[idx]
                
                if ch == '/':
                    if nxt < 0 or pre < 0:
                        nxt *= -1
                        stack.append((pre//nxt)*(-1))
                    
                    else:
                        stack.append(pre // nxt)
                else:
                    stack.append(pre * nxt)
            else:
                stack.append(ch)
 
            idx += 1

        total = stack[0]
        if len(stack) == 1:
            return total

        for idx in range(1, len(stack), 2):
            sign = stack[idx]
            digit = stack[idx + 1]

            if sign == '+':
                total += digit
            else:
                total -= digit

        return total