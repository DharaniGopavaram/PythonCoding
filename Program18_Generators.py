"""
The below program explains about generators.
Generators in Python are a powerful tool for creating iterators.
They allow you to iterate over a potentially large sequence of data
    without creating the entire sequence in memory at once.
This can be more memory-efficient and faster compared to traditional approaches,
    especially when dealing with large datasets.
"""

sample_list = [x * x for x in range(10000000000000000000000)]