class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();

        for (int each : nums) {
            if (set.add(each) == false) {
                return true;
            }
        }

        return false;

    }
}