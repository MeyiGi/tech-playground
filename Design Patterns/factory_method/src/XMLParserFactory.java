public class XMLParserFactory implements ParserFactory{
    public Parser createParser() {
        return new XMLParser();
    }
}
