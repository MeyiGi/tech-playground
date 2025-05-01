public class Notification {
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

    // Перегрузка send(): без параметров
    public void send() {
        System.out.println("Sending generic notification to " + recipient + ": " + message);
    }

    // Перегрузка send(): с приоритетом
    public void send(String priority) {
        System.out.println("[" + priority + "] Sending generic notification to " + recipient + ": " + message);
    }

    // Перегрузка schedule(): без параметров
    public void schedule() {
        System.out.println("Scheduling generic notification at default time.");
    }

    // Перегрузка schedule(): с указанием времени
    public void schedule(String datetime) {
        System.out.println("Scheduling generic notification at " + datetime);
    }

    // Геттеры/сеттеры
    public String getRecipient() { return recipient; }
    public void setRecipient(String recipient) { this.recipient = recipient; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
}
