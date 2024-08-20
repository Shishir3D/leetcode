class Solution {
    public boolean isValid(String s) {
        // ({[]}) : valid
        int n = s.length();
        char[] chars = s.toCharArray();
        Stack<Character> stackk = new Stack<Character>();
        HashMap<Character, Character> map = new HashMap<>();
        
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        if (n % 2 != 0) return false;

        for (int i = 0; i < n; i++){
            char a = chars[i];
            if (a == '(' || a == '{' || a == '[') {
                stackk.push(a);
            } else { 
                if (stackk.isEmpty() || map.get(chars[i]) != stackk.pop()) {
                    return false;
                }
            }
        }

        return stackk.isEmpty();
    }
}