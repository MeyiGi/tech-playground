public class Model {
    private int result;

    public int add(int x, int y) {
        this.result = x + y;
        return result;
    } 

    public int substract(int x, int y) {
        this.result = x - y;
        return result;
    }

    public int getResult() {
        return this.result;
    }

}
