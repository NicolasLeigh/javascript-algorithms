class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                # 右半部分有序，最小值在左半部分，包括 mid
                right = mid
            else:
                # 最小值一定在 mid 右侧
                left = mid + 1

        return nums[left]