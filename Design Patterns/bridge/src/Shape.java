public abstract class Shape {
    protected Color color;

    public Shape(Color color) {
        this.color = color;
    }
    public Color getColor() {
        return color;
    }

    public abstract void getShape();
    public abstract double getArea();
}
