class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # Moore's Voting Algorithm

        count = 0
        candidate = -1

        # step 1
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # step 2
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
        else:
            return -1


s = Solution()
m = s.majorityElement([3, 2, 3])
