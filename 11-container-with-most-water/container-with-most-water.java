class Solution {
    public int maxArea(int[] height) {
        int lPointer = 0;
        int rPointer = height.length - 1;
        int area = -1;
        int length;
        int breadth;
        int maxArea = 0;
        int lHeight;
        int rHeight;

        while(lPointer < rPointer) {
            length = rPointer - lPointer;
            lHeight = height[lPointer];
            rHeight = height[rPointer];

            // min height of wall
            if (lHeight < rHeight) {
                breadth = lHeight;
            } else {
                breadth = rHeight;
            }

            area = length * breadth;

            // setting the max Area
            if (area > maxArea) {
                maxArea = area;
            }

            // moving the bigger wall
            if (lHeight < rHeight){
                lPointer++;
            } else {
                rPointer--;
            }
        }
        
        return maxArea;
    }
}