# Based on https://leetcode.com/problems/nth-digit/

class Solution:
    def findNthDigit(self, n: int) -> int:

        groupstartnumber = dict()  # the first number in each group
        groupstartnumdigits = dict()  # the cum number of digits at the start num

        numdigitsgroup = 1
        cumnumdigits = 0
        while cumnumdigits <= n:
            if numdigitsgroup == 1:
                groupstartnumber[numdigitsgroup] = 1
            else:
                groupstartnumber[numdigitsgroup] = int('9' * (numdigitsgroup - 1)) + 1
            groupstartnumdigits[numdigitsgroup] = cumnumdigits
            numdigitsingroup = numdigitsgroup * (9 * 10 ** (numdigitsgroup - 1))
            cumnumdigits += numdigitsingroup
            numdigitsgroup += 1

        # Find group.
        while True:
            if numdigitsgroup in groupstartnumdigits and groupstartnumdigits[numdigitsgroup] < n:
                break
            else:
                numdigitsgroup -= 1

        # Find difference.
        diff = n - groupstartnumdigits[numdigitsgroup] - 1
        positioningroup = diff // numdigitsgroup
        digitplace = diff % numdigitsgroup
        targetnumber = positioningroup + groupstartnumber[numdigitsgroup]
        digit = int(str(targetnumber)[digitplace])

        return digit


if __name__ == '__main__':
    sol = Solution()
    print(sol.findNthDigit(3))
    print(sol.findNthDigit(11))
    print(sol.findNthDigit(189))
    print(sol.findNthDigit(190))
