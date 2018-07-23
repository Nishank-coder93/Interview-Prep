"""
Author: Nishank Bhatnagar
Description: Given two strings how many minimum edits will it take to convert one string to another 
given that we can Edit, Delete or add to convert one string to another 
Solution: 
MATRIX
1) We create a matrix with length or row as length of string1 plus 1 and len of column being len of string2 plus 1
2) We initialize the 0th row and 0th column with ith and jth value as it will take that many edits to convert to Null string

Running Time: O()
Space Complexity: O()
"""

class MinimumEdit: 
    def __init__(self): 
        # Initialize variables 
        pass

    def print_matrix(self,mat): 
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                print(mat[row][col],end=" ")
            
            print('\n')
            
    # Regular matrix solution
    def mat_solution(self,string1,string2):
        
        # Initialize the matrix with all -1 values
        self.result = [[0 for col in range(len(string2)+1)] for row in range(len(string1)+1)]
        
        # Intialize the 0th col and 0th row 
        for row in range(len(string1) + 1): 
            self.result[row][0] = row
        
        for col in range(len(string2) + 1):
            self.result[0][col] = col
        
        for row in range(1,len(string1) + 1):
            for col in range(1,len(string2) + 1): 
                
                if string1[row-1] == string2[col-1]:
                    self.result[row][col] = self.result[row-1][col-1]
                else:
                    self.result[row][col] = 1 + min(self.result[row-1][col-1], self.result[row-1][col],
                                                   self.result[row][col-1])
        
        self.print_matrix(self.result)
        
        # Traceback to get the letters that were changed 
        row = len(string1) + 1
        col = len(string2) + 1
        
        self.solution = self.result[row][col]
        
        while row != 0 and col != 0: 
            if self.result[row]

    
    # Recursive solution TO-DO
    def rec_solution(self):
        pass

if __name__ == "__main__":
    string1 = 'azced'
    string2 = 'abcdef'

    me = MinimumEdit()
    print(me.mat_solution(string1,string2))
