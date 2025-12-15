public class ConcreateObserver implements Observer {
    private String weather;

    @Override
    public void update(String message) {
        Object arg;
        if (message instanceof String) {
            this.weather = (String) message;
            display();
        }
    }

    public void display() {
        System.out.println("");
    }
}
