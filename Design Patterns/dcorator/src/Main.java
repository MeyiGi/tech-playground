public class Main {
    public static void MakeCoffee(Coffee coffee) {
        System.out.println("Description: " + coffee.getDescription());
        System.out.println("Cost: " + coffee.getCost() + "\n");
    }

    public static void main(String[] args) {
        PlainCoffee plainCoffee = new PlainCoffee();
        MakeCoffee(plainCoffee);

        MilkCoffee milkCoffee = new MilkCoffee(new PlainCoffee());
        MakeCoffee(milkCoffee);

        SugarCoffee sugarCoffee = new SugarCoffee(new MilkCoffee(new PlainCoffee()));
        MakeCoffee(sugarCoffee);
    }
}