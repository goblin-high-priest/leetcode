class Solution {
    int ROWS, COLS;
    boolean[][] path;

    public boolean exist(char[][] board, String word) {
        ROWS = board.length;
        COLS = board[0].length;
        path = new boolean[ROWS][COLS];

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                
                if (dfs(board, word, r, c, 0)) return true;
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, String word, int r, int c, int i) {
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        if (i == word.length()) return true;

        if (r < 0 || r >= ROWS || c < 0 || c >= COLS || path[r][c] || board[r][c] != word.charAt(i)) return false;

        path[r][c] = true;

        for (int[] dir : directions) {
            int dx = dir[0], dy = dir[1];

            if (dfs(board, word, r + dx, c + dy, i + 1)) {
                return true;
            }
        }

        path[r][c] = false;
        return false;
    }
}