public abstract class BeverageMaker {
    void makeBeverage() {
        boilWater();// boilWater - default
        brew();// brew
        pourInCup();// pourInCup - default
        addCondiments();// addCondiments
    }

    abstract void brew();
    abstract void addCondiments();

    void boilWater() {
        System.out.println("Boiling the water");
    }
    void pourInCup() {
        System.out.println("pouring into cup");
    }
}
