public class SMSNotification extends Notification {
    private String senderNumber;

    public SMSNotification() {
        super();
        this.senderNumber = "+0000000000";
    }

    public SMSNotification(String recipient, String senderNumber, String message) {
        super(recipient, message);
        this.senderNumber = senderNumber;
    }

    @Override
    public void send() {
        System.out.println("SMS from " + senderNumber +
            " to " + getRecipient() +
            ": " + getMessage());
    }

    @Override
    public void send(String priority) {
        System.out.println("[" + priority + "][SMS] from " + senderNumber +
            " to " + getRecipient() +
            ": " + getMessage());
    }

    @Override
    public void schedule() {
        System.out.println("SMS scheduled from " + senderNumber + " at default time.");
    }

    @Override
    public void schedule(String datetime) {
        System.out.println("SMS scheduled at " + datetime +
            " from " + senderNumber);
    }

    public String getSenderNumber() { return senderNumber; }
    public void setSenderNumber(String senderNumber) { this.senderNumber = senderNumber; }
}
