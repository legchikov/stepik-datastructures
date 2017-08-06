# Task 2
def create_tree(seq):
    tree = dict()
    for value, key in enumerate(seq):
        if key in tree:
            tree.get(key).append(value)
        else:
            tree[key] = list([value])
    return tree


def height_tree(parents, root):
    height = 1
    if root in parents:
        node = parents.get(root)
        for subnode in node:
            height = max(height, 1 + height_tree(parents, subnode))
        return height
    else:
        return 0

#n = int(input())
#str_input = input()
#seq = [int(s) for s in str_input.split(' ')]

#parents = {parent:node for node, parent in enumerate(seq)} # list() --> dict()
