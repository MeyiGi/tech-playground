public class JSONParserFactory implements ParserFactory{
    public Parser createParser() {
        return new JSONParser();
    }
}
