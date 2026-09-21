# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self,
               node,  # the node to insert
               node_position):  # the position of the node to insert

        # Need to compare 'node' to all nodes starting from self.head until we find a node whose value
        # is greater than that of 'node' or we run out of nodes.
        # Once this situation has been reached, insert the node before the node in question or just
        # leave it as is since it belongs at the end.

        comparison_node, comparison_predecessor, comparison_position = self.head, None, 0
        node_next = node.next

        # Scan through to find first position where node.val < comparison (if any before node itself).
        while node.val >= comparison_node.val and comparison_position < node_position:
            comparison_node, comparison_predecessor = comparison_node.next, comparison_node
            comparison_position += 1

        if comparison_position == node_position:
            pass  # Nothing to do, node was in right place.
        else:
            if comparison_node == self.head:
                self.head = node
            else:
                comparison_predecessor.next = node
            node.next = comparison_node
            while comparison_node != node:
                comparison_node, comparison_predecessor = comparison_node.next, comparison_node
            comparison_predecessor.next = node_next

    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        self.head = head
        node, position = self.head.next, 1

        while node:
            next_node = node.next
            self.insert(node, position)
            node = next_node
            position += 1

        return self.head

    @staticmethod
    def print_list(node, maxiter=20):
        message = ''
        cnt = 0
        while node and cnt <= maxiter:
            message += str(node.val) + '->'
            node = node.next
            cnt += 1
        if cnt > maxiter:
            return message + '...'
        else:
            return message + 'None'


if __name__ == '__main__':
    node1 = ListNode(-1)
    node2 = ListNode(5)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(0)
    node4.next = node5

    sol = Solution()
    print(sol.print_list(node1))

    node = sol.insertionSortList(node1)
    print(sol.print_list(node))