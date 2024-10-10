class Solution {
    public int findMin(int[] nums) {
        int leftPointer = 0;
        int rightPointer = nums.length - 1 ;
        int lowest = nums[0];

        while (leftPointer < rightPointer) {
            int midPointer = leftPointer + (rightPointer - leftPointer) / 2;
            if (nums[midPointer] > nums[rightPointer]) {
                leftPointer = midPointer + 1;
            }
            else {
                rightPointer = midPointer;
            }
        }

        return nums[leftPointer];
    }
}