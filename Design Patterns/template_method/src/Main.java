public class Main {
    public static void main(String[] args) {
        BeverageMaker teaMaker = new TeaMaker();
        teaMaker.makeBeverage();

        BeverageMaker coffeMaker = new CoffeeMaker();
        coffeMaker.makeBeverage();
    }
}