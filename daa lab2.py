#!/usr/bin/env python
# coding: utf-8

# In[ ]:


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

product = 1
for row in matrix:
    for element in row:
        product *= element

if product > 50:
    print("The product of the matrix is greater than 50.")
else:
    print("The product of the matrix is not greater than 50.")
    


# In[ ]:


import numpy as np

def is_idempotent(matrix):
    product = np.dot(matrix, matrix)
    return np.array_equal(matrix, product)

def main():
    
    matrix = np.zeros((3, 3))
    
    print("Enter elements for the 3x3 matrix:")
    for i in range(3):
        for j in range(3):
            matrix[i][j] = float(input(f"Enter element at position ({i+1},{j+1}): "))

    if is_idempotent(matrix):
        print("The matrix is idempotent.")
    else:
        print("The matrix is not idempotent.")

if __name__ == "__main__":
    main()


# In[4]:


import math

def multiply(mat, res):

    N= len(mat)
    for i in range(0,N):
        for j in range(0,N):
            res[i][j] = 0
            for k in range(0,N):
                res[i][j] += mat[i][k] * mat[k][j]


def checkIdempotent(mat):

    N= len(mat)

    res =[[0]*N for i in range(0,N)]
    multiply(mat, res)

    for i in range(0,N):
        for j in range(0,N):
            if (mat[i][j] != res[i][j]):
                return False
    return True

mat = [ [2, -2, -4],
        [-1, 3, 4],
        [1, -2, -3] ]


if (checkIdempotent(mat)):
    print("Idempotent Matrix")
else:
    print("Not Idempotent Matrix.")



# In[7]:


class Matrix:
   def solve(self, matrix):
      if not matrix or not matrix[0]:
         return []
      n = len(matrix)
      for row in matrix:
         row.reverse()
      for i in range(n):
         for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i],
            matrix[i][j]
      return matrix
mx = Matrix()
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(mx.solve(matrix))


# In[9]:


def rotate_matrix(matrix):
    n = len(matrix)
    
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

   
    for i in range(n):
        matrix[i].reverse()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


rotate_matrix(matrix)


for row in matrix:
    print(" ".join(map(str, row)))


# In[3]:


def rotate_matrix(matrix):
    n = len(matrix)
    
  
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

 
    matrix.reverse()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


rotate_matrix(matrix)


for row in matrix:
    print(" ".join(map(str, row)))


# In[ ]:




