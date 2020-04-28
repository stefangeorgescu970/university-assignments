package ro.ubbcluj.ppd.lab7.util;

import java.util.LinkedList;
import java.util.Queue;

public class SyncQueue {
    private Queue<Integer> queue;
    private boolean isClosed;
    private final Object mutex;
    private Object conditionalVariableReadyToConsume;

    public SyncQueue() {
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
