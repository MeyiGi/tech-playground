class Controller {
    private Model model;
    private View view;

    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;

        // Назначение обработчиков событий для каждой кнопки доски
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                final int row = i, col = j;
                view.addButtonListener(row, col, e -> handleMove(row, col));
            }
        }

        // Обработчик для кнопки перезапуска игры
        view.addResetListener(e -> resetGame());
    }

    // Обработка хода игрока
    private void handleMove(int row, int col) {
        if (model.makeMove(row, col)) {
            view.updateButton(row, col, model.getCell(row, col));
            if (model.isGameOver()) {
                if (model.getWinner() != ' ') {
                    view.setStatus("Player " + model.getWinner() + " wins!");
                } else {
                    view.setStatus("Draw!");
                }
            } else {
                view.setStatus("Player " + model.getCurrentPlayer() + "'s turn");
            }
        }
    }

    // Перезапуск игры
    private void resetGame() {
        model.resetBoard();
        view.resetBoard();
        view.setStatus("Player " + model.getCurrentPlayer() + "'s turn");
    }
}