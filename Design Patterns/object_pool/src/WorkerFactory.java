public class WorkerFactory implements Factory<Worker> {
    public Worker create() {
        return new Worker();
    }
}
