class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones)>1:
            sorted_ar =  sorted(stones)
            y = sorted_ar[-1]
            x =  sorted_ar[-2]
            if x == y:
                index_y = stones.index(y)
                index_x = stones.index(x)
                stones.remove(x)
                stones.remove(y)
            elif x<y:
                index_y = stones.index(y)
                index_x = stones.index(x)
                y = y-x
                stones[index_y] = y
                stones.remove(x)
        if len(stones)>0:
            return stones[0]
        return 0

            


        