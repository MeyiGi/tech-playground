public class Main {
    public void main(String[] args) {
        // defining what kind of builder we want to instatiate product
        Builder sportCarBuilder = new SportCarBuilder();
        Builder suvCarBuilder = new SUVBuilder();

        // construction process
        Director sportCarDirector = new Director(sportCarBuilder);
        sportCarDirector.construct();
        Director suvCarDirector = new Director(suvCarBuilder);
        suvCarDirector.construct();

        // like that we can get result
        Car suvCar = suvCarBuilder.getResult();
        Car sportCar = sportCarBuilder.getResult();

        System.out.println(suvCar.toString());
        System.out.println(sportCar.toString());
    }
}