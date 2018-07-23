"""
Author: Nishank Bhatnagar
Description: Given 2 strings how do we find the longest common subsequece 
E.g. 
- abcdaf
- acbcf 
=> The longest common subsequence is: abcf

Solution: 
MATRIX
1) We create a matrix with len of string1 plus 1 as columns and length of string2 plus 1 as rows 
and we initialize the 0th row and column with 0s as we consider as Null string 
2) We loop through the matrix in order to fill up the table 
3) If the char in one string matches the other then we add 1 to the previous diagonal value
- i.e. all the common subsequences seen before that character 
4) If not equal then we get the max of left or upper value 

Running Time: O(m x n)
Space Complexity: O(m x n)
"""

class LongestCommonSubsequence: 
    def __init__(self): 
        # Initialize variables 
        self.result = []
        self.final_string = ""

    def print_matrix(self,mat): 
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                print(mat[row][col],end=" ")
            
            print('\n')
            
    # Regular matrix solution
    def mat_solution(self,string1,string2):
        
        len_one = len(string1)
        len_two = len(string2)
        
        self.result = [[0 for i in range(len_one+1)] for j in range(len_two+1)]
        
#         self.print_matrix(self.result)
        # Since we have already initialized the array with 0 values, we don't need
        # to do the initial step 
        
        for row in range(1,len_two+1): 
            for col in range(1,len_one+1):
                
                if string2[row-1] == string1[col-1]: 
                    self.result[row][col] = self.result[row-1][col-1] + 1
                else: 
                    self.result[row][col] = max(self.result[row-1][col],
                                                self.result[row][col-1])
        
        # Print the matrix 
        self.print_matrix(self.result)
                
        row = len_two
        col = len_one
        max_common = self.result[row][col]
        
        while row != 0 and col != 0:
            if self.result[row][col] != self.result[row][col-1] and self.result[row][col] != self.result[row-1][col]:
                self.final_string = string2[row-1] + self.final_string
                row -= 1
                col -= 1
            elif self.result[row][col] == self.result[row][col-1]: 
                col -= 1
            else: 
                row -= 1
        
        return self.final_string
    
    # Recursive solution TO DO
    def rec_solution(self):
        pass


if __name__ == "__main__":
    str1 = "abcdafk"
    str2 = "acbcfe"
    print(len(str1))
    print(len(str2))

    lcs = LongestCommonSubsequence()
    print("Result:",lcs.mat_solution(str1,str2))
