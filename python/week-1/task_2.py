# Task 2
def create_tree(seq):
    tree = dict()
    for value, key in enumerate(seq):
        if key in tree:
            tree.get(key).append(value)
        else:
            tree[key] = list([value])
    #print(tree)
    return tree


def height_tree(parents, root):
    height = 1
    #print('root = {}'.format(root))
    if root in parents:
        node = parents.get(root)
        #print('node = {}'.format(node))
        for subnode in node:
            #print('subnode = {}'.format(subnode))
            height = max(height, 1 + height_tree(parents, subnode))
        return height
    else:
        return 0

#n = int(input())
#str_input = input()
#seq = [int(s) for s in str_input.split(' ')]

#parents = {parent:node for node, parent in enumerate(seq)} # list() --> dict()
