#!/usr/bin/env python
# coding: utf-8

# In[3]:


def find_pairs_with_left_greater(arr):
    n = len(arr)
    pairs = []

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                pairs.append((arr[i], arr[j]))

    return pairs


input_array = [9, 16,8, 1]
pairs = find_pairs_with_left_greater(input_array)

for pair in pairs:
    print(pair)
    


# In[4]:


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def are_identical_trees(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False

    if root1.value != root2.value:
        return False

    return (are_identical_trees(root1.left, root2.left) and
            are_identical_trees(root1.right, root2.right))

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

if are_identical_trees(root1, root2):
    print("The trees are identical.")
else:
    print("The trees are not identical.")
    


# In[7]:


def reverse_even_strings(sentence):
    words = sentence.split()
    
    modified_words = []
    
    for i, word in enumerate(words):
        if i % 2 == 1:
            reversed_word = word[::-1]
            modified_words.append(reversed_word)
        else:
            modified_words.append(word)
    
    modified_sentence = ' '.join(modified_words)
    
    return modified_sentence

input_sentence = "The sky is blue"
result = reverse_even_strings(input_sentence)
print(result)


# In[10]:


def find_row_with_most_ones(matrix):
    max_ones = 0
    row_with_most_ones = 0

    for i, row in enumerate(matrix):
        ones_count = row.count(1)
        if ones_count > max_ones:
            max_ones = ones_count
            row_with_most_ones = i

    return row_with_most_ones

matrix = [
    [0, 0, 1, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

result = find_row_with_most_ones(matrix)

if result != 0:
    print(f"The row with the most ones is row {result}")
else:
    print("No ones found in the matrix.")
    


# In[2]:


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

num_rows = len(matrix)
num_cols = len(matrix[0])

middle_row = matrix[num_rows // 2]
middle_col = [matrix[i][num_cols // 2] for i in range(num_rows)]

intersecting_element = matrix[num_rows // 2][num_cols // 2]

total_sum = sum(middle_row) + sum(middle_col) - intersecting_element

print("Sum of middle row and middle column with intersecting element added once:",total_sum)


# In[4]:


input_string = input("Enter a string sequence: ")
substring_to_find = "ABCD"
index = 0

while index < len(input_string):
    if input_string[index:index+4] == substring_to_find:
        print(f"Found 'ABCD' at index {index}")
        index += 1
    else:
        index += 1


# In[ ]:




