public class Main {
    public static void main(String[] args) {
        JSONParserFactory jsonParserFactory = new JSONParserFactory();
        XMLParserFactory xmlParserFactory = new XMLParserFactory();

        Client userWithJSON = new Client(jsonParserFactory);
        Client userWithXML = new Client(xmlParserFactory);

        Parser jsonParser = userWithJSON.getParser();
        Parser xmlParser = userWithXML.getParser();

        jsonParser.parse();
        xmlParser.parse();
    }
}