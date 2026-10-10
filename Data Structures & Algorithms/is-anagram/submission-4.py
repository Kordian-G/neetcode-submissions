class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # could create a list of all possible permutations and then compare if another word is in this list 
        # this would be very inefficient and brute force 
        # better would be to count number of each specific letter in a dictionary and then compare with the other, if they have the same number of same 
        # letters then they can be anagrams 
        if len(s) != len(t):
            return False 
        dictionary = {}
        for character in s:
            if character in dictionary.keys():
                dictionary[character] +=1 
            else: 
                dictionary[character] = 1
        
        dictionary_t = {}
        for character in t:
            if character in dictionary_t.keys():
                dictionary_t[character] +=1 
            else: 
                dictionary_t[character] = 1


        if dictionary == dictionary_t:
            return True
        else:
            return False 