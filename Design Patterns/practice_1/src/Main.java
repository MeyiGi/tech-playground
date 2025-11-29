import factory.ParserFactory;
import factory.parser_factory_impl.JSONFactory;
import factory.parser_factory_impl.XMLFactory;
import model.Parser;

class Main {
    public static Parser getParser(ParserFactory factory) {
        return factory.createParser();
    }
    public static void main(String[] args) {
        JSONFactory jsonFactory = new JSONFactory();
        XMLFactory xmlFactory = new XMLFactory();

        Parser parser = Main.getParser(jsonFactory);
        parser.scrapeWebpage();
    }
}