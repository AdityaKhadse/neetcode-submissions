class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_m = {}
        for index, element in enumerate(nums):
            hash_m[element] = index

        for index,element in enumerate(nums):
            req = target - element
            if req in hash_m:
                if index != hash_m[req]:
                    return [index,hash_m[req]]


