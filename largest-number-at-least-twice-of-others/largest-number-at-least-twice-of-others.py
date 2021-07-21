class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
        Trivial cases
        
        - Array only has 1 element
            the return must be 0
         
         - An array of length 2
            - [3, 6]
            
         [3, 6, 1, 0]
         enumerate(nums)
         
         [(0, 3), (1, 6), (2, 1), (3, 0)]
            
         - Do max to find the max, remove it, then do max again and compare them
         
         - Largest starts at the beginning
         
         - Iterate through the array, comparing the curent element to the largest
         if its larger, assign largest to it
         
         
        """
        
        largest = -1
        second_largest = -1
        largest_index = -1
        
        for i, x in enumerate(nums):
            if x > largest:
                second_largest = largest
                largest = x
                largest_index = i
                
            elif x > second_largest:
                second_largest = x
                
        if largest < second_largest*2:
                return -1
                
        return largest_index       