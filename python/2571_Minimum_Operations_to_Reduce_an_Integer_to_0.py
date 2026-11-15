class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0

        while n > 0:

            if n & (n - 1) == 0:
                operations += 1
                break
            
            lowest_bit = n & -n
            next_bit = lowest_bit << 1

            if n & next_bit:
                n += lowest_bit
            else:
                n -= lowest_bit
            
            operations += 1
        
        return operations
