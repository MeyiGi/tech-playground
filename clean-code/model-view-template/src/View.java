import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class View extends JFrame {
    private JButton[][] buttons;
    private JButton btnReset;
    private JLabel lblStatus;

    public View() {
        setTitle("Tic Tac Toe MVC");
        setSize(400, 450);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Панель для игрового поля (3х3 кнопки)
        JPanel boardPanel = new JPanel();
        boardPanel.setLayout(new GridLayout(3, 3));
        buttons = new JButton[3][3];

        Font buttonFont = new Font("Arial", Font.BOLD, 60);
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                buttons[i][j] = new JButton("");
                buttons[i][j].setFont(buttonFont);
                boardPanel.add(buttons[i][j]);
            }
        }
        add(boardPanel, BorderLayout.CENTER);

        // Панель для управления игрой: статус и кнопка перезапуска
        JPanel controlPanel = new JPanel(new BorderLayout());

        lblStatus = new JLabel("Player X's turn");
        lblStatus.setHorizontalAlignment(SwingConstants.CENTER);
        lblStatus.setFont(new Font("Arial", Font.PLAIN, 20));
        controlPanel.add(lblStatus, BorderLayout.CENTER);

        btnReset = new JButton("Restart Game");
        controlPanel.add(btnReset, BorderLayout.SOUTH);

        add(controlPanel, BorderLayout.SOUTH);
    }

    // Обновление текста кнопки (установка символа в ячейке)
    public void updateButton(int row, int col, char player) {
        buttons[row][col].setText(String.valueOf(player));
    }

    // Обновление информационного лейбла состояния игры
    public void setStatus(String status) {
        lblStatus.setText(status);
    }

    // Сброс интерфейса игрового поля
    public void resetBoard() {
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                buttons[i][j].setText("");
            }
        }
    }

    // Добавление слушателя для конкретной кнопки (ячейки доски)
    public void addButtonListener(int row, int col, ActionListener listener) {
        buttons[row][col].addActionListener(listener);
    }

    // Добавление слушателя для кнопки перезапуска игры
    public void addResetListener(ActionListener listener) {
        btnReset.addActionListener(listener);
    }
}