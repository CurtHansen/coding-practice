from typing import List
from collections import defaultdict


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        if len(buildings) == 0:
            return []

        heights = []  # will have entries [left, right,height]
        print(f'len(buildings): {len(buildings)}')
        for b in buildings:
            n_heights = len(heights)
            building = b.copy()
            print(f'building: {building}')
            l, r, h = building

            # Find the first height block, if any, where the new building needs to be merged.
            # To do this, look for blocks where right hand side is to the right of new building's left side.
            # After the loop, idx is one unit too small, so add 1.
            idx = n_heights - 1
            while idx >= 0 and l < heights[idx][1]:
                idx -= 1
            idx += 1

            if idx == n_heights:
                # This is the first possibility, no overlap.
                # There are two sub possibilities:
                #   1) new building is adjacent to last existing building.
                #   2) new building has a gap with last existing building.
                if l == heights[-1][r]:         # Case 1
                    if h == heights[-1][2]:     # same height, so just extend
                        heights[-1][1] = r
                    else:                       # different height, so append
                        heights.append(building)
                else:                           # Case 2
                    heights.append([heights[-1][r], l, 0])    # blank space
                    heights.append(building)

            else:




                old_left, old_right, old_height = heights[-1]
                print(f'old_left, old_right, old_height: {old_left, old_right, old_height}')
                if l == old_right:  # adjoining
                    heights.append(building)
                elif l > old_right:  # gap between old and new
                    heights.append([old_right,l,0])
                    heights.append(building)
                else:  # overlap
                    if l == old_left:  # same left edge
                        if r < old_right:  # new right edge is to the left of current right
                            if old_height >= h:
                                pass  # do nothing since current building overshadows new
                            else:  # new building is taller, need to break up skyline
                                heights[-1][1] = r
                                heights[-1][2] = h
                                heights.append([r,old_right,old_height])
                        elif r == old_right:  # new right edge equals current right
                            if old_height >= h:
                                pass  # do nothing since current building overshadows new
                            else:  # new building is taller, need to update height
                                heights[-1][2] = h
                        else:  # new right to the right of old right
                            if old_height >= h:
                                heights.append([old_right,r,h])
                            else:
                                heights[-1][1] = r
                                heights[-1][2] = h
                    else:  # in this case, it must be that old_left < l < old_right
                        if r < old_right: # new right edge is to the left of current right
                            if old_height >= h:
                                pass  # do nothing since current building overshadows new
                            else:  # new building is taller, need to break up skyline
                                heights[-1][1] = l
                                heights.append(building)
                                heights.append([r,old_right,old_height])
                        elif r == old_right:  # new right edge equals current right
                            if old_height >= h:
                                pass  # do nothing since current building overshadows new
                            else:  # new building is taller, need to break up skyline
                                heights[-1][1] = l
                                heights.append(building)
                        else:  # new right to the right of old right
                            if old_height >= h:
                                heights.append([old_right,r,h])
                            else:
                                heights[-1][1] = l
                                heights.append(building)


        print(f'heights: {heights}')

        result = []
        for entry in heights:
            result.append([entry[0], entry[2]])
        result.append([heights[-1][1], 0])

        return result


if __name__ == '__main__':
    sol = Solution()
#    buildings = [[0,1,3]]
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print(sol.getSkyline(buildings))



"""
heights = defaultdict(int)
min_spot = buildings[0][0]
max_spot = 0

for building in buildings:
    start = building[0]
    end = building[1]
    for i in range(start, end):
        heights[i] = max(heights[i], building[2])
        max_spot = max(max_spot, i)

answer = []
last_height = None
for i in range(min_spot, max_spot+1):
    if heights[i] != last_height:
        answer.append([i,heights[i]])
        last_height = heights[i]
answer.append([max_spot+1,0])

return answer
"""
