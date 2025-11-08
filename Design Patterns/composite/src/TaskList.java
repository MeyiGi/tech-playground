import java.util.ArrayList;
import java.util.List;

public class TaskList implements Task {
    private String title;
    private List<Task> tasks = new ArrayList<>();

    public TaskList(String title) {
        this.title = title;
    }

    public void addTask(Task task) {
        this.tasks.add(task);
    }

    public void removeTask(Task task) {
        this.tasks.remove(task);
    }

    @Override
    public void displayTask() {
        System.out.println("Task List: " + title);
        for (Task task : tasks) {
            task.displayTask();
        }
    }
}
