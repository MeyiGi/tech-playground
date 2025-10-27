public class Car {
    private String engine;
    private int seats;
    private String color;
    private boolean gps;

    public void setColor(String color) {
        this.color = color;
    }

    public void setGps(boolean gps) {
        this.gps = gps;
    }

    public void setEngine(String engine) {
        this.engine = engine;
    }

    public void setSeats(int seats) {
        this.seats = seats;
    }

    @Override
    public String toString() {
        return "Car{" +
                "engine='" + engine + '\'' +
                ", seats=" + seats +
                ", color='" + color + '\'' +
                ", gps=" + gps +
                '}';
    }
}
