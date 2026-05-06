class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        my_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_map:
                y = my_map[diff]
                ans.append(y)
                ans.append(i)
            else:
                my_map[nums[i]] = i
        return ans