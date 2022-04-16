class Solution(object):
    def twoSum(self, numbers, target):
        lp, rp = 0, len(numbers) - 1
        
        while lp < rp:
            res = numbers[lp] + numbers[rp]
            
            if res > target:
                rp -= 1
            elif res < target:
                lp += 1
            else:
                return [lp + 1, rp + 1]