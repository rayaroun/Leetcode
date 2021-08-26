'''

One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

    For example, it could never contain two consecutive commas, such as "1,,3".

Note: You are not allowed to reconstruct the tree.

 

Example 1:

Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:

Input: preorder = "1,#"
Output: false

Example 3:

Input: preorder = "9,#,#,1"
Output: false

 

Constraints:

    1 <= preorder.length <= 104
    preorder consist of integers in the range [0, 100] and '#' separated by commas ','.

'''





'''

Now why we are dealing with Slots??
As we want to verify whether the preorder serialization is correct or not!,
so we want to confirm whether the number of TreeNodes(including nullable nodes '#') are equal to NumberOfSlotsAvailable in Tree,
i.e, Number Of TreeNodes == Number Of Slots Available (Valid Preorder Serialization)
else Invalid Preorder Serialization.

Now Let us see that how we can calculate the number of slots,
1) For a Leaf Node (0 Children) the slots will be 1 (Why because that slot is only for that leaf node).
2) For a Non Leaf Node the slots will be 3 ,
HOW??
1 slot for the non leaf node itself,
2 slots for its Left and Rigth Child,

3) And for Nullable Node('#') the slots will be 1,
why??
because if a node is NULL then its parent has to define a pointer (NULL) to mention that
either its left or right child is NULL.


Lets take One Example:
"9,3,4,#,#,1,#,#,2,#,6,#,#"

Initially The numberOfSlots = 1 (To accomodate root node only)

1) when we encounter 9 ,
we decrease the numberOfSlots by 1 (because the node 9 is now placed at that slot)
so numberOfSlots become 0
now we will check whether this node is Non Leaf Node,(if it is != '#'),
so as 9 is non leaf node,
so we add 2 in the numberOfSlots(2 slots for its children)
now numberOfSlots become 2

2) Similarly for "3",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 1)
--> Then increment numberOfSlots by 2 (numberOfSlots = 3)

3) Similarly for "4",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 2)
--> Then increment numberOfSlots by 2 (numberOfSlots = 4)

4) For "#",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 3)
--> As this is Nullable Node so we don't increment the numberOfSlots

5) again  For "#",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 2)
--> As this is Nullable Node so we don't increment the numberOfSlots

6) Similarly for "1",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 1)
--> Then increment numberOfSlots by 2 (numberOfSlots = 3)

7) again  For "#",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 2)
--> As this is Nullable Node so we don't increment the numberOfSlots

8) again  For "#",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 1)
--> As this is Nullable Node so we don't increment the numberOfSlots

9)Similarly for "2",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 0)
--> Then increment numberOfSlots by 2 (numberOfSlots = 2)

10) again  For "#",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 1)
--> As this is Nullable Node so we don't increment the numberOfSlots

11) Similarly for "6",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 0)
--> Then increment numberOfSlots by 2 (numberOfSlots = 2)

12) again  For "#",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 1)
--> As this is Nullable Node so we don't increment the numberOfSlots

13) again  For "#",
--> First we decrement numberOfSlots by 1. (numberOfSlots = 0)
--> As this is Nullable Node so we don't increment the numberOfSlots

And finally compare whether numberOfSlots == 0 (If Yes) return true else return false;

'''


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        #based on the approach in the discussion thread
        
        temp = preorder.split(',')
        
        numSlots = 1
        
        for node in temp:
            
            numSlots -= 1
            
            
            print(node, numSlots)
            
            
            if numSlots < 0:
                return False
            
            if node != '#':
                numSlots += 2
            
        
        
        print(numSlots)
        return numSlots == 0

