class Solution {
    public int[] twoSum(int[] nums, int target) {
        // put elements as key and its indices as values in a hash map
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        int diff;

        for (int j = 0; j < nums.length; j++) {
            diff = target - nums[j];
            if (map.containsKey(diff) &&  
                map.get( diff ) != j) {
                result[0] = j;
                result[1] = map.get( diff );
                return result;
            } else {                
                map.put(nums[j], j);
            }
        }

        return result;
    }
}