#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Matrix Operation

# In[3]:


def matrix_op():
    # Ensure to handle input conversion correctly
    rows = int(input('Enter number of rows: '))
    cols = int(input('Enter number of cols: '))
    Matrix = []

    for i in range(rows):
        # Collect each row from user input
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        Matrix.append(row)

    np_matrix = np.array(Matrix)
    return np_matrix

# Example usage:
matrix1 = matrix_op()
print('Matrix1:')
print(matrix1)
print()

matrix2 = matrix_op()
print('Matrix2:')
print(matrix2)


# # Matrix Addition

# In[6]:


print('Matrix Addittion :')
matrix3=matrix1 + matrix2
print(matrix3)


# # Matrix Subtraction
# 

# In[8]:


print('Matrix Subtraction: ')
matrix3=matrix1 - matrix2
print(matrix3)


# # Matrix Multiplication

# In[9]:


print('Matrix Multiplication: ')
matrix3=np.dot(matrix1,matrix2)
print(matrix3)


# In[ ]:




