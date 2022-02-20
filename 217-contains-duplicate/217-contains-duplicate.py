class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        flag = False
        for i in nums:
            if i  not in visited:
                visited.add(i)
            else:
                flag = True
        return flag