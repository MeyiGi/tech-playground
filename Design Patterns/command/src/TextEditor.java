// Reciever

public class TextEditor {
    private StringBuilder text = new StringBuilder();

    public void addText(String newText) {
        text.append(newText);
    }

    public void deleteText(int length) {
        if (text.length() >= length) {
            text.delete(text.length() - length, text.length());
        } else {
            throw new IndexOutOfBoundsException("Length of text is less than provided to remove length");
        }

    }

    public String getText() {
        return text.toString();
    }
}
