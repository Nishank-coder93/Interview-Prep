"""
Author: Nishank Bhatnagar
Description: Give a list of integers find the longest increasing subsequence eg. 3 4 -1 0 6 2 3 => -1 0 2 3 - 4
Solution:

Running Time: O(n^2)
Space Complexity: O(n)
"""

class LongestIncreasingSubsequence: 
    def __init__(self): 
        self.result = []
        self.solution = []
            
    # Regular array solution
    def arr_solution(self,arr):
        
        # Initialize the array with all 1 values as there will be atleast one subsequence
        self.result = [1 for i in range(len(arr))]
        self.solution = [i for i in range(len(arr))]
        
        i = 1
        
        while i < len(arr):
            j = 0
            while j < i:
                
                if arr[i] > arr[j] and self.result[i] < self.result[j] + 1:
                    self.result[i] = self.result[j]+1
                    self.solution[i] = j
                
                j += 1
            
            i += 1
        
        print(self.result)
        print(self.solution)
        print(self.result[len(arr) - 1])
        
        # traceback solution array to get the numbers 
        max_value = max(self.result)
        index = self.result.index(max_value)
        res = []
        
        res.append(arr[index])
        
        while index > 0:
            index = self.solution[index]
            res.insert(0,arr[index])
        
        return res
            
    # Recursive solution TO-DO
    def rec_solution(self):
        pass

if __name__ == "__main__": 
    lst = [-2,3,4,-1,0,6,2,3]

    lic = LongestIncreasingSubsequence()
    print(lic.arr_solution(lst))