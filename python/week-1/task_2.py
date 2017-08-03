# Task 2

def height_tree(unique_parents, node, count):
    if unique_parents:
        #print(unique_parents)
        item = unique_parents.pop(node)
        print(item)
        count += 1
        height_tree(unique_parents, item, count)
    else:
        return count





seq = [4, -1, 4, 1, 1]
seq = [-1, 0, 4, 0, 3]
parents = [seq[i] for i in range(len(seq))]
print(parents)

root = 0
for i, x in enumerate(seq):
    if x == -1:
        root = i
print(root)
unique_parents = {parent:node for node, parent in enumerate(parents)}
print(unique_parents)
height = height_tree(unique_parents, -1, 0)
print(height)
#print(unique_parents)
