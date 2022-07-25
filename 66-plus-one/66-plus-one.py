class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ''
        for num in digits:
            digits_str += str(num)
        digits_str = str(int(digits_str) + 1)
        res = []
        for i in range(len(digits_str)):
            res.append(int(digits_str[i]))
        return res