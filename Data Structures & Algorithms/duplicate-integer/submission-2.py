class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set() # Use a hash set 

        for num in nums:
            if num in seen:
                return True 
            seen.add(num) # Add to set since it wasn't seen before
        
        return False