class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False # Cannot have anagram if letter size are not the same

        hash_tableS = {}
        hash_tableT = {}
        
        for letter in s: # Count characters in string S
            if letter in hash_tableS: # Check if the letter is already in the Hash table
                hash_tableS[letter] += 1
            else:
                hash_tableS[letter] = 1 # Add the letter to the hashtable at set its value to 1
        

        for letter in t: # Count characters in string T
            if letter in hash_tableT:
                hash_tableT[letter] += 1
            else:
                hash_tableT[letter] = 1
        
        return hash_tableS == hash_tableT

