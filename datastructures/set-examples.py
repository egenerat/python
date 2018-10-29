# Set: unordered collection of unique elements

# Instantiate a set
first_set = {1, 2, 3}
print(first_set)

# Create an empty set
second_set = set()
print(second_set)

print(type(second_set))

# Be careful, {} creates a dictionary
not_a_set = {}
print(type(not_a_set))

# Add elements to a set
first_set.add(4)
print(first_set)

# Re-adding same element
first_set.add(4)
print(first_set)

# Check if element is in the set
print(4 in first_set)
print(5 in first_set)

# Remove element from the set
first_set.remove(2)
print(first_set)