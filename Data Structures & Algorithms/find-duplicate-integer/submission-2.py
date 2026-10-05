class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast=0,0
        while True:
            slow =nums[slow]
            fast =nums[nums[fast]]
            if slow == fast:
                break

        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow== slow2:
                return slow

        # s0,1,2 
        # f0,2,2 in cycle
        # break
        # s:2,3,2
        # s2:0,1,2
        #     2