
nums = [2, 3, 4]
target = 7


hashed = {}


def two_sum(nums, target):
    for i in range(len(nums)):
        if target-nums[i] in hashed:
            print([hashed[target-nums[i]], i])
            return [hashed[target-nums[i]], i]

        hashed[nums[i]] = i


two_sum(nums, target)
print(hashed)

