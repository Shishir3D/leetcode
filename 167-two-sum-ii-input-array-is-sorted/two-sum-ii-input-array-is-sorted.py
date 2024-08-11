class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer approach

        lpointer = 0
        rpointer = len(numbers)-1

        while lpointer < rpointer:
            mynum = numbers[lpointer] + numbers[rpointer]
            if mynum > target:
                rpointer -= 1
            elif mynum < target:
                lpointer += 1
            else:
                return [lpointer + 1, rpointer + 1]
            
        

            
            
            