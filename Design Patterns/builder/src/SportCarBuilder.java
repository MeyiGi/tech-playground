public class SportCarBuilder implements Builder {
    private Car car = new Car();

    @Override
    public void buildEngine() {
        car.setEngine("Sport Car Motor");
    }

    @Override
    public void buildGPS() {
        car.setGps(true);
    }

    @Override
    public void buildColor() {
        car.setColor("Orange");
    }

    @Override
    public void buildSeats() {
        car.setSeats(4);
    }

    @Override
    public Car getResult() {
        return this.car;
    }
}
