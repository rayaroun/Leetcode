'''

THE APPROACH USED IN THIS PROBLEM DIDN'T WORK FOR ALL THE TEST CASES.


Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:

Input: root = [3,1,4,3,None,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,None,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    
    global gno
    

    
    def goodNodes(self, root: TreeNode) -> int:

        
        def inOrderTry(root, gno):
            
            global c
            
            if root.left != None:  
                if root.left.val != None :
                    if root.val > root.left.val :
                        print("root : ", root.val, "root left " , root.left.val)
                        gno = gno - 1 
                        c = gno
                        print("gn : " , gno)
                        inOrderTry(root.left,gno)
                    else:
                        inOrderTry(root.left,gno)
            if root.right != None:
                if root.right.val != None :
                    if root.val > root.right.val:
                        print( "root : " ,  root.val, "root right " , root.right.val)
                        gno = gno - 1
                        c = gno
                        print("gn : " , gno)
                        inOrderTry(root.right,gno)
                    else:
                        inOrderTry(root.right,gno)

            return gno
        
        global arr
        
        arr = []
        
        def printInorder(root):
 
            if root:

                # First recur on left child
                printInorder(root.left)

                # then print the data of node
                arr.append(root.val)

                # now recur on right child
                printInorder(root.right)

        
        printInorder(root)
        
        
        
              
        
        good_nodes = sum(1 for e in arr if e)
        
        if good_nodes == 1:
            return good_nodes
        
        print("good_nodes " , arr)
        
        gno = good_nodes
        
        inOrderTry(root, good_nodes)
        
        
        return c
        
        
        

