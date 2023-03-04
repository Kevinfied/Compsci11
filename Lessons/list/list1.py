"""
lists
a list is a variable that can hold multiple values.
These values can be of any type, even lists
"""
#
#
# nums = [12, 5, 6, 23]
# print(nums[0])    # not a list (int)
# print(nums[1:2])  # is a list
# nums[1] = 99      # NEW - you can assign to slices
# print(nums)
# nums[2:3] = [1,2,3,4]   # This is not used very often
# print(nums)
#
# rain = [0] * 7
# print(rain)
#
# rain = rain + [1, 1, 1]    # add lists
# print(rain)
#
# # Add and remove elements
# # Add - append
# nums = [0]
# nums.append(89)
# print(nums)
# # nums = nums + [89]   - slower
# # nums = [89} + nums
# nums.insert(0, 22)      # can insert anywhere
# print(nums)
#

nums = [12,99,99,6,23]
# remove based on value
nums.remove(99)      # removes ONLY the first one
print(nums)

# remove based on position
del nums[0]
print(nums)

print(nums.count(99))
print(nums.index(6))     # index is the find for lists (also works for strings)
                         # Index gie you the position of a value in the list
                         # Crashes if not there


print(len(nums))
print(sum(nums))
print(min(nums))
print(max(nums))
print(sum(nums) / len(nums))

for n in nums:
    n = n*2
    print("***",n)
print(nums)

# If i want to change the elements
for i in range(len(nums)):
    nums[i] *= 2
print(nums)

print(nums)
animals = ["dog","cat","Rat", "elk","bat","bee"]
animals.sort(reverse=True)
print(animals)
animals.reverse()
print(animals)
nums.reverse()
print(nums)
animal = animals.pop()
print(animal)
print(animals)




