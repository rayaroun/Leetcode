'''


You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

 

Example 1:

Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:

Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]

 

Constraints:

    1 <= points.length <= 3000
    points[i].length == 2
    0 <= xi, yi <= 100
    All the given points are unique.







'''



#my approach was to find the maximum y and min y for each x. But also need to find the max x and and min x for each y to arrive at teh optimal solution. 

from typing import List, final


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # print(sorted(trees))

        minx = 100
        maxx = 0


        for tree in trees:
            if minx > tree[0]:
                minx = tree[0]

            if maxx < tree[0]:
                maxx = tree[0]




        # print (minx, maxx)
        def subfinder(mylist, i):
            return list(filter(lambda x: x[0] == i, mylist))




            # return [ele for ele in mylist]


        # print(subfinder(trees,2))


        finalfence = []

        for i in range(minx,maxx+1):

            miny= 100
            maxy = 0

            tlist = subfinder(trees,i)
            if not tlist:
                continue

            if len(tlist) == 1:
                print(tlist)
                finalfence.extend(tlist)
                continue
            else:
                
                maxy = max(tlist, key=lambda x: x[1])
                miny = min(tlist, key=lambda x: x[1])

                # print(miny,maxy)

                # a = [i,maxy]
                # b = [i,miny]

                # if maxy == miny:
                #     finalfence.append(maxy)
                # else:
                print(maxy, miny)
                finalfence.append(maxy)
                finalfence.append(miny)

        return finalfence
                 
