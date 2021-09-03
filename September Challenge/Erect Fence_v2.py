#I don't think this is getting any efficient 

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # print(sorted(trees))

        minx_outer = 100
        maxx_outer = 0
        miny_outer = 100
        maxy_outer = 0

        for tree in trees:
            if minx_outer > tree[0]:
                minx_outer = tree[0]

            if maxx_outer < tree[0]:
                maxx_outer = tree[0]

            if miny_outer > tree[1]:
                miny_outer = tree[1]

            if maxy_outer < tree[1]:
                maxy_outer = tree[1]





        # print (minx, maxx)
        def subfindery(mylist, i):
            return list(filter(lambda x: x[0] == i, mylist))

        def subfinderx(mylist, i):
            return list(filter(lambda x: x[1] == i, mylist))




            # return [ele for ele in mylist]


        # print(subfinder(trees,2))






        def yequal(minx_outer,maxx_outer):

            finalfencex = []


            for i in range(minx_outer,maxx_outer+1):

                # miny= 100
                # maxy = 0

                tlist = subfindery(trees,i)
                if not tlist:
                    continue

                if len(tlist) == 1:
                    # print(tlist)
                    finalfencex.extend(tlist)
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
                    # print(maxy, miny)
                    finalfencex.append(maxy)
                    finalfencex.append(miny)

            return finalfencex


        def xequal(miny_outer,maxy_outer):


            finalfencey = []


            for j in range(miny_outer,maxy_outer+1):

                # minx = 100
                # maxx = 0

                tlist = subfinderx(trees,j)
                if not tlist:
                    continue

                if len(tlist) == 1:
                    # print(tlist)
                    finalfencey.extend(tlist)
                    continue
                else:
                    
                    maxx = max(tlist, key=lambda x: x[0])
                    minx = min(tlist, key=lambda x: x[0])

                    # print(miny,maxy)

                    # a = [i,maxy]
                    # b = [i,miny]

                    # if maxy == miny:
                    #     finalfence.append(maxy)
                    # else:
                    # print(maxy, miny)
                    finalfencey.append(maxx)
                    finalfencey.append(minx)

            return finalfencey






        if miny_outer == maxy_outer:
            print("1")
            return yequal(minx_outer, maxx_outer)


            

        if minx_outer == maxx_outer:
            print("2")
            return xequal(miny_outer,maxy_outer)


        if minx_outer != maxx_outer and miny_outer != maxy_outer:
            finalfencex = yequal(minx_outer,maxx_outer)
            finalfencey = xequal(miny_outer,maxy_outer)
            finale = [list(x) for x in set(map(tuple, finalfencex)).intersection(map(tuple, finalfencey))]
            return finale
            
