from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i == 0 or nums[i] != nums[i - 1]:
            low, high = i + 1, n - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s < 0:
                    low += 1
                elif s > 0:
                    high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
    return result

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    print("Unique triplets that sum to zero:")
    for triplet in result:
        print(triplet)