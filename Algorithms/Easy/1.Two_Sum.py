def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i


nums = list(map(int, input("Enter the list of numbers: ").split()))
target = int(input("Enter the target number: "))
print(two_sum(nums, target))
