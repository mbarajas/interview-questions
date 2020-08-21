class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def directionalView(root, direction):
    queue = []

    if root is None:
        print("The tree is empty")
        return

    queue.append(root)
    queue.append(None)

    while (len(queue)):
        current_node = queue[0]

        if (current_node):
            print(current_node.data, end = "\t")

            while (queue[0] != None):
                current_node = queue[0]

                if direction == "left":
                    if current_node.left:
                        queue.append(current_node.left)

                    if current_node.right:
                        queue.append(current_node.right)
                elif direction == "right":
                    if current_node.right:
                        queue.append(current_node.right)

                    if current_node.left:
                        queue.append(current_node.left)
                else:
                    print("Please enter either left or right for the direction")
                    return

                queue.pop(0)

            queue.append(None)

        queue.pop(0)

root = Node(50)
root.left = Node(21)
root.right = Node(37)
root.left.right = Node(11)
root.left.left = Node(66)
root.right.left = Node(99)
root.right.right= Node(1)
root.right.left.right = Node(16)
root.right.left.right.left = Node(45)
root.right.left.right.right = Node(9)

direction = str(input("Please enter the side of the tree you wish to see: "))
directionalView(root, direction)
