class Solution {
    public int findMin(int[] nums) {
        int leftPointer = 0;
        int rightPointer = nums.length - 1 ;
        int lowest = nums[0];
        int midPointer;

        while (leftPointer < rightPointer) {
            midPointer = leftPointer + (int) Math.floor((rightPointer - leftPointer) / 2);
            if (nums[midPointer] > nums[rightPointer]) {
                leftPointer = midPointer + 1;
            }
            else {
                rightPointer = midPointer;
            }

            if (nums[midPointer] < lowest) {
                lowest = nums[midPointer];
            }            

        }

        return nums[leftPointer];
    }
}