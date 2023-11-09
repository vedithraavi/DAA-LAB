#!/usr/bin/env python
# coding: utf-8

# In[2]:


keypad = {
    '1': '000',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}

def letter_combinations(digits):
    if not digits:
        return []

    def possible_outputs(combination, next_digits):
        if not next_digits:
            result.append(combination)
        else:
            for letter in keypad[next_digits[0]]:
                possible_outputs(combination + letter, next_digits[1:])
#Coder Vedith 
    result = []
    possible_outputs('', digits)
    return result

digits = input("Enter a string of digits (2-9): ")

combinations = letter_combinations(digits)
print("Possible combinations:")
for combination in combinations:
    print(combination)
#                                                                                                                  Vedith Raavi
#                                                                                                                 Python Coder                                                                                                                  


# In[4]:


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def get_nodes_at_levels(root, level):
    if root is None:
        return []
    if level == 1:
        return [root.value]
    left_nodes = get_nodes_at_levels(root.left, level - 1)
    right_nodes = get_nodes_at_levels(root.right, level - 1)
    return left_nodes + right_nodes

def main():
    root = None

    elements = [4, 2, 6, 1, 3, 5, 7]
    for element in elements:
        root = insert(root, element)

    first_level_nodes = get_nodes_at_levels(root, 1)
    third_level_nodes = get_nodes_at_levels(root, 3)

    print("Nodes in the first level:", first_level_nodes)
    print("Nodes in the third level:", third_level_nodes)

if __name__ == "__main__":
    main()


# In[ ]:




