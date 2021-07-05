class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        strlist = []
        for i in range(numRows):
            for j in range(i, len(s), 2 * numRows - 2):
                strlist.append(s[j])
                if i != numRows - 1 and i != 0 and j + 2 * numRows - 2 - 2 * i < len(s):
                    strlist.append(s[j + 2 * numRows - 2 - 2 * i])
        ans = ''.join(strlist)
        return ans
