# Based on https://leetcode.com/problems/next-greater-element-iii/

class Solution:
    def nextGreaterElement(self, n: int) -> int:

        number = list(map(int, list(str(n))))
        n = len(number)

        answer = [0]

        pointer = n - 2
        found = False
        while pointer >= 0 and not found:
            subpointer = pointer + 1
            min_idx, min_digit = None, 10
            while subpointer < n:
                if number[subpointer] > number[pointer] and number[subpointer] < min_digit:
                    min_idx, min_digit = subpointer, number[subpointer]
                subpointer += 1
            if min_idx:
                remaining_numbers = number[pointer:min_idx] + number[min_idx+1:n]
                remaining_numbers.sort()
                answer = number[0:pointer] + [min_digit] + remaining_numbers
                found = True
            pointer -= 1

        answer = int("".join([str(x) for x in answer]))
        if answer == 0 or answer > 2 ** 31:
            return -1
        else:
            return answer


if __name__ == '__main__':
    sol = Solution()
    numbers = [12, 23345, 9877654, 54321, 1234321, 1224321]
    for num in numbers:
        print(sol.nextGreaterElement(num))
