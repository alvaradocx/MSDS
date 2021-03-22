#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# CS5012
# Chelsea Alvarado
# cxa6ky


# In[ ]:


class Node:

    def __init__(self, data): # Constructor of Node class
        # A node has a data value, a left child node and a right child node
        self.data = data  #data item
        self.left = None  #left child, initially empty
        self.right = None #right child, initially empty


    def __str__(self): # Printing a node
        return str(self.data) #return as string


# In[ ]:


class BinarySearchTree:

    def __init__(self): # Constructor of BinarySearchTree class

        self.root = None  # Initially, an empty root node

# ===================================================================
    def buildBST(self, val):# Build ("create") a binary search tree 
        
        if self.root == None:
            self.root = Node(val)

        else:
            current = self.root

            while 1:

                if val < current.data:

                    if current.left:
                        current = current.left  # Go left...
                    else:
                        current.left = Node(val)  # Left child is empty; place value here
                        break;      

                elif val > current.data:
                 
                    if current.right:
                        current = current.right  # Go right...
                    else:
                        current.right = Node(val)  # Right child is empty; place value here
                        break;      

                else:             
                    break 


# ===================================================================
      
    def find(self, target):  # Find a node with the 'target' value in the BST
        while self.root is not None:
            if self.root.data == target:
                    return True
            if target < self.root.data:
                self.root = self.root.left
            else:
                self.root = self.root.right
        return False

# ===================================================================
    def size(self, node):  # Counts the number of nodes in the BST
        # non recursive(iterative) to get return -1 to show
        if node is None:
            return -1
        d = [] #queue for tracking
        d.append(node)
        count = 1
        while(len(d) != 0):
            node = d.pop(0)
            if (node.left):
                d.append(node.left)
                count +=1
            if (node.right):
                d.append(node.right)
                count +=1
        return count
    
    #original recursive moethod but return -1 does not work
    # if node is None:
    #    return 0
    # return 1 + self.size(node.left) + self.size(node.right)
        

# ===================================================================
    def inorder(self, node):  # Performing in-order tree traversal; smallest to largest
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

# ===================================================================
    def preorder(self, node):  # Performing pre-order tree traversal; root(node), left, right
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

# ===================================================================
    def postorder(self, node):  # Performing post-order tree traversal; left, right, root(node)
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end = ' ')
              
# ===================================================================


# In[ ]:


##################                  
## Testing Code ##
##################                        
                        
tree = BinarySearchTree()    
treeEmpty = BinarySearchTree()  # Empty tree

arr = [8,3,1,6,4,7,10,14,13]    # Array of nodes (data items)
for i in arr:                   # For each data item, build the Binary Search Tree
    tree.buildBST(i)

print('What\'s the size of the tree?')
print(tree.size(tree.root))     # size method

print('What\'s the size of the tree?')
print(treeEmpty.size(treeEmpty.root))

print("") 
print ('In-order Tree Traversal:')
tree.inorder(tree.root)         # Perform in-order tree traversal, and print
 
print("") 
print ('Pre-order Tree Traversal:')
tree.preorder(tree.root)        # Perform pre-order tree traversal, and print

print("")
print ('Post-order Tree Traversal:')
tree.postorder(tree.root)       # Perform post-order tree traversal, and print

print("")
print ('Find 7:', end=" ")      # find method
print(tree.find(7))

print('Find 5:', end=" ")
print(tree.find(5))

print('Find 30:', end=" ")
print(tree.find(30))


# In[ ]:




