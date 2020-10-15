def kClosest(points, K):
    ordered_k_list = []
    for i, point in enumerate(points):
        if i < len(points) - 1:
            square_value_1 = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1])
            square_value_2 = (points[i + 1][0] * points[i + 1][0]) + (points[i+ 1][1] * points[i + 1][1])

            if square_value_1 > square_value_2:
                temp = points[i]
                points[i] = points[i + 1]
                points[i + 1] = temp

    ordered_k_list = points[0:K]
    return ordered_k_list

test_array1 = [[1,3],[-2,2]]
test_array2 = [[3,3],[5,-1],[-2,4]]

print(kClosest(test_array1, 1))
