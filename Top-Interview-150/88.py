from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        l1 = len(nums1)
        end = l1 - 1
        while n > 0 and m > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[end] = nums1[m-1]
                m -= 1
            else:
                nums1[end] = nums2[n-1]
                n -= 1
            end -= 1
        while n > 0:
            nums1[end] = nums2[n-1]
            n -= 1
            end -= 1
        

        
        
