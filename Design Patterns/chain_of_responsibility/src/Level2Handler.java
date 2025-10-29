public class Level2Handler implements Handler {
    private Handler handler;
    @Override
    public void setNext(Handler handler) {
        this.handler = handler;
    }

    @Override
    public void process_request(String request) {
        if (request.equalsIgnoreCase("software issue")) {
            System.out.println("Level2 support: Handling software issue");
        } else if (handler != null) {
            handler.process_request(request);
        } else {
            System.out.println("No available handler for: " + request);
        }
    }
}
