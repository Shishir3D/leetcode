class Solution {
    public int[] productExceptSelf(int[] nums) 
    {
        int n = nums.length;
        int [] result = new int[n];
        int curr = 1;

        Arrays.fill(result, 1);

        for(int i = 0; i < n; i++) {
            result[i] *= curr;
            curr *= nums[i];
        }
        curr = 1;
        for(int i = n - 1; i >= 0; i--) {
            result[i] *= curr;
            curr *= nums[i];
        }

        return result;
    }
}