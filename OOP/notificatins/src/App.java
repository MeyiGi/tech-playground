public class App {
    public static void main(String[] args) {
        Notification email = new EmailNotification("alice@example.com", "Meeting Reminder", "Don't forget at 10 AM");
        Notification sms   = new SMSNotification("Bob", "+123456789", "Your code is ready");

        Notification[] notifications = { email, sms };

        for (Notification n : notifications) {
            // Polymorphism + Overriding + Overloading
            n.send();
            n.send("HIGH");               // перегружённый метод
            n.schedule();
            n.schedule("2025-05-02 09:00");
            System.out.println();
        }
    }
}
