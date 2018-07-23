"""
Author: Nishank Bhatnagar
Description: Given a list of non negative integers and a total value is there a given subset
which equals to the total value 
Solution: 
MATRIX
1) Create a matrix of of row of length of list of integers and column of lenght of total value
2) Initialize the 0th column as T and 0th row accordingly
3) Loop through the matrix and check if the value in the given list is greater than the jth column value 
if so then we grab the top result (i.e. we have already found the subset)
else we check the above row and col or above row and jth col - the current value of the list
Running Time: O(m x n)
Space Complexity: O(m x n)
"""

class SubsetSum: 
    def __init__(self): 
        self.result = []
        
    def print_matrix(self,mat): 
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                print(mat[row][col],end=" ")
            
            print('\n')  
            
    # Regular matrix solution
    def mat_solution(self,lst,totalVal):
        # Initialize the matrix with all False values
        self.result = [[False for j in range(totalVal+1)] for i in range(len(lst))]
        
        # Intialize the 0th col and 0th row 
        for row in range(len(lst)): 
            self.result[row][0] = True
        
        for col in range(1,totalVal + 1): 
            if lst[0] == col:
                self.result[0][col] = True
            else: 
                self.result[0][col] = False
                
        for row in range(len(lst)):
            for col in range(totalVal + 1): 
                if lst[row] > col: 
                    self.result[row][col] = self.result[row-1][col]
                else: 
                    self.result[row][col] = self.result[row-1][col] or self.result[row-1][col-lst[row]]
        
        self.print_matrix(self.result)
        
        row = len(lst)-1
        col = totalVal
        res = []
        
        print("Result:", self.result[row][col])
        
        # Traceback to get the numbers used to get result
        if self.result[row][col]:
            while row != 0 and col != 0: 
                if self.result[row][col] == self.result[row-1][col]:
                    row -= 1
                else: 
                    res.append(lst[row])
                    col -= lst[row]
                    row -= 1
            return (True,res)
        else:
            return (False,res)
    
    # Recursive solution 
    def rec_solution(self):
        pass

if __name__ == "__main__": 
    lst = [2,3,7,8,10]
    total_val = 11

    ss = SubsetSum()
    print(ss.mat_solution(lst,total_val))