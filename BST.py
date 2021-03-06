class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def add_node_to_bst(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                add_node_to_bst(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                add_node_to_bst(root.r_child, node)

def pre_order_print(root):
    if not root:
        return        
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)
    
binary_list=[3,7,1,5]
r = Node(binary_list[0])
for item in binary_list[1:]:
    add_node_to_bst(r,Node(item))

pre_order_print(r)
                       
