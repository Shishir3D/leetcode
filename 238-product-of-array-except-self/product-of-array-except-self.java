class Solution {
    public int[] productExceptSelf(int[] nums) {
        // create a suffix and prefix array
        // each index in suffix array will contain the product 
        // of all the elements that are to the left of the suffix (not inclusive)
        // elements in prefix is the same as suffix but have product of elements to the right (not inc)
        // multiply suffix and prefix at every index to get the answer

        ArrayList<Integer> suffix = new ArrayList<>();
        ArrayList<Integer> prefix = new ArrayList<>();
        int n = nums.length;
        int [] result = new int[n];

        for (int i = 0; i < n; i++) {
            suffix.add(1);
            prefix.add(1);
        }

        for (int j = 1; j < n; j++) {
            suffix.set(j, suffix.get(j-1) * nums[j-1]);
        } 

        for (int k = n-2; k > -1; k--) {
            prefix.set(k, prefix.get(k+1) * nums[k+1]);
        }
        
        for (int l = 0; l < n; l++) {
            result[l] = suffix.get(l) * prefix.get(l);
        }

        return result;
    }
}