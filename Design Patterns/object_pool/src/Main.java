public class Main {
  public static void main(String[] args) throws InterruptedException {
    WorkerFactory workerFactory = new WorkerFactory();
    ObjectPool<Worker> pool = new ObjectPool<>(2, workerFactory);

    Worker w1 = pool.acquire();
    Worker w2 = pool.acquire();

    w1.doWork();
    w2.doWork();

    w1.doWork();
    pool.put(w1);
    pool.put(w2);
  }
}