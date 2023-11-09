#!/usr/bin/env python
# coding: utf-8

# In[3]:


input_arr = input("Enter an array")


digit_counts = {}
for digit in input_arr:
    if digit.isdigit():
        digit_counts[digit] = digit_counts.get(digit, 0) + 1


output_arr = ""
for digit in sorted(digit_counts.keys()):
    count = digit_counts[digit]
    output_arr += count * digit


output_arr = "0" * (len(input_arr) - len(output_arr)) + output_arr

print(output_arr)


# In[1]:


def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1

    count = [0] * range_of_elements

    for num in arr:
        count[num - min_value] += 1

    sorted_array = []
    for i in range(range_of_elements):
        while count[i] > 0:
            sorted_array.append(i + min_value)
            count[i] -= 1

    return sorted_array

array = [1, 1, 0, 0, 2, 2, 0, 0, 1, 0, 2, 0, 1]
sorted_array = counting_sort(array)
print(sorted_array)


# In[1]:


input_string = 'vedith raavi'

words = input_string.split()

capitalized_words = [word.capitalize() for word in words]
result_string = ' '.join(capitalized_words)

print(result_string)


# In[ ]:




