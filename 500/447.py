class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(points)):
            h = {}
            for j in range(len(points)):
                if i != j:
                    dt = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                    count += h.get(dt, 0)
                    h[dt] = h.get(dt, 0) + 1
        return count*2

if __name__ == "__main__":
    s = Solution()
    p = [[1, 0], [0, 0], [2, 0]]
    res = s.numberOfBoomerangs(p)
    print(res)
