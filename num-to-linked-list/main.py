class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def numList(n):
    if n < 0:
        print("Please enter a number greater than or equal to 0")
        return None

    startNode = Node(0, None)
    loopNode = startNode

    for i in range(n - 1):
        loopNode.next = Node(i + 1, None)
        loopNode = loopNode.next

    return startNode

def printList(head):
    while head is not None:
        print(head.data)
        head = head.next

number = 4
linkedList = numList(number)
printList(linkedList)
