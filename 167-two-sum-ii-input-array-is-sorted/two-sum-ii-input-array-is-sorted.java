class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int lPointer = 0;
        int rPointer = numbers.length -1;
        int sum;
        int [] sumIndex = new int[2];

        while (lPointer < rPointer) {
            sum = numbers[lPointer] + numbers[rPointer];

            if (sum < target) {
                lPointer = lPointer +1;
            } else if (sum > target) {
                rPointer = rPointer - 1;                
            } else {
                sumIndex[0] = lPointer + 1;
                sumIndex[1] = rPointer + 1;
                return sumIndex;
            }
        }

        return sumIndex;
    }
}