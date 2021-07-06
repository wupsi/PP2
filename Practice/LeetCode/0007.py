class Solution:
    def reverse(self, x: int) -> int:
        if 1563847412 >= abs(x) >= 1534236469:
            return 0
        elif x >= 0 and abs(x) < 2147483647:
            return int(str(x)[::-1])
        elif abs(x) >= 2147483647:
            return 0
        else:
            return int('-' + str(x)[1:][::-1])