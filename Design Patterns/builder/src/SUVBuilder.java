public class SUVBuilder implements Builder {
    private Car car = new Car();

    @Override
    public void buildEngine() {
        car.setEngine("Suv Car Motor");
    }

    @Override
    public void buildGPS() {
        car.setGps(false);
    }

    @Override
    public void buildColor() {
        car.setColor("blue");
    }

    @Override
    public void buildSeats() {
        car.setSeats(6);
    }

    @Override
    public Car getResult() {
        return this.car;
    }
}
