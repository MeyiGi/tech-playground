import javax.swing.*;
import java.awt.*;

public class View extends JFrame {
    private JTextField num1Field = new JTextField(10);
    private JTextField num2Field = new JTextField(10);
    private JTextField result = new JTextField(10);
    private JButton addButton = new JButton("add");
    private JButton substractButton = new JButton("substract");

    public View() {
        this.setTitle("Calculator");
        this.setLayout(new FlowLayout());
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        this.add(new JLabel("number 1: "));
        this.add(this.num1Field);

        this.add(new JLabel("number 2: "));
        this.add(this.num2Field);

        result.setEditable(false);
        this.add(new JLabel("result: "));
        this.add(result);

        this.add(addButton);
        this.add(substractButton);

        this.setSize(300, 200);
        this.setVisible(true);
    }

    public String getNum1() {
        return this.num1Field.getText();
    }

    public String getNum2() {
        return this.num2Field.getText();
    }

    public void setResult(String valueString) {
        this.result.setText(valueString);
    }

    public void addListener(java.awt.event.ActionListener listenForButton) {
        this.addButton.addActionListener(listenForButton);
    }

    public void substractListener(java.awt.event.ActionListener listForButton) {
        this.substractButton.addActionListener(listForButton);
    }

}
