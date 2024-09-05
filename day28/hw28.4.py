# Import the reduce function from functools
from functools import reduce

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the product of the list elements
product = reduce(lambda x, y: x * y, numbers)

# Print the result
print("Product of elements:", product)