class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        people = sorted(people, reverse=True)
        l,r = 0, len(people)-1
        while l <=r:
            #edge we have a very heavy person, they go alone
            if people[l]+people[r] > limit:
                boat +=1
                l+=1
            elif people[l]+people[r] <= limit:
                boat+=1
                r-=1
                l+=1

        return boat


        