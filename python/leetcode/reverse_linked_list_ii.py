# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        string = ""
        current = self
        while current:
            string = string + str(current.val) + "->"
            current = current.next
        string = string + "None"
        print(string)


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        last_before_reverse = None
        current = head
        position = 1
        # Fast forward to leftmost reversal node.
        while position < left:
            last_before_reverse = current
            current = current.next
            position += 1
        # At this point, current is the leftmost node in the reversal
        first_reversal, last_reversal, previous = current, current, None
        while position < right:
            old_next = current.next
            current.next = previous
            previous = current
            current = old_next
            position += 1
        last_reversal = current
        old_next = current.next
        last_reversal.next = previous
        first_after_reversal = old_next
        if last_before_reverse:
            last_before_reverse.next = last_reversal
        if first_after_reversal:
            first_reversal.next = first_after_reversal

        if left > 1 or right == 1:
            return head
        else:
            return last_reversal


if __name__ == '__main__':
    num_nodes = 5
    node = ListNode(1); head = node
    for i in range(2, num_nodes+1):
        node.next = ListNode(i)
        node = node.next
    head.print()
    sol = Solution()
    result = sol.reverseBetween(head, 1, 5)
    result.print()