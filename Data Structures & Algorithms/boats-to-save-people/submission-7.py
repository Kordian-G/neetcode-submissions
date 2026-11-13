class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        people = sorted(people, reverse=True)
        l,r = 0, len(people)-1
        while l <=r:
            if people[l]+people[r] <= limit:
                r-=1     
            boat +=1
            l+=1
        return boat


        