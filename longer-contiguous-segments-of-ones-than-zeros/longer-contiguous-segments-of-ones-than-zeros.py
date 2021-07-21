class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # Check for 1s, increment 1s counter if 1
        # Store highest 1s counter 
        # check for 0s, increment 0s counter if 0
        # Store highest 0s counter
        # Compare 1s ciunter and 0s counter, return true if 1s is longer 
        # false if not
        
        counter_ones = 0
        counter_zeroes = 0
        most_ones = 0
        most_zeroes = 0
        
        for i in s:
            if i == '1':
                counter_ones += 1
                most_ones = max(counter_ones, most_ones)
                counter_zeroes = 0
            
            if i == '0':
                counter_zeroes += 1
                most_zeroes = max(counter_zeroes, most_zeroes)
                counter_ones = 0
                
        return most_ones > most_zeroes
                
                
                