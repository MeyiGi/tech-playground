public interface Handler {
    void setNext(Handler handler);
    void process_request(String request);
}
