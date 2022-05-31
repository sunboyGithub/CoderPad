class Solution:
    def threeSumSmaller(self, nums, target):
        '''05/31/22 O(N^2) sort, two pointer'''
        nums.sort()
        if len(nums) <= 2:
            return 0
        res = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums) -1
            ad_target = target - nums[i]
            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum < ad_target:
                    rr = r
                    while rr > l:
                        res.add((nums[i], nums[l], nums[rr]))
                        rr -= 1
                    l += 1
                elif cur_sum == ad_target:
                    r -= 1
                else: # cur_sum > ad_target
                    r -= 1
        return len(res)


test = Solution()
test_res = test.threeSumSmaller(nums = [-2,0,1,3], target = 2)
print(test_res)