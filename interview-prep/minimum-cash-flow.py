def minCashFlowRec(amount):
    mxCredit = amount.index(max(amount))
    mxDebit = amount.index(min(amount))

    if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
        return 0

    minimum = min(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= minimum
    amount[mxDebit] += minimum

    print("Person " , mxDebit , " pays " , minimum
          , " to " , "Person " , mxCredit)

    minCashFlowRec(amount)

def minCashFlow(graph):
    amount = [0 for i in range(N)]

    for p in range(N):
        for i in range(N):
            amount[p] += (graph[i][p] - graph[p][i])

    minCashFlowRec(amount)

N = 3
graph = [[0, 1000, 2000],
         [0, 0, 5000],
         [4000, 0, 0]]

minCashFlow(graph)
