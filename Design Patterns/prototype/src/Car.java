public class Car implements Prototype {
    private String model;
    private int wheels;
    private int seats;

    public Car() {
        super();
    }
    public Car(String model, int wheels, int seats) {
        this.model = model;
        this.wheels = wheels;
        this.seats = seats;
    }
    public Car(Car car) {
        this.model = car.model;
        this.wheels = car.wheels;
        this.seats = car.wheels;
    }

    // Getters
    public String getModel() {
        return model;
    }

    public int getWheels() {
        return wheels;
    }

    public int getSeats() {
        return seats;
    }

    // Setters
    public void setModel(String model) {
        this.model = model;
    }

    public void setWheels(int wheels) {
        this.wheels = wheels;
    }

    public void setSeats(int seats) {
        this.seats = seats;
    }

    // Clone method (Prototype pattern)
    @Override
    public Prototype clone() {
        return new Car(this.model, this.wheels, this.seats);
    }

    @Override
    public String toString() {
        return "Car{" +
                "model='" + model + '\'' +
                ", wheels=" + wheels +
                ", seats=" + seats +
                '}';
    }
}
