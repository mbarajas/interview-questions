# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum valuesue that
# can be put in a knapsackWeight of
# capacity knapsackWeight
def knapSack(knapsackWeight, weights, values, n):

    # Base Case
    if n == 0 or knapsackWeight == 0 :
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity knapsackWeight,
    # then this item cannot be included
    # in the optimal solution
    if (weights[n-1] > knapsackWeight):
        return knapSack(knapsackWeight, weights, values, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(values[n-1] + knapSack(knapsackWeight-weights[n-1], weights, values, n-1),knapSack(knapsackWeight, weights, values, n-1))

# To test above function
values = [10,20,30,40]
weights = [10, 20, 30, 40]
knapsackWeight = 50
n = len(values)
print(knapSack(knapsackWeight, weights, values, n))
