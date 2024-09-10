import java.util.HashSet;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = 9;

        // Check for rows and columns
        for (int i = 0; i < n; i++) {
            HashSet<Character> rowElements = new HashSet<>();
            HashSet<Character> columnElements = new HashSet<>();

            for (int j = 0; j < n; j++) {
                // Check for row duplicates
                if (board[i][j] != '.' && !rowElements.add(board[i][j])) {
                    return false;
                }
                // Check for column duplicates
                if (board[j][i] != '.' && !columnElements.add(board[j][i])) {
                    return false;
                }
            }
        }

        // Check for 3x3 sub-grids
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                HashSet<Character> gridElements = new HashSet<>();

                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        char current = board[row * 3 + i][col * 3 + j];
                        if (current != '.' && !gridElements.add(current)) {
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }
}
