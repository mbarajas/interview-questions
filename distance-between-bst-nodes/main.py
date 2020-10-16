#STEPS:
# 1. Build BST
# 2. Find LCA
# 3. Find Distance from LCA to given Nodes

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_distance(node_list, node_value_1, node_value_2):
    root = Node(node_list[0])
    for i in range(1, len(node_list)):
        root = build_bst(root, node_list[i])

    lca = find_lca(root, node_value_1, node_value_2)
    distance = find_distance_from_lca(lca, node_value_1) + find_distance_from_lca(lca, node_value_2)
    return distance

def build_bst(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = build_bst(root.right, key)
        else:
            root.left = build_bst(root.left, key)
    return root

def find_lca(root, node_value_1, node_value_2):
    while True:
        if(root.value > node_value_1 and root.value > node_value_2):
            root = root.left
        elif(root.value < node_value_1 and root.value < node_value_2):
            root = root.right
        else:
            return root

def find_distance_from_lca(lca, node_value):
    distanceSum = 0

    while True:
        if(lca is not None):
            if(lca.value == node_value):
                return distanceSum
            elif(lca.value < node_value):
                distanceSum += 1
                lca = lca.right
            elif(lca.value > node_value):
                distanceSum += 1
                lca = lca.left
        else:
            return distanceSum


node_list = [2, 1, 3, 5, 4, 6, 10]
node_value_1 = 1
node_value_2 = 6

print(find_distance(node_list, node_value_1, node_value_2))
