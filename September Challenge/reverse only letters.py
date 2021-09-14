'''

Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

 

Constraints:

    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.



'''



class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        x = ( int(len(s)/2)-1 if len(s)%2 == 0 else int(len(s)/2) )
    

        def reverseSting(text):
            index = -1
            i = len(text)-1
            # Loop from last index until half of the index    
            while i > index:
                print ("i : ", i , "index : " , index)
                # match character is alphabet or not        
                if text[i].isalpha():
                    temp = text[i]
                    while True:
                        index += 1
                        if text[index].isalpha():

                            text[i] = text[index]
                            text[index] = temp
                            i-=1
                            break
                else:
                    i-=1
            return text
        
        return "".join(reverseSting(list(s)))



