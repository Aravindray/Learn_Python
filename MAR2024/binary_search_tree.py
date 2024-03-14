'''This is the module for binary search tree'''
from node import TreeNode

class BinarySearchTree:
    '''Tree like structure where root node is the base node and other nodes are placed
    left or right with respect to lower and higher number accordingly'''
    def __init__(self):
        '''Object constructed as empty'''
        self.root = None

    def insert_value(self, value):
        '''New value will be inserted based on the BST structure'''
        if self.root is None:
            self.root = TreeNode(value)
        else:
            child = self.root
            parent = None
            while child is not None:
                parent = child
                if value <= child.data:
                    child = child.left
                else:
                    child = child.right
            if value <= parent.data:
                parent.left = TreeNode(value)
            else:
                parent.right = TreeNode(value)

    def inorder_traversal(self):
        '''
        Inorder traversal of left subtree
        Visit the root
        Inorder traversal of right subtree
        '''
        traversal_lst = list()
        def inorder(root):
            if root is not None:
                inorder(root.left)
                traversal_lst.append(root.data)
                inorder(root.right)
        inorder(self.root)
        return traversal_lst

    def preorder_traversal(self):
        '''
        Visit the root node
        preorder traversal of left subtree
        preorder traversal of right subtree
        '''
        traversal_lst = list()
        def preorder(root):
            if root is not None:
                traversal_lst.append(root.data)
                preorder(root.left)
                preorder(root.right)
        preorder(self.root)
        return traversal_lst
    
    def postorder_traversal(self):
        '''
        Postorder traversal of left subtree
        Postorder traversal of right subtree
        visit the root node
        '''
        traversal_lst = list()
        def postorder(root):
            if root is not None:
                postorder(root.left)
                postorder(root.right)
                traversal_lst.append(root.data)
        postorder(self.root)
        return traversal_lst

    def delete_value(self, value):
        '''Delete the node w.r.t given value'''
        if self.root is None:
            print('Tree is Empty!')
            return None
        current = self.root
        previous = None
        while current.data != value:
            if value < current.data:
                previous = current
                current = current.left
                if current is None:
                    print('node not in the tree')
                    return None
            else:
                previous = current
                current = current.right
                if current is None:
                    print('node not in the tree')
                    return None
        if current.left is None and current.right is None:
            if current.data < previous.data:
                previous.left = None
                temp_data = current.data
                del current
                print(f'Leaf Node {temp_data} is deleted!')
            else:
                previous.right = None
                temp_data = current.data
                del current
                print(f'Leaf Node {temp_data} is deleted!')
        else:
            if value == self.root.data:
                if self.root.right is None:
                    self.root = self.root.left
                else:
                    temp = self.root.left
                    while temp.right is not None:
                        temp = temp.right
                    temp.right = self.root.right
                    self.root = self.root.left
                print('root element is deleted')
            else:
                previous.right = current.left
                temp = current.left
                while temp.right is not None:
                    temp = temp.right
                temp.right = current.right
                del current

    def level_order_traversal(self):
        '''Traverses Binary tree level by level'''
        def lot(tree_node):
            if not tree_node:
                return
            queue = list()
            queue.append(tree_node)
            while queue:
                level_nodes = len(queue)
                for _ in range(level_nodes):
                    temp = queue.pop(0)
                    print(temp.data,end=' ')
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
                print()
        lot(self.root)

    def count(self):
        '''Count and return no of nodes in BST'''
        lst = self.preorder_traversal()
        return len(lst)

    def count_leaves(self):
        '''Count and return no of leaves nodes in BST'''
        def count_lvs(tree_node):
            count = int()
            if tree_node is not None:
                if tree_node.left is None and tree_node.right is None:
                    return 1
                count += count_lvs(tree_node.left)
                count += count_lvs(tree_node.right)
            return count
        return count_lvs(self.root)

    def count_non_leaves(self):
        '''Count and return no of non leaves nodes in BST'''
        return self.count() - self.count_leaves()

    def delete_leaves(self):
        '''Find and remove all the leaves'''
        leaves = list()
        def delete_lvs(tree_node):
            if tree_node is not None:
                if tree_node.left is None and tree_node.right is None:
                    leaves.append(tree_node.data)
                delete_lvs(tree_node.left)
                delete_lvs(tree_node.right)
        delete_lvs(self.root)
        print(leaves)
        for lvs in leaves:
            self.delete_value(lvs)

    def mirror_bst(self):
        '''Create and return mirror image of binary search tree'''

    def copy_bst(self):
        '''Create and return a copy of binary search tree'''

    def minimum_value(self):
        '''Find and return minimum value in a BST'''

    def ancestor(self):
        '''Find and return the first common ancestor of a pair of nodes in the BST'''
    
    def __str__(self):
        '''String representation of bst with inorder traversal'''
        # result_lst = self.inorder_traversal()
        result_lst = self.preorder_traversal()
        result_str = str()
        for lst in result_lst:
            result_str += str(lst) + ' '
        return result_str

bst = BinarySearchTree()
nodes = [8, 8, 12, 5, 10, 13, 3, 7, 11, 1, 4, 6, 8]
for node in nodes:
    bst.insert_value(node)
bst.level_order_traversal()
# print(bst.count())
# print(bst.count_leaves())
# print(bst.count_non_leaves())
# print(bst.delete_leaves())
# print('after delete the leaves',bst)
bst.delete_value(8)
print()
bst.level_order_traversal()
