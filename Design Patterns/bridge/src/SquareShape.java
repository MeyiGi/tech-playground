public class SquareShape extends  Shape {
    private double length;

    public SquareShape(Color color, double length) {
        super(color);
        this.length = length;
    }

    @Override
    public void getShape() {
        System.out.println("it is very good square I'm beggin' you");
    }

    @Override
    public double getArea() {
        System.out.println("Calculating " + color.getColor() + " square");
        return length * length;
    }
}
