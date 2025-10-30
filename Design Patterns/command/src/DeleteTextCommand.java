public class DeleteTextCommand implements Command {
    private final TextEditor editor;
    private String deletedText;
    private final int length;

    public DeleteTextCommand(TextEditor editor, int length) {
        this.length = length;
        this.editor = editor;
    }

    @Override
    public void execute() {
        String current = editor.getText();
        this.deletedText = current.substring(current.length() - this.length);
        editor.deleteText(this.length);
    }

    @Override
    public void undo() {
        editor.addText(deletedText);
    }
}
