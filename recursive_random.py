import random

# Define a list of items
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Pick four random items from the list and create a new list
new_list = [random.choice(my_list) for i in range(10000)]

# Pick a random item from the new list
final_item = random.choice(new_list)

# Print the final item
print(random.choice(my_list))
