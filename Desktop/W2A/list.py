# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert value 15 at the second position
my_list.insert(1, 15)

# Extend the list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list
my_list.sort()

# Find and print the index of value 30
index_of_30 = my_list.index(30)
print(index_of_30)