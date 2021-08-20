class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def recursion(s,i,j):
            if i==j or i>j:
                return
            
            print("swapping : " , s[i],s[j])
            
            
            c = s[i]
            s[i] = s[j]
            s[j] = c
            
            
            
            
            
            i = i+1
            j = j-1
            
            recursion(s,i,j)
            
            
            
        recursion(s,0,len(s)-1)
            
        
        
            
