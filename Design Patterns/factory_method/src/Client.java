public class Client {
    private Parser parser;

    public Client(ParserFactory factory) {
        this.parser = factory.createParser();
    }

    public Parser getParser() {
        return parser;
    }
}
