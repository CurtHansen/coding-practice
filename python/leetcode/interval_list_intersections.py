def intervalIntersection(A, B):

    """
    Compute the intersection between a list of intervals in one list and those in a second list.
    Args:
        A (list[list[int]]): first set of intervals, ordered and disjoint.
        B (list[list[int]]): second set of intervals, ordered and disjoint.
    Returns:
        list[list[int]] of intersections between all elements in 'A' and 'B'.
    """

    def find_overlap(start1,
                     end1,
                     start2,
                     end2):
        """
        Find the intersection between two intervals.
        Args:
            start1 (int): Starting point for interval 1.
            end1 (int): Ending point for interval 1.
            start2 (int): Starting point for interval 2.
            end2 (int): Ending point for interval 2.

        Returns:
            lis[int, int]: the intersection
        """
        maxstart = max(start1, start2)
        minend = min(end1, end2)
        if minend < maxstart:
            return None
        else:
            return [maxstart, minend]

    lenA, lenB = len(A), len(B)
    ans = []

    if lenA > 0 and lenB > 0:

        idxA = idxB = 0

        while True:
            """
            Walk through both list using respective indices.
            Step forward in a list when that list's next element is before the other's next element or the other list 
            has no elements left at all. 
            """
            startA, endA = A[idxA]
            startB, endB = B[idxB]
            intersection = find_overlap(startA, endA, startB, endB)
            if intersection:
                ans.append(intersection)

            lastA = (idxA == lenA - 1)  # Are we at last interval in A?
            lastB = (idxB == lenB - 1)  # Are we at last interval in B?
            if lastA and lastB:         # No more intervals to consider in either list.
                break
            elif lastA and not lastB:   # No more intervals in A but some in B, so advance in B.
                idxB += 1
            elif not lastA and lastB:   # No more intervals in B but some in A, so advance in A.
                idxA += 1
            else:                       # Intervals left in both A and B.
                nextAstart = A[idxA + 1][0]
                nextBstart = B[idxB + 1][0]
                if nextAstart < nextBstart:
                    idxA += 1
                else:
                    idxB += 1

    return ans


if __name__ == '__main__':
    inputA, inputB = [[0, 2], [5, 10], [13, 23], [24, 25]], \
                     [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(intervalIntersection(inputA, inputB))
