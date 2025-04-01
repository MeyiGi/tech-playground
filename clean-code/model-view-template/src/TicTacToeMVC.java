import javax.swing.*;

public class TicTacToeMVC {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Model model = new Model();
            View view = new View();
            new Controller(model, view);
            view.setVisible(true);
        });
    }
}