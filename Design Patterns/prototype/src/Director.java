public class Director {
    Builder builder;

    public Director(Builder builder) {
        this.builder = builder;
    }

    public void construct() {
        this.builder.model();
        this.builder.seats();
        this.builder.wheels();
    }
}
