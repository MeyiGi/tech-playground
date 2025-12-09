public class Document {
    private String content;

    public Document(String content) {
        this.content = content;
    }

    public void write(String content) {
        this.content += content;
    }

    public String getContent() {
        return this.content;
    }

    public DocumentMemento saveMemento() {
        return new DocumentMemento(content);
    }

    public void restoreMemento(DocumentMemento memento) {
        this.content = memento.getSavedMemento();
    }
}
