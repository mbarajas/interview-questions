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

def levelView(root):
    if root is None:
        return

    queue = []

    queue.append(root)

    while(len(queue) > 0):
        node = queue[0]
        queue.pop(0)
        print (node.data)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

#direction = str(input("Please enter the side of the tree you wish to see: "))
#directionalView(root, direction)
levelView(root)
