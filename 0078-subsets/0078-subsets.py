class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sub = []
        result = []
        def seq(i):

            if i==len(nums):
                result.append(sub.copy())
                return

            sub.append(nums[i])
            seq(i+1)

            sub.pop()
            seq(i+1)
        
        seq(0)
        return result

