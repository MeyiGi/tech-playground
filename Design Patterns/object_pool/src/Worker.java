public class Worker {
    private int overallWorkedHours = 0;

    public void doWork() {
        overallWorkedHours += 2;
        System.out.println(System.identityHashCode(this) + " object worked overall: " + overallWorkedHours);
    }
}
