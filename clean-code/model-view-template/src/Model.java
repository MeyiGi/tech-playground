public class Model {
    private char[][] board;
    private char currentPlayer;
    private boolean gameOver;
    private char winner; // 'X', 'O' или ' ' - если победителя нет

    public Model() {
        board = new char[3][3];
        resetBoard();
    }

    public char getCurrentPlayer() {
        return currentPlayer;
    }
    
    public boolean isGameOver() {
        return gameOver;
    }
    
    public char getWinner() {
        return winner;
    }

    // Метод для совершения хода в указанной ячейке
    public boolean makeMove(int row, int col) {
        if (board[row][col] == ' ' && !gameOver) {
            board[row][col] = currentPlayer;
            if (checkWin(currentPlayer)) {
                gameOver = true;
                winner = currentPlayer;
            } else if (isBoardFull()) {
                gameOver = true;
                winner = ' '; // ничья
            } else {
                // Переключаем игрока
                currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
            }
            return true;
        }
        return false;
    }

    public char getCell(int row, int col) {
        return board[row][col];
    }

    // Сброс игрового поля до начального состояния
    public void resetBoard() {
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                board[i][j] = ' ';
            }
        }
        currentPlayer = 'X';
        gameOver = false;
        winner = ' ';
    }

    // Проверка, заполнена ли доска полностью
    private boolean isBoardFull() {
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                if (board[i][j] == ' ') return false;
            }
        }
        return true;
    }

    // Проверка выигрышных комбинаций для указанного игрока
    private boolean checkWin(char player) {
        // Проверка строк и столбцов
        for (int i = 0; i < 3; i++){
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
                return true;
            if (board[0][i] == player && board[1][i] == player && board[2][i] == player)
                return true;
        }
        // Проверка диагоналей
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
            return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
            return true;
        return false;
    }
}