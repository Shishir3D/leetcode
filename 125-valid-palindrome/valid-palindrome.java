class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int n = s.length();
        char ch;
        char a = 'a';
        char z = 'z';
        char zero ='0';
        char nine = '9';
        String fwStr = "";
        String bwStr = "";

        for (int i = 0 ; i < n ; i++){
            ch = s.charAt(i);
            
            if ( //checking if it is alphanumeric
                ( (int) ch >= (int) a &&
                (int) ch <= (int) z ) ||
                ( (int) ch >= (int) zero &&
                (int) ch <= (int) nine )
                ) {
                    fwStr = fwStr + ch;
                    bwStr = ch + bwStr;
                }            
        }

        return fwStr.equals(bwStr);

    }
}