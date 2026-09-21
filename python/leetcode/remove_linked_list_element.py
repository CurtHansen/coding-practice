# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def process_node(self, node, predecessor, val):

        if not node:
            return False, None
        elif node.val == val:
            if predecessor:
                predecessor.next = node.next
            return False, node.next
        else:
            return True, node.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:

        new_head = None

        prev_node = None
        retain, next_node = self.process_node(head, prev_node, val)
        if retain:
            new_head = head
            prev_node = head

        current_node = next_node
        while current_node:
            retain, next_node = self.process_node(current_node, prev_node, val)
            if retain:
                prev_node = current_node
                if not new_head:
                    new_head = current_node

            current_node = next_node

        return new_head


if __name__ == '__main__':
    sol = Solution()
    node6 = ListNode(6)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    print(sol.removeElements(node1, 6))
