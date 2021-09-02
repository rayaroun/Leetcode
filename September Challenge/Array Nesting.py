'''

You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

    The first element in s[k] starts with the selection of the element nums[k] of index = k.
    The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
    We stop adding right before a duplicate element occurs in s[k].

Return the longest length of a set s[k].

 

Example 1:

Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

Example 2:

Input: nums = [0,1,2]
Output: 1


'''

#Was better than only 13% of the python submissions, didn't really need to create the dictionary to find the max. 


from typing import List
from collections import defaultdict



class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
              

        
        final = defaultdict(set)
       

        def GetMaxFlox(flows):
            return max((len(v), k) for k,v in flows.items())        

        def workfunction(store,index,n):
  
                        

            if n in store[index]:


                for val in store[index]:
            
                    if val in final.keys():
                        continue
            
                    else:
                        final[val] = store[index]
            
                return
            
            else:
                store[index].add(n)
                workfunction(store,index,nums[n])


        for i in range(len(nums)):
            if i in final.keys():
                continue
            else:
                tempdict = defaultdict(set)
                workfunction(tempdict,i,nums[i])


    
        return GetMaxFlox(final)[0]

