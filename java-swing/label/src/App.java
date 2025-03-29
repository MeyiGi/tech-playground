import java.awt.Color;
import java.awt.Font;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.border.Border;

public class App {
    public static void main(String[] args) throws Exception {
        
        Border border = BorderFactory.createLineBorder(Color.green, 3);

        ImageIcon image = new ImageIcon("logo.png");
        JLabel label = new JLabel();
        label.setText("Hello world!");
        label.setForeground(new Color(252, 20, 173));
        label.setFont(new Font("MV Boli", Font.ITALIC, 20));
        label.setIcon(image);
        label.setHorizontalTextPosition(JLabel.CENTER);
        label.setVerticalTextPosition(JLabel.TOP);
        label.setBackground(Color.BLACK);
        label.setOpaque(true);
        label.setBorder(border);
        label.setVerticalAlignment(JLabel.CENTER);
        label.setHorizontalAlignment(JLabel.CENTER);
        label.setBounds(0, 0, 700, 700);

        MyFrame frame = new MyFrame();
        frame.add(label);
        // frame.setLayout(null);
        frame.pack();

    }
}