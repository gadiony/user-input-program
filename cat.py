# 1. Create an empty list
my_list = []

# 2. Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)  # [10, 20, 30, 40]

# 3. Insert 15 at second position (index 1)
my_list.insert(1, 15)
print("After inserting 15:", my_list)  # [10, 15, 20, 30, 40]

# 4. Extend with another list
my_list.extend([50, 60, 70])
print("After extending:", my_list)  # [10, 15, 20, 30, 40, 50, 60, 70]

# 5. Remove last element
my_list.pop()
print("After removing last element:", my_list)  # [10, 15, 20, 30, 40, 50, 60]

# 6. Sort in ascending order
my_list.sort()
print("After sorting:", my_list)  # [10, 15, 20, 30, 40, 50, 60]

# 7. Find index of 30
index = my_list.index(30)
print("Index of 30:", index)  # 