class Solution(object):
    def containsDuplicate(self, nums):
        existed = {}
        for num in nums:
            if num not in existed:
                existed[num] = 1
            else:
                return True
        return False
                
        