#!/usr/bin/env python
# coding: utf-8

# In[1]:


def linear_search(values, search_for):
   search_at = 0
   search_res = False
# Match the value with each data element	
   while search_at < len(values) and search_res is False:
      if values[search_at] == search_for:
         search_res = True
      else:
         search_at = search_at + 1
   return search_res
l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))
print(linear_search(l, 91))


# In[2]:


# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


# In[4]:


class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color  # Red or Black
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, 'black')
        self.root = self.NIL_LEAF
    
    def insert(self, key):
        new_node = Node(key, 'red', self.NIL_LEAF, self.NIL_LEAF)
        if self.root == self.NIL_LEAF:
            self.root = new_node
            self.root.color = 'black'
        else:
            self._insert_recursive(self.root, new_node)
            self._fix_violations(new_node)
    
    def _insert_recursive(self, current, new_node):
        if new_node.key < current.key:
            if current.left == self.NIL_LEAF:
                current.left = new_node
                new_node.parent = current
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right == self.NIL_LEAF:
                current.right = new_node
                new_node.parent = current
            else:
                self._insert_recursive(current.right, new_node)
    
    def _fix_violations(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'black'
    
    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child
    
    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child
    
    def is_valid(self):
        if self.root == self.NIL_LEAF:
            return True
        
        # Check if it's a binary search tree
        def is_bst(node, min_key, max_key):
            if node == self.NIL_LEAF:
                return True
            if not min_key <= node.key <= max_key:
                return False
            return (is_bst(node.left, min_key, node.key - 1) and
                    is_bst(node.right, node.key + 1, max_key))
        
        # Check if it satisfies Red-Black Tree properties
        def is_red_black_tree(node):
            if node == self.NIL_LEAF:
                return True
            if node.color != 'red' and node.color != 'black':
                return False
            if node.color == 'red' and (
                    (node.left and node.left.color == 'red') or
                    (node.right and node.right.color == 'red')):
                return False
            left_black_height = self._black_height(node.left)
            right_black_height = self._black_height(node.right)
            if left_black_height != right_black_height:
                return False
            return (is_red_black_tree(node.left) and is_red_black_tree(node.right))
        
        return is_bst(self.root, float('-inf'), float('inf')) and is_red_black_tree(self.root)
    
    def _black_height(self, node):
        if node == self.NIL_LEAF:
            return 1
        left_black_height = self._black_height(node.left)
        right_black_height = self._black_height(node.right)
        return left_black_height + (1 if node.color == 'black' else 0)


# In[ ]:




