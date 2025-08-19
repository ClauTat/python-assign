my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Initial List:", my_list)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print("After inserting 15:", my_list)

# Extend my_list with another list
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# Remove the last element from my_list
my_list.pop()
print("After removing the last element:", my_list)

# Sort my_list in ascending order
my_list.sort()
print("After sorting:", my_list)

# Find and print the index of the value 30 in my_list
index = my_list.index(30)
print("Index of 30:", index)