class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer approach
        
        lpointer = 0
        rpointer = len(numbers)-1
        found = False

        while found == False:
            mynum = numbers[lpointer] + numbers[rpointer]
            if mynum > target:
                rpointer -= 1
            elif mynum < target:
                lpointer += 1
            elif mynum == target:
                return [lpointer + 1, rpointer + 1]
            
        

            
            
            