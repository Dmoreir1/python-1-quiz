# create a function that given a list of numbers (positive or negative integers),
# it will return a list containing the indices of the two highest values. Order of the returned indices does not matter.

def max_values(nums):
  # max_val = []
  # for i in nums:
  #   max(range(len(nums)))
  #
  # max_val.append(i)



  x = max(range(len(nums)))
  return x

# print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
print(max_values([-5, -2, -1, -11])) # -> [1, 2]

## for loop that takes the highest index and adds to a list, then repeat for 2nd highest number