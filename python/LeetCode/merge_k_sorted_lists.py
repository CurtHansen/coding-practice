# Definition for singly-linked list.
from typing import List
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        headnode, prevnode = None, None
        k = len(lists)
        myheap = []
        heapq.heapify(myheap)
        heap_seq_num = 0
        for i in range(k):
            if lists[i] is not None:
                heapq.heappush(myheap,(lists[i].val,heap_seq_num,lists[i]))
                heap_seq_num += 1

        nextnode = None
        while len(myheap) > 0:
            _,_,nextnode = heapq.heappop(myheap)
            if not headnode:
                headnode = nextnode
            if prevnode:
                prevnode.next = nextnode
            if nextnode.next is not None:
                heapq.heappush(myheap,(nextnode.next.val, heap_seq_num, nextnode.next))
                heap_seq_num += 1
            prevnode = nextnode

        if nextnode is not None:
            nextnode.next = None

        return headnode


if __name__ == '__main__':
    n1a, n1b, n1c = ListNode(1), ListNode(4), ListNode(5)
    n1a.next = n1b; n1b.next = n1c
    n2a, n2b, n2c = ListNode(1),ListNode(3), ListNode(4)
    n2a.next=n2b; n2b.next=n2c
    n3a,n3b = ListNode(2),ListNode(6)
    n3a.next=n3b
    sol = Solution()
    print(sol.mergeKLists([n1a,n2a,n3a]))


"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        headnode, prevnode = None, None
        n = len(lists)
        mydict = dict()
        for i in range(n):
            mydict[i] = lists[i]

        while True:
            print(f'headnode {headnode}')
            lowest, lowestidx = float('inf'), None
            for i in range(n):
                if mydict[i] and mydict[i].val < lowest:
                    lowest = mydict[i].val
                    lowestidx = i
            print(f'lowestidx/lowest: {lowestidx}/{lowest}')
            if lowestidx is not None:
                nextnode = mydict[lowestidx]
                mydict[lowestidx] = nextnode.next
                if not headnode:
                    headnode = nextnode
                if prevnode:
                    prevnode.next = nextnode
                prevnode = nextnode
            else:
                break
            nextnode.next = None

        return headnode
"""