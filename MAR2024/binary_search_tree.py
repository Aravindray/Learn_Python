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

    def level_order_traversal(self):
        '''Traverses Binary tree level by level'''

    def count(self):
        '''Count and return no of nodes in BST'''

    def count_leaves(self):
        '''Count and return no of leaved nodes in BST'''

    def count_non_leaves(self):
        '''Count and return no of non leaves nodes in BST'''

    def delete_leaves(self):
        '''Find and remove all the leaves'''

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
        result_lst = self.inorder_traversal()
        result_str = str()
        for lst in result_lst:
            result_str += str(lst) + ' '
        return result_str

bst = BinarySearchTree()
bst.insert_value(12)
bst.insert_value(10)
bst.insert_value(7)
bst.insert_value(15)
print(bst)
