
'''


Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

'''






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




def swap(ListNode):

    # print(" Listnode :  " , ListNode.val)
    
    
    
    if not ListNode:
        return None

    
    
    
    if ListNode.next is None:
        
        print("Returning Alone : " , ListNode.val)
        
        return ListNode.val

    

    
    if ListNode.next.next is None:

        print("swapping alone : " , ListNode.val , ListNode.next.val)

        a = ListNode.val
        ListNode.val = ListNode.next.val
        ListNode.next.val = a

        return ListNode.val






    if ListNode.next.val is not None:
        
        print("swapping " , ListNode.val, ListNode.next.val)
        
        c = ListNode.val
        ListNode.val = ListNode.next.val
        ListNode.next.val = c

        
        
        if ListNode.next.next:
            
            print("ListNode next next val : " , ListNode.next.next.val)
            
            swap(ListNode.next.next)
            


    
    



class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
            # print(head.val)
            
            swap(head)
            
            return head
            
            
            
                
                
