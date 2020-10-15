def is_winner(code_list, shopping_cart):
    if len(code_list) < 1:
        return is_winner

    if len(shopping_cart) < 1:
           is_winner = 0
           return is_winner

    i,j = 0,0

    for item in shopping_cart:
        if code_list[i][j] == item or code_list[i][j] == "anything":
            j += 1
            if j == len(code_list):
                i += 1
                j = 0
            if i == len(code_list):
                return 1
        else:
            j = 1 if code_list[i][0] == "anything" else 0


    return 0



code_list = [ [ "apple", "apple" ], [ "banana", "anything", "banana" ] ]
shopping_cart = [ "orange", "apple", "apple", "banana", "orange", "banana" ]

print(is_winner(code_list, shopping_cart))
