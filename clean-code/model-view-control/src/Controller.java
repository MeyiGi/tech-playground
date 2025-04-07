import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Controller {
    private Model model;
    private View view;

    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;

        view.addListener(new AddButtonListener());
        view.substractListener(new SubstractButtonListener());
    }

    class AddButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            int num1 = Integer.parseInt(view.getNum1());
            int num2 = Integer.parseInt(view.getNum2());
            int result = model.add(num1, num2);
            view.setResult(String.valueOf(result));
        } 
    }

    class SubstractButtonListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            int num1 = Integer.parseInt(view.getNum1());
            int num2 = Integer.parseInt(view.getNum2());
            int result = model.substract(num1, num2);
            view.setResult(String.valueOf(result));
        }
    }
}