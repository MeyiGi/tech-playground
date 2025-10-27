public class BugattiBuilder implements Builder {
    private Car car = new Car();
    @Override
    public void model() {
        car.setModel("Bugatti");
    }

    @Override
    public void seats() {
        car.setSeats(4);
    }

    @Override
    public void wheels() {
        car.setWheels(4);
    }

    @Override
    public Car getResult() {
        return this.car;
    }


}
