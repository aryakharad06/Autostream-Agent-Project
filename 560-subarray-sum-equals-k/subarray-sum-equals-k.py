class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        map = {0: 1}
        for num in nums:
            prefix += num
            remove = prefix - k
            count += map.get(remove, 0)
            map[prefix] = map.get(prefix, 0) + 1
        return count
        