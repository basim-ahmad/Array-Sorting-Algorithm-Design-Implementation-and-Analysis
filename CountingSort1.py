#!/usr/bin/env python
# coding: utf-8

# In[3]:


def CountingSort(A):
    n = len(A)
    C = [0] * n
    sorted_A = [0] * n

    # Count elements less than A[i]
    for i in range(n):
        for j in range(n):
            if A[j] < A[i]:
                C[i] += 1

    # Place elements at the correct position
    for i in range(n):
        sorted_A[C[i]] = A[i]

    # Copy back to the original array
    for i in range(n):
        A[i] = sorted_A[i]

# Example usage
import random
test_array = random.sample(range(-100, 100), 20)  # Generate 20 unique random numbers
print("Original Array:", test_array)
CountingSort(test_array)
print("Sorted Array:", test_array)


# In[ ]:





# In[ ]:




