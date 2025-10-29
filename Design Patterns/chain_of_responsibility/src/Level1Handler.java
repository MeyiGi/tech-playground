public class Level1Handler implements Handler {
    private Handler handler;
    @Override
    public void setNext(Handler handler) {
        this.handler = handler;
    }

    @Override
    public void process_request(String request) {
        if (request.equalsIgnoreCase("reset password")) {
            System.out.println("Level1 support: Handling reset password");
        } else if (handler != null) {
            handler.process_request(request);
        } else {
            System.out.println("No available handler for: " + request);
        }
    }
}
