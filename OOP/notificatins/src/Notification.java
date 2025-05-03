public abstract class Notification {
    private String recipient;
    private String message;

    // Конструктор без параметров
    public Notification() {
        this.recipient = "Unknown";
        this.message = "No message";
    }

    // Конструктор с параметрами
    public Notification(String recipient, String message) {
        this.recipient = recipient;
        this.message = message;
    }

    // Абстрактные методы
    public abstract void send();
    public abstract void send(String priority);
    public abstract void schedule();
    public abstract void schedule(String datetime);

    // Геттеры/сеттеры
    public String getRecipient() { return recipient; }
    public void setRecipient(String recipient) { this.recipient = recipient; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
}
