public class Level3Handler implements Handler {
    private Handler handler;
    @Override
    public void setNext(Handler handler) {
        this.handler = handler;
    }

    @Override
    public void process_request(String request) {
        if (request.equalsIgnoreCase("billing issue")) {
            System.out.println("Level3 support: Handling billing issue");
        } else if (handler != null) {
            handler.process_request(request);
        } else {
            System.out.println("No available handler for: " + request);
        }
    }
}
