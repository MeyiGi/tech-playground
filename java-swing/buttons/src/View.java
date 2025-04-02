import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;

public class View extends JFrame {
    JButton button;
    public View() {
        button = new JButton();
        button.setBounds(200, 100, 100, 50);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(500, 500);
        this.setLayout(null);
        this.setVisible(true);
        this.add(button);
    }

    public void addButtonListener(ActionListener listener) {
        button.addActionListener(listener);
    }
}