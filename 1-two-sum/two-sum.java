class Solution {
    public int[] twoSum(int[] nums, int target) {
        // put elements as key and its indices as values in a hash map
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for (int j = 0; j < nums.length; j++) {
            
            if (map.containsKey(target - nums[j]) &&  
                map.get( target - nums[j] ) != j) {
                result[0] = j;
                result[1] = map.get( target - nums[j] );
                return result;
            }
        }

        return result;

    }
}