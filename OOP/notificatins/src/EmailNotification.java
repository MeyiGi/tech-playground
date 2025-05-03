public class EmailNotification extends Notification {
    private String subject;

    public EmailNotification() {
        super();
        this.subject = "No subject";
    }

    public EmailNotification(String recipient, String subject, String message) {
        super(recipient, message);
        this.subject = subject;
    }

    @Override
    public void send() {
        System.out.println("EMAIL to " + getRecipient() +
            " | Subject: " + subject +
            " | Body: " + getMessage());
    }

    @Override
    public void send(String priority) {
        System.out.println("[" + priority + "][EMAIL] to " + getRecipient() +
            " | Subject: " + subject +
            " | Body: " + getMessage());
    }

    @Override
    public void schedule() {
        System.out.println("Email scheduled with subject \"" + subject + "\" at default time.");
    }

    @Override
    public void schedule(String datetime) {
        System.out.println("Email scheduled at " + datetime +
            " | Subject: " + subject);
    }

    public String getSubject() { return subject; }
    public void setSubject(String subject) { this.subject = subject; }
}
