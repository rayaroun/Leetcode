# REALLY PROUD OF THIS ONE


'''


etermine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true



'''




class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def flatten(t):
            return [item for sublist in t for item in sublist]
        
        for i in range(0,9):
            row = board[i]

            row_without_dot = []

            
            
            
            [row_without_dot.append(x) for x in row if x != "." ]


            column = [element[i] for element in board]


            column_without_dot = []

            [column_without_dot.append(x) for x in column if x != "."]


            if (sorted(row_without_dot) == sorted(list(set(row_without_dot)))): 
                if (sorted(column_without_dot) == sorted(list(set(column_without_dot)))):
                    continue
#                     print( sorted(row_without_dot) , " == " , sorted(list(set(row_without_dot))) )
#                     print( sorted(column_without_dot) , " == " , sorted(list(set(column_without_dot))) )

                else:
                    return False
            else:
                return False
        
        
        
        
        
        for i in range(0,7,3):

            flatted1 = (flatten([  board[i][0:3], board[i+1][0:3] , board[i+2][0:3]  ]))

            flatted2 = (flatten([  board[i][3:6], board[i+1][3:6] , board[i+2][3:6]  ]))

            flatted3 = (flatten([  board[i][6:9], board[i+1][6:9] , board[i+2][6:9]  ]))




            box_without_dot1 = []

            box_without_dot2 = []

            box_without_dot3 = []


            [ box_without_dot1.append(x) for x in flatted1 if  x != "." ]

            [ box_without_dot2.append(x) for x in flatted2 if  x != "." ]

            [ box_without_dot3.append(x) for x in flatted3 if  x != "." ]

            # print(i)
            # print(box_without_dot1)
            # print(box_without_dot2)
            # print(box_without_dot3)


            if(sorted(box_without_dot1) == sorted(list(set(box_without_dot1)))):
                if(sorted(box_without_dot2) == sorted(list(set(box_without_dot2)))):
                    if(sorted(box_without_dot3) == sorted(list(set(box_without_dot3)))):
                                continue
        #                 print(sorted(box_without_dot2), " == " , sorted(list(set(box_without_dot2))))
                    else:
                        return False
                else:
                    return False
            else:
                return False

        
        
        return True



    
        
        
        
