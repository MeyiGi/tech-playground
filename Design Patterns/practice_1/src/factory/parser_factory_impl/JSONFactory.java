package factory.parser_factory_impl;

import factory.ParserFactory;
import model.Parser;
import model.parser_impl.impl.JSONParser;

public class JSONFactory implements ParserFactory {
    @Override
    public Parser createParser() {
        return new JSONParser();
    }
}
