#!/usr/bin/env python
# coding: utf-8

# In[1]:


def CountingSortWithDuplicates(B):
    if not B:
        return

    min_element = min(B)
    max_element = max(B)
    range_of_elements = max_element - min_element + 1
    C = [0] * range_of_elements
    sorted_B = [0] * len(B)

    # Count each element's frequency
    for number in B:
        C[number - min_element] += 1

    # Convert frequencies to indices
    for i in range(1, range_of_elements):
        C[i] += C[i - 1]

    # Sort the elements
    for i in reversed(range(len(B))):
        sorted_B[C[B[i] - min_element] - 1] = B[i]
        C[B[i] - min_element] -= 1

    # Copy back to original array
    for i in range(len(B)):
        B[i] = sorted_B[i]

# Example usage
import random
test_array = [random.choice(range(-10, 11)) for _ in range(20)]  # Allow duplicates
print("Original Array:", test_array)
CountingSortWithDuplicates(test_array)
print("Sorted Array:", test_array)


# In[ ]:




