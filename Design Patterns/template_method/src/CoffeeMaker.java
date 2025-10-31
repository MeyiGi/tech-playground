public class CoffeeMaker extends BeverageMaker {
    @Override
    void addCondiments() {
        System.out.println("adding sugar and milk");
    }

    @Override
    void brew() {
        System.out.println("Dripping coffee through filter");
    }
}
