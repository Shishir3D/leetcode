class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> countMap = new HashMap<>();

        for (char each : s.toCharArray()) {
            countMap.put(each, countMap.getOrDefault(each,0) + 1);            
        }

        for (char c : t.toCharArray()) {
            if (countMap.containsKey(c) == false) {
                return false;
            }

            countMap.put(c, countMap.get(c) - 1);

            if (countMap.get(c) == 0) {
                countMap.remove(c);
            }
        }

        return countMap.isEmpty();

        
    }
}