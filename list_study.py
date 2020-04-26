members = ['uthay', 'prsanna', 'karthick']
members_master = members
print(members)  # print the entire list
print(members[0])  # print list items one by one
print(members[1])
print(members[2])
msg = "Hello!"
print(f"{msg},{members[0].title()}")
print(f"{msg},{members[1].title()}")
print(f"{msg},{members[2].title()}")
# Adding an element to the list
members.append('ratheesh')
print(members)

# Define an empty list
Grade = []

# removing items using del statement
del members[0]
print(members)

# Removing an Item Using the pop() Method
members.pop()
print(members)
members1 = members.pop(0)
print(members1)

# we can remove the items by value by remove command
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
