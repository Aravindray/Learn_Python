import sys
sys.path.append('d:\\Github\\Python\\MAR2024')
from node import TreeNode

def main():
    bst = TreeNode(15)
    bst.left = TreeNode(10)
    bst.right= TreeNode(23)
    bst.left.left = TreeNode(6)
    bst.right.left = TreeNode(20)
    bst.right.right = TreeNode(30)
    level_order_traversal(bst)

def level_order_traversal(node):
    node_lst = [[node]]
    last = node_lst[-1]
    while last:
        temp = []
        for x in last:
            if x.left is not None:
                temp.append(x.left)
            if x.right is not None:
                temp.append(x.right)
        node_lst.append(temp)
        last = node_lst[-1]
    print(node_lst)
    node_lst.pop()
    print('after pop')
    result = list()
    new_temp = list()
    for x in node_lst:
        for y in x:
            new_temp.append(y.data)
        result.append(new_temp)
        new_temp = list()
    print(result)
                

def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

if __name__ == '__main__':
    main()
