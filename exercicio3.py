class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)

        start = 0
        end = x

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX < x else float('inf')

            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY < y else float('inf')

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                end = partitionX - 1

            else:
                start = partitionX + 1


nums1 = [1,3]
nums2 = [2]
nums3 = [1,2]
nums4 = [3,4]

s = Solution()
result = s.findMedianSortedArrays(nums1, nums2)
print(f"merged array = {sorted(nums1 + nums2)} and median is {result}")

result1 = s.findMedianSortedArrays(nums3, nums4)
print(f"merged array = {sorted(nums3 + nums4)} and median is {result1}")