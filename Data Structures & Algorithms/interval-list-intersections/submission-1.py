class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        for interval1 in firstList:
            for interval2 in secondList:
                # check if interval2 overlaps
                if interval2[0] > interval1[1] or interval2[1] < interval1[0]:
                    pass
                else:
                    common = [max(interval1[0],interval2[0]), min(interval1[1], interval2[1])]
                    output.append(common)
        return output



        