"""
Author: Nishank Bhatnagar
Description: Problem Statement 
Solution: Solution steps 

Running Time: O()
Space Complexity: O()
"""

class LongestPalindromicSubsequence: 
    def __init__(self): 
        # Initialize variables 
        self.result = []
        

    def print_matrix(self,mat): 
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                print(mat[row][col],end=" ")
            
            print('\n')
            
    # Regular matrix solution
    def mat_solution(self,string):
        
        # Initialize the matrix with all -1 values
        self.result = [[-1 for j in range(len(string))] for i in range(len(string))]
        
        # Intialize the ith col and ith row 
        for i in range(len(string)): 
            self.result[i][i] = 1
            
        l = 2 
        
        while l < len(string)+1:
            i = 0
            j = l-1
            
            while j < len(string):
                if string[i] != string[j]:
                    self.result[i][j] = max(self.result[i][j-1],self.result[i+1][j])
                elif string[i] == string[j]:
                    self.result[i][j] = 2 + self.result[i+1][j-1]
                i += 1
                j += 1
            
            l += 1
        
        self.print_matrix(self.result)
        
    
    # Recursive solution TO-DO
    def rec_solution(self):
        pass

if __name__ == "__main__": 
    lps = LongestPalindromicSubsequence()
    lps.mat_solution('agbdba')