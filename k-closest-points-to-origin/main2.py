def kClosest(points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]


test_array1 = [[1,3],[-2,2]]
test_array2 = [[3,3],[5,-1],[-2,4]]

print(kClosest(test_array1, 1))
