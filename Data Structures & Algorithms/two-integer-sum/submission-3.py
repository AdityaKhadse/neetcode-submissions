class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_m = {}
        for index, element in enumerate(nums):
            hash_m[element] = index
        
        print(hash_m)

        for index,element in enumerate(nums):
            req = target - element
            print("req:",req)
            if req in hash_m:
                print("index:", index)
                print("hash_m[req]:", hash_m[req])
                if index != hash_m[req]:
                    return [index,hash_m[req]]


                    