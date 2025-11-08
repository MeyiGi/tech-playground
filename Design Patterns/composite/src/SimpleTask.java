public class SimpleTask implements Task {
    private final String title;

    public SimpleTask(String title) {
        this.title = title;
    }

    @Override
    public void displayTask() {
        System.out.println("Simple Task: " + title);
    }
}
