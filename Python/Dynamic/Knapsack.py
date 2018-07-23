"""
Author: Nishank Bhatnagar
Description: 0/1 Knapsack problem, given an array of weights and their values.
How to choose the weights such that the sum of thier values is Maximum and sum of weights 
is less than equal to a given weight

Solution: 
- USING MATRIX
 1) We create a temporary matrix with rows as weights and mapped to their given values 
 and columns from 0....n where n is the given weight
 2) Initialize the 0th col with 0 as no amount of weight can satisfy total 0 wt(unless specified)
 initialize 0th row and 1...n col with value of wt[0] if wt[0] <= 1....n value else 0
 3) Then we loop through the matrix from 1,1 to n,n checking if we include the weight
 then whether the (current value + value of wt) is greater or not if we didn't include it 

Running Time: O(m x n) where m -> rows, n -> cols 
Space Complexity: O(m x n)
"""

class Knapsack: 
    def __init__(self): 
        # Initialize variables
        self.result = []
        self.res_weight_value_pair = []
        self.max_value = 0 
    
    def print_matrix(self,mat): 
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                print(mat[row][col],end=" ")
            
            print('\n')
        
    # Regular matrix solution
    def mat_solution(self,weights, values, total_weight):
        
        # Initialize the matrix with all -1 values
        self.result = [[-1 for i in range(total_weight+1)] for j in range(len(weights))]
        
        # Intialize the 0th col and 0th row 
        for row in range(len(weights)): 
            self.result[row][0] = 0
        
        for col in range(1,total_weight+1): 
            if weights[0] <= col:
                self.result[0][col] = values[0]
            else: 
                self.result[0][col] = 0
        
        # Go through each Weight value pair and check to see if it should be included 
        
        for row in range(1,len(weights)):
            for col in range(1,total_weight+1): 
                # If the given weight value is greater than current total weight value
                if weights[row] > col: 
                    self.result[row][col] = self.result[row-1][col]
                else:
                    # Check if the current value plus the value at remaining weight is greater
                    # than value observed if we didn't select the weight (the above value)
                    selg.result[row][col] = max(values[row] + self.result[row-1][col - weights[row]],
                                          self.result[row-1][col])
        
        # Solution for getting the corresponding weights and values used
        row = len(weights)-1
        col = total_weight 
        
        while row != 0 and col != 0: 
            if self.result[row][col] == self.result[row-1][col]: 
                row -= 1
            else: 
                self.res_weight_value_pair.append((values[row],weights[row]))
                row -= 1
                col -= weights[row]
                
        self.print_matrix(result)
        self.max_value = result[len(weights)-1][total_weight]
        
        return self.max_value,self.res_weight_value_pair
    
    # Recursive solution with memoization TO DO
    def rec_solution(self):
        pass


if __name__ == __main__: 
    wt = [1,3,4,5]
    vals = [1,4,5,7]
    total = 7 

    knap = Knapsack() 
    knap.mat_solution(wt,vals,total)