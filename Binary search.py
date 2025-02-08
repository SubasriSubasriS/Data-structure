class Solution(object):
    def search(self, nums, target):
        l = 0 
        r = len(nums) - 1

        while l <= r:  
            m = (l + r) // 2  

            if target == nums[m]:  
                return m  
            elif target > nums[m]:  
                l = m + 1
            else:  
                r = m - 1

        return -1 

solution = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = solution.search(nums, target)
print("Target found at index:", result) 
