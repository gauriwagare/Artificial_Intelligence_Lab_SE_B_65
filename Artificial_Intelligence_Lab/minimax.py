#Minimax algorithm Implementation
def minimax(depth, node_index, is_maximizing, values, max_depth):
    #if we reached the leaf node
    if depth == max_depth:
        return values[node_index]
    if is_maximizing:
        best = float('-inf')
        #left and right child of the node
        best = max(best, minimax(depth+1, node_index*2, False, values, max_depth))
        best = max(best, minimax(depth+1, node_index*2+1, False, values, max_depth))
        return best
    else:
        best = float('inf')
        #Left and right chid of current node
        best = min(best, minimax(depth+1, node_index*2, True, values, max_depth))
        best = min(best, minimax(depth+1, node_index*2+1, True, values, max_depth))
        return best
# Example graph values(leaf nodes)
values=[2,5,1,9]
max_depth = 2 #depth of the tree
print("The optimal value is: " , minimax(0,0,True, values, max_depth))

