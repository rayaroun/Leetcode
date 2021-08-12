"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lower-case English letters.


"""




#### FIRST ATTEMPT ####



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if set(strs)=={""}:
            return [strs]

        final_list = []
        cp_list = strs[:]
        # i = 0

        while strs:
            # print(strs,i)
            # i+=1
            templist = []

            word_del = strs.pop(0)

            
            templist.append(word_del)


            loop_index = 0

            if strs:
                while loop_index <= len(strs)-1:   
                    if set(strs[loop_index]) == set(word_del) :
                        # print(word_del,word)    
                        templist.append(strs.pop(loop_index))
                    else:
                        loop_index += 1
                    

            final_list.append(templist)

        return final_list
      
 



### MUCH EASIER USING DEFAULTDICT ####


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        defdict = defaultdict(list)

        # print(d)

        for s in strs:
            defdict[''.join(sorted(s))].append(s)
        return [value for key,value in defdict.items()]
