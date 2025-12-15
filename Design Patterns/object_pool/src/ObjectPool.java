import java.util.ArrayList;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingDeque;
import java.util.concurrent.BlockingQueue;

public class ObjectPool<T> {
    private final BlockingQueue<T> pool;

    ObjectPool(int size, Factory<T> factory) {
        pool = new ArrayBlockingQueue<>(size);

        for (int i = 0; i < size; i++) {
            pool.add(factory.create());
        }
    }

    public T acquire() throws InterruptedException{
        return pool.take();
    }


    public void put(T obj) throws InterruptedException {
        pool.put(obj);
    }
}
