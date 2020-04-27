# This script  shows the examples for lists
# example 1

my_foods = ['rice', 'dosa', 'sambar']
friends_favourite = my_foods
print(friends_favourite)  # output :['rice', 'dosa', 'sambar']
my_foods.append('idly')
print(friends_favourite)  # ['rice', 'dosa', 'sambar', 'idly']
# Notes :
# the above example my_foods and friends favourite are same list . If appending a value
# in one list the same will show another list

# example 2
my_foods = ['rice', 'dosa', 'sambar']
friends_favourite = my_foods[:]
print(friends_favourite)  # output :['rice', 'dosa', 'sambar']
my_foods.append('idly')
print(friends_favourite)  # output :['rice', 'dosa', 'sambar']

# in the above example , Both list are different
