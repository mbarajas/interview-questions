def calculate_sum(ball_array, ball):
    ball_sum = []
    current_count = 0

    while ball > current_count:
        for i in range(ball_array.index(ball) + 1, len(ball_array)):
            if ball_array[i] < ball and (current_count + ball_array[i] <= ball):
                current_count += ball_array[i]
                ball_sum.append(ball_array[i])


    return ball_sum



ball_array = [7,3,2,8,1]
print(calculate_sum(ball_array, 8))
