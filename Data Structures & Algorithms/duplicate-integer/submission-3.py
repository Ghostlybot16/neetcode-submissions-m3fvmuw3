class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # Empty hashset creation

        for n in nums: # Loop through the inputs
            if n in hashset: # Check if the current number already exists in the hash set
                return True # Return True since the value has appeared before
            hashset.add(n) # Add the current number to the hashset since its the first time seeing it
        return False # Return False if it doesn't appear more than once.