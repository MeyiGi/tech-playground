public class CircleShape extends Shape {
    private final double radios;

    public CircleShape(Color color, Double radios) {
        super(color);
        this.radios = radios;
    }

    @Override
    public void getShape() {
        System.out.println("It is fucking cirle shape");
    }

    @Override
    public double getArea() {
        System.out.println("Calculating " + color.getColor() + " circle");
        return 3.14*radios*radios;
    }
}
