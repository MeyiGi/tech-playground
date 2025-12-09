public class Main {
    public static void main(String[] args) {
        Document document = new Document("Hey hey!");
        History history = new History();

        document.write(" hello1");
        history.addMemento(document.saveMemento());
        document.write(" hello2");
        history.addMemento(document.saveMemento());
        document.write(" hello3");
        history.addMemento(document.saveMemento());

        document.restoreMemento(history.getMemento(1));

        System.out.println(document.getContent());
    }
}