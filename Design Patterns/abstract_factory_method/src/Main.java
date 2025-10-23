public class Main {
    public static void main(String[] args) {
        GUIFactory factory = new MacFactory();

        Button button = factory.createButton();
        CheckBox checkBox = factory.createCheckBox();

        button.render();
        checkBox.render();
    }
}