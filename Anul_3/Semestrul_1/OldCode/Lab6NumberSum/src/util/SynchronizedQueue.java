package util;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by Sergiu on 19.11.2016.
 */
public class SynchronizedQueue {
    private Queue<Integer> queue;
    private boolean isClosed;
    private final Object mutex;
    private Object conditionalVariableReadyToConsume;

    public SynchronizedQueue() {
        queue = new LinkedList<>();
        isClosed = false;
        mutex = new Object();
        conditionalVariableReadyToConsume = new Object();
    }

    public Result dequeue() {
        synchronized (mutex) {
            while (true) {
                if (!queue.isEmpty()) {
                    Result result = new Result(true, queue.poll());
                    return result;
                }
                if (isClosed) {
                    return new Result(false, 0);
                }
                try {
//                    conditionalVariableReadyToConsume.wait();
                    mutex.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public void enqueue(int value) {
        synchronized (mutex) {
            queue.add(value);
//            conditionalVariableReadyToConsume.notify();
            mutex.notify();
        }
    }

    public void close() {
        synchronized (mutex) {
            isClosed = true;
//            conditionalVariableReadyToConsume.notifyAll();
            mutex.notifyAll();
        }
    }
}
