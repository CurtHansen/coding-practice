class Solution:
    def addBinary(self, a: str, b: str) -> str:
        self.ans = ''

        lena, lenb = len(a), len(b)
        idx1, idx2 = lena-1, lenb-1
        carryover = 0
        while idx1 >= 0 or idx2 >= 0 or carryover > 0:
            digita = '0' if idx1 < 0 else a[idx1]
            digitb = '0' if idx2 < 0 else b[idx2]
            carryover, digit = self.add_bits(digita, digitb, carryover)
            self.ans = str(digit) + self.ans
            idx1 -= 1
            idx2 -= 1

        return self.ans

    def add_bits(self, bitone, bittwo, carryover):
        result = int(bitone) + int(bittwo) + carryover
        digit = result % 2
        carryover = (result - digit) // 2
        return carryover, digit


if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary('1010', '1011'))