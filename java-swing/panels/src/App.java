import java.awt.Color;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class App {
    public static void main(String[] args) throws Exception {
        ImageIcon icon = new ImageIcon("logo.png");
        System.out.println("Image width: " + icon.getIconWidth());
        System.out.println("Image height: " + icon.getIconHeight());

        JLabel label = new JLabel();
        label.setText("Hello World!");
        label.setIcon(icon);

        JPanel redPanel = new JPanel();
        redPanel.setBackground(Color.red);
        redPanel.setBounds(0, 0, 250, 250);

        JPanel bluePanel = new JPanel();
        bluePanel.setBackground(Color.blue);
        bluePanel.setBounds(250, 0, 250, 250);

        JPanel greenPanel = new JPanel();
        greenPanel.setBackground(Color.green);
        greenPanel.setBounds(0, 250, 500, 250);

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(750, 750);
        frame.setLayout(null);
        frame.setVisible(true);
        redPanel.add(label);
        frame.add(redPanel);
        frame.add(greenPanel);
        frame.add(bluePanel); 
    }
}
