from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_dict = {}
        for position, number in enumerate(nums):
            result = target - number
            if result in lookup_dict:
                return [lookup_dict[result], position]
            lookup_dict[number] = position


if __name__ == "__main__":
    assert (TwoSum().twoSum([2, 7, 11, 15], 9) == [0, 1])
    assert (TwoSum().twoSum([6, 4, 19, 1, 0, 11], 15) == [1, 5])
