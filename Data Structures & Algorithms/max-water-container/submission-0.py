# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         l, r= 0, len(heights)-1 #0, len(heights)-1
#         maxamount=0
#         while l<r: #while l<r:
#             contain = min(heights[l],heights[r] )*(r-l) 
#             maxamount=max(maxamount, contain)
#             if heights[l] <= heights[r]: #if heights[l] <= heights[r]:
#                 l+=1
#             else: #else:
#                 r-=1
#         return maxamount
class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r = 0, len(h)-1
        maxamount=0
        while l<r:
            contain=min(h[l],h[r])*(r-l)
            maxamount=max(maxamount, contain)
            if h[l]<=h[r]:
                l+=1
            else:
                r-=1
        return maxamount