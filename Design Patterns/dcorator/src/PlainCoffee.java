public class PlainCoffee implements Coffee {
    @Override
    public Double getCost() {
        return 2.0;
    }

    @Override
    public String getDescription() {
        return "Plain Coffee";
    }
}
