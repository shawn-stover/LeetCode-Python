class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        [1, 0, 1, 1, 0, 1]
        2
        """
        
        # Track a counter for consecutive 1s
        counter = 0
        
        # Keep track of highest score
        high_score = 0
            
        # Iterate through array
        for i in nums:
            if i == 1:
                # If encounter 1, increment counter
                counter += 1
                
                # Check if new high score
                # If counter is greater, set new high score using max
                high_score = max(counter, high_score)
                    
            else:
                # If encounter 0, reset counter and save high score
                counter = 0
                
        return high_score
        