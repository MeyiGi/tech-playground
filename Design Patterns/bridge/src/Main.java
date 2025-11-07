public class Main {


    public static void main() {
        Shape circleShape = new CircleShape(new BlueColor(), 10.0);
        System.out.println(circleShape.getArea());

        Shape squareShape = new SquareShape(new RedColor(), 5.9);
        System.out.println(squareShape.getArea());
    }
}