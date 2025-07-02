def second_largest_sorted(nums):
    if len(nums) < 2:
        return None
    nums_sorted = sorted(nums)
    return nums_sorted[-2]

print(second_largest_sorted([10, 20, 4, 45, 99]))  # → 45

