public class EmailNotification extends Notification {
    private String subject;

    // Конструктор без параметров
    public EmailNotification() {
        super();
        this.subject = "No subject";
    }

    // Конструктор с параметрами
    public EmailNotification(String recipient, String subject, String message) {
        super(recipient, message);
        this.subject = subject;
    }

    // Overriding send()
    @Override
    public void send() {
        System.out.println("EMAIL to " + getRecipient() +
            " | Subject: " + subject +
            " | Body: " + getMessage());
    }

    // Overriding overloaded send()
    @Override
    public void send(String priority) {
        System.out.println("[" + priority + "][EMAIL] to " + getRecipient() +
            " | Subject: " + subject +
            " | Body: " + getMessage());
    }

    // Overriding schedule()
    @Override
    public void schedule() {
        System.out.println("Email scheduled with subject \"" + subject + "\" at default time.");
    }

    // Overriding overloaded schedule()
    @Override
    public void schedule(String datetime) {
        System.out.println("Email scheduled at " + datetime +
            " | Subject: " + subject);
    }

    // Геттер/сеттер для subject
    public String getSubject() { return subject; }
    public void setSubject(String subject) { this.subject = subject; }
}
