public class SMSNotification extends Notification {
    private String senderNumber;

    // Конструктор без параметров
    public SMSNotification() {
        super();
        this.senderNumber = "+0000000000";
    }

    // Конструктор с параметрами
    public SMSNotification(String recipient, String senderNumber, String message) {
        super(recipient, message);
        this.senderNumber = senderNumber;
    }

    // Overriding send()
    @Override
    public void send() {
        System.out.println("SMS from " + senderNumber +
            " to " + getRecipient() +
            ": " + getMessage());
    }

    // Overriding overloaded send()
    @Override
    public void send(String priority) {
        System.out.println("[" + priority + "][SMS] from " + senderNumber +
            " to " + getRecipient() +
            ": " + getMessage());
    }

    // Overriding schedule()
    @Override
    public void schedule() {
        System.out.println("SMS scheduled from " + senderNumber + " at default time.");
    }

    // Overriding overloaded schedule()
    @Override
    public void schedule(String datetime) {
        System.out.println("SMS scheduled at " + datetime +
            " from " + senderNumber);
    }

    // Геттер/сеттер для senderNumber
    public String getSenderNumber() { return senderNumber; }
    public void setSenderNumber(String senderNumber) { this.senderNumber = senderNumber; }
}
