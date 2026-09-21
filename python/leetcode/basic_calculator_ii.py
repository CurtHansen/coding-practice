# Based on https://leetcode.com/problems/basic-calculator-ii/


class Solution:
    def evaluate_blob(self, blob):
        blob = blob.split("*")
        result = 1
        for elem in blob:
            if elem.isdigit():
                result *= int(elem)
            else:
                divs = elem.split('/')
                idx = 1
                for divelem in divs:
                    if idx == 1:
                        result *= int(divelem)
                    else:
                        result //= int(divelem)
                    idx += 1
        return result

    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        first_pass = s.split('+')
        additions, subtractions = [], []
        for each in first_pass:
            results = each.split('-')
            first = True
            for result in results:
                if first:
                    first = False
                    additions += [result]
                else:
                    subtractions += [result]

        print(additions)
        print(subtractions)

        result = 0
        for elem in additions:
            result += self.evaluate_blob(elem)
            print(result)
        for elem in subtractions:
            result -= self.evaluate_blob(elem)
            print(result)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate('2*3*4+5*8-10-100+20*10'))

"""
        numbers = []
        operators = []

        current_number = ''
        for char in s:
            if char.isdigit():
                current_number += char
            else:
                numbers.append(int(current_number))
                current_number = ''
                operators.append(char)
        numbers.append(int(current_number))

        current_number, new_numbers, new_operators = numbers[0], [], []
        idx = 0
        while idx < len(operators):
            while idx < len(operators) and operators[idx] in ['*', '/']:
                if operators[idx] == '*':
                    current_number *= numbers[idx + 1]
                elif operators[idx] == '/':
                    current_number /= numbers[idx + 1]
                idx += 1
            new_numbers.append(current_number)
            current_number = numbers[idx + 1]

            if idx < len(operators):
                new_operators.append(operators[idx])
                idx += 1
        if operators[-1] in ['+', '-']:
            new_numbers.append(current_number)

        print(new_numbers, new_operators)

        operators = new_operators
        answer = numbers[0]
        idx = 0
        for idx in range(len(operators)):
            if operators[idx] == '+':
                answer += numbers[idx + 1]
            else:
                answer -= numbers[idx + 1]

        return answer



"""