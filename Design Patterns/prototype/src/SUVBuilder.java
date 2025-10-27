public class SUVBuilder implements Builder {
    private Car car;
    @Override
    public void model() {
        car.setModel("SUV car");
    }

    @Override
    public void seats() {
        car.setSeats(6);
    }

    @Override
    public void wheels() {
        car.setWheels(8);
    }

    @Override
    public Car getResult() {
        return this.car;
    }
}
