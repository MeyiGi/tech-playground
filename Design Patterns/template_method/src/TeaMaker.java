public class TeaMaker extends BeverageMaker {
    @Override
    void addCondiments() {
        System.out.println("Adding lemon to the tea");
    }

    @Override
    void brew() {
        System.out.println("Steeping the tea");
    }
}
