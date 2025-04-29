from typing import List

testPath = "/Users/jinmingz/projects/NEU_Courses_Repo/Leetcode/L1_TwoSum/testFile.txt"


def readFile():
    f = open(testPath, 'r')
    lines = f.readlines()
    test_cases = []
    for l in lines:
        test_input = l.split(',')[0]
        result = l.split(',')[1]
        # [test_input, result] = l.split(',')
        test_cases.append((test_input, result))
    [print(i) for i in test_cases]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return []


def main():
    readFile()


if __name__ == '__main__':
    main()
