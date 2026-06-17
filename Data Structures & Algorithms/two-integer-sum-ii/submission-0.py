class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(num)):
            if target-num[i] in mp:
                return [mp[target-num[i]], i+1]
            else:
                mp[num[i]]=i+1
        return []