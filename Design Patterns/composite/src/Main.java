public class Main {
    public static void main() {
        TaskList projectTasks = new TaskList("Project tasks");
        projectTasks.addTask(new SimpleTask("Completing code"));
        projectTasks.addTask(new SimpleTask("Writing documentation"));

        TaskList firstStageTaskList = new TaskList("Phase 1 tasks");
        firstStageTaskList.addTask(new SimpleTask("Designing"));
        firstStageTaskList.addTask(new SimpleTask("Predicting Futures"));

        projectTasks.addTask(firstStageTaskList);
        projectTasks.displayTask();
    }
}