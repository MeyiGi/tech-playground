// Client

public class Main {
    public static void main(String[] args) {
        TextEditor editor = new TextEditor();
        CommandManager commandManager = new CommandManager();
        
        commandManager.executeCommand(new AddTextCommand(editor, "hello "));
        System.out.println(editor.getText());
        
        commandManager.executeCommand(new AddTextCommand(editor, "world!"));
        System.out.println(editor.getText());

        commandManager.undo();
        System.out.println(editor.getText());

        commandManager.redo();
        System.out.println(editor.getText());



        commandManager.executeCommand(new DeleteTextCommand(editor, 6));
        System.out.println(editor.getText());

        commandManager.undo();
        System.out.println(editor.getText());

        commandManager.redo();
        System.out.println(editor.getText());
    }
}