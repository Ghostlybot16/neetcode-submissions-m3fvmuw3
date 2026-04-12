class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for idx, val in enumerate(nums):
            diff = target - val

            # check if the difference value exists in the hashmap 
            if diff in hash_map:
                return [hash_map[diff], idx] # Return the indices of the found pair

            # If not found, store current value and it's index in the hashmap
            hash_map[val] = idx