public class AddTextCommand implements Command {
    private final TextEditor editor;
    private final String addToText;

    public AddTextCommand(TextEditor editor, String addToText) {
        this.addToText = addToText;
        this.editor = editor;
    }

    @Override
    public void execute() {
        editor.addText(addToText);
    }

    @Override
    public void undo() {
        editor.deleteText(addToText.length());
    }
}
