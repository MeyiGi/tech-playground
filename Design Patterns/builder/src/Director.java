public class Director {
    private Builder carBuilder;

    public Director(Builder carBuilder) {
        this.carBuilder = carBuilder;
    }

    public void construct() {
        this.carBuilder.buildColor();
        this.carBuilder.buildEngine();
        this.carBuilder.buildSeats();
        this.carBuilder.buildGPS();
    }
}
