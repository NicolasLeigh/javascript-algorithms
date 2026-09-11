class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid + 1]:
                # 上坡，峰值在右边
                left = mid + 1
            else:
                # 下坡，峰值在左边，包括 mid
                right = mid

        return left