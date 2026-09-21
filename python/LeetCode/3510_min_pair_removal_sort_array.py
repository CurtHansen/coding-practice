from heapq import heapify, heappop, heappush
from typing import List

class Node:
    def __init__(self, id, value, prev=None, succ=None):
        self.id = id
        self.value = value
        self.predecessor = prev
        self.successor = succ
    def __lt__(self, other):
        return self.id < other.id

    def print_node(self):
        current_string = str(self.id) + '(' + str(self.value) + ')'
        if self.successor is None:
            return current_string
        else:
            return current_string + '->' + self.successor.print_node()

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        print(f'\n\n\n{nums=}')

        pair_sums, prev, exceptions, root, active = [], None, set(), None, set()
        for id, num in enumerate(nums):
            node = Node(id, num, prev)
            active.add(id)
            if root is None: root = node
            if prev:
                prev.successor = node
                pair_sum = prev.value + node.value
                heappush(pair_sums, (pair_sum, prev, prev.value, node, node.value))
                if prev.value > node.value:
                    exceptions.add(prev)
            prev = node

        count = 0
        while len(exceptions) > 0:
            count += 1
            print(f'\nsequence: {root.print_node()}')
            print(f'exceptions: {[x.id for x in exceptions]}')
            print(f'active: {active}')
            print(f'{len(pair_sums)=} with first entry as {pair_sums[0]}')
            while pair_sums and (pair_sums[0][1].id not in active or pair_sums[0][1].value != pair_sums[0][2] or pair_sums[0][3].id not in active or pair_sums[0][3].value != pair_sums[0][4]):
                sumvalue, left, leftval, right, rightval = heappop(pair_sums)
                print(f'  discarding sumvalues:{sumvalue}/leftid:{left.id}/leftval:{left.value}/rightid:{right.id}/rightval:{right.value}')
            sumvalue, left, leftval, right, rightval = heappop(pair_sums)
            predecessor = left.predecessor
            successor = right.successor

            print(f'  selected (sumvalues:{sumvalue},leftid:{left.id},leftval:{leftval},rightid:{right.id},rightval:{rightval})', end=" ")
            msg_text1 = "with predecessor "
            msg_text2 = f'id:{predecessor.id}/val:{predecessor.value}' if predecessor else 'None'
            print(msg_text1 + msg_text2, end=" ")
            msg_text1 = "and successor "
            msg_text2 = f'id:{right.id}/val:{right.value}' if right else 'None'
            print(msg_text1 + msg_text2)

            left.value = sumvalue
            left.successor = successor
            if left.successor:
                left.successor.predecessor = left
            exceptions.discard(predecessor)
            exceptions.discard(left)
            exceptions.discard(right)
            active.remove(right.id)

            if predecessor:
                if predecessor.value > left.value:
                    exceptions.add(predecessor)
                pair_sum = predecessor.value + left.value
                heappush(pair_sums, (pair_sum, predecessor, predecessor.value, left, left.value))

            if left.successor:
                pair_sum = left.value + left.successor.value
                heappush(pair_sums, (pair_sum, left, left.value, left.successor, left.successor.value))
                if left.value > left.successor.value:
                    exceptions.add(left)

        print(f'\nfinal: {root.print_node()}')

        return count


if __name__ == '__main__':
    sol = Solution()
    cases = [
        [1, 1, 4, 1],
        [5, 2, 3, 1],
        [1, 2, 2],
        [1, 1, 4, 4, 2, -4, -1],
        [689, -360, 234, 673, 663, -741, 480, 860, -707, 209, 246, 792, 930, 696, -305],
        [2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1],
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499],
        [503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997],
    ]
    for case in cases:
        print(f'\nresult: {sol.minimumPairRemoval(case)}')

