class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = {}
        for point in points:
            xi,yi = point[0],point[1]
            d = math.sqrt(xi**2 + yi**2)
            point_name = tuple(point)
            distances[point_name] = d

        sorted_items = sorted(distances.items(), key=lambda item: item[1])
        top_k = sorted_items[:k]
        return [list(point) for point, d in top_k]
    

        