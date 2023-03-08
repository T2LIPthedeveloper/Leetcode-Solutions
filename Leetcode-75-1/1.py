class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end, index_list = 0, len(nums)-1, [i for i in range(len(nums))]

        # list is unsorted
        # sort the list
        self.list_sorter(index_list, nums)

        # find the two numbers that add up to the target
        while start < end:
            if nums[start] + nums[end] == target:
                return [index_list[start], index_list[end]]
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        
    def list_sorter(self, index_list, nums):
        for i in range(len(nums)):
            current = nums[i]
            current_index = index_list[i]
            j = i - 1
            while j >= 0 and nums[j] > current:
                nums[j+1] = nums[j]
                index_list[j+1] = index_list[j]
                j -= 1
            nums[j+1] = current
            index_list[j+1] = current_index
