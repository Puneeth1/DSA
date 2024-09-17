nums = [1, 2, 3]

# Brute Force : O(2^n * n) -> Iterating n digits for 2^n times
possible_subsets = 2 ** len(nums)
subsets = []
# 0 to 2^(n-1)
for i in range(possible_subsets):
    # bin(2) --> 0b10
    # The zfill(n) function pads the binary string with leading zeros until its length is n.This ensures that every binary string used for subset generation has exactly n bits
    binary_value = bin(i)[2:].zfill(len(nums))
    subset = []
    for j in range(len(nums)):
        if int(binary_value[j]):
            subset.append(nums[j])
    subsets.append(subset)
print(subsets)