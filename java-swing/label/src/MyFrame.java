import java.awt.Color;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class MyFrame extends JFrame {
    MyFrame() {
        this.setTitle("Hello world!");
        this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
        this.setResizable(false);
        // this.setSize(1000, 1000);
        this.setVisible(true);
        // ImageIcon image = new ImageIcon("logo.png");
        // System.out.println(image.getImage());
        // this.setIconImage(image.getImage());
        // this.getContentPane().setBackground(Color.white);
    }
}
