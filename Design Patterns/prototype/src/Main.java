public class Main {
    public static void main(String[] args) {
        Builder bugattiBuilder = new BugattiBuilder();
        Director director = new Director(bugattiBuilder);
        director.construct();

        Car bugattiCar = bugattiBuilder.getResult();

        Car coppiedBugattiCar = new Car(bugattiCar);

        coppiedBugattiCar.setModel("Bugatti Pro+");

        System.out.println(bugattiCar);
        System.out.println(coppiedBugattiCar);
    }
}