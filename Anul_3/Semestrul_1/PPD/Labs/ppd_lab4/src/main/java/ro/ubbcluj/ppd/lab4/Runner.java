package ro.ubbcluj.ppd.lab4;

import java.lang.reflect.Array;
import java.util.List;
import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Created by Stefan on 5.11.2016.
 */
public class Runner {
    public static void main(String args[]) {
        (new Runner()).run();
    }

    private static final int MAX_MAT_SIZE = 20;
    private static final int MAX_MUL_SIZE = 10;

    private AtomicInteger nrThreadsThatNeedToLock;
    private Object threadLockedNotifier;

    private AtomicInteger nrThreadsThatNeedToFinishMul2;
    private Object threadFinishedNotifier;

    private ReentrantLock cellLocks[][];

    private List<Thread> mul1Threads;
    private List<Thread> mul2Threads;

    private void run() {
        Random rng = new Random();
        int m = rng.nextInt(MAX_MAT_SIZE) + 1;
        int n = rng.nextInt(MAX_MAT_SIZE) + 1;
        int p = rng.nextInt(MAX_MAT_SIZE) + 1;
        int q = rng.nextInt(MAX_MAT_SIZE) + 1;
        Integer A[][] = (Integer[][]) Array.newInstance(Integer.class, m, n);
        Integer B[][] = (Integer[][]) Array.newInstance(Integer.class, n, p);
        Integer C[][] = (Integer[][]) Array.newInstance(Integer.class, p, q);
        int i, j;
        for (i = 0; i < m; i++) {
            for (j = 0; j < n; j++) {
                A[i][j] = rng.nextInt(MAX_MUL_SIZE);
            }
        }
        for (i = 0; i < n; i++) {
            for (j = 0; j < p; j++) {
                B[i][j] = rng.nextInt(MAX_MUL_SIZE);
            }
        }
        for (i = 0; i < p; i++) {
            for (j = 0; j < q; j++) {
                C[i][j] = rng.nextInt(MAX_MUL_SIZE);
            }
        }

        System.out.println("FIRST MATRIX");
        printMat(A);
        System.out.println("SECOND MATRIX");
        printMat(B);
        System.out.println("THIRD MATRIX");
        printMat(C);

        int firstNumberOfThreads = rng.nextInt(m * p) + 1;
        int secondNumberOfThreads = rng.nextInt(m * q) + 1;

        Integer result[][] = mul3mat(A, B, C, firstNumberOfThreads, secondNumberOfThreads);

        System.out.println("RESULT MATRIX");
        printMat(result);

    }

    private Integer[][] mul3mat(Integer A[][], Integer B[][], Integer C[][], int firstNumberOfThreads, int secondNumberOfThreads) {
        int m = A.length;
        int p = C.length;
        int q = C[0].length;

        System.out.println("\nThe first multiplication is done on " + firstNumberOfThreads + " threads.");
        System.out.println("The second multiplication is done on " + secondNumberOfThreads + " threads.\n");

        Integer AB[][] = (Integer[][]) Array.newInstance(Integer.class, m, p);
        Integer result[][] = (Integer[][]) Array.newInstance(Integer.class, m, q);
        cellLocks = (ReentrantLock[][]) Array.newInstance(ReentrantLock.class, m, p);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < p; j++) {
                cellLocks[i][j] = new ReentrantLock();
                AB[i][j] = 0;
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < q; j++) {
                result[i][j] = 0;
            }
        }

        nrThreadsThatNeedToLock = new AtomicInteger(firstNumberOfThreads);
        threadLockedNotifier = new Object();

        nrThreadsThatNeedToFinishMul2 = new AtomicInteger(secondNumberOfThreads);
        threadFinishedNotifier = new Object();

        mul1Threads = IntStream
                .range(0, firstNumberOfThreads)
                .mapToObj((thNr) -> new Thread(() -> computeMul1(A, B, AB, thNr, firstNumberOfThreads)))
                .collect(Collectors.toList());

        mul1Threads.forEach(Thread::start);

        mul2Threads = IntStream
                .range(0, secondNumberOfThreads)
                .mapToObj((thNr) -> new Thread(() -> computeMul2(AB, C, result, thNr, secondNumberOfThreads)))
                .collect(Collectors.toList());

        while (true) {
            if (nrThreadsThatNeedToLock.get() <= 0) {
                break;
            }
            try {
                synchronized (threadLockedNotifier) {
                    threadLockedNotifier.wait();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        mul2Threads.forEach(Thread::start);

        while (true) {
            if (nrThreadsThatNeedToFinishMul2.get() <= 0) {
                break;
            }
            try {
                synchronized (threadFinishedNotifier) {
                    threadFinishedNotifier.wait();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        return result;

    }

    private void computeMul1(Integer A[][], Integer B[][], Integer AB[][], int initialPos, int stepSize) {
        int x;
        int y;
        int pos = initialPos;
        int totalX = AB.length;
        int totalY = AB[0].length;
        int totalCells = totalX * totalY;
        int totalInterm = B.length;
        while (pos < totalCells) {
            x = pos / totalY;
            y = pos % totalY;
            cellLocks[x][y].lock();
            pos += stepSize;
        }
        nrThreadsThatNeedToLock.decrementAndGet();
        synchronized (threadLockedNotifier) {
            threadLockedNotifier.notify();
        }
        pos = initialPos;
        while (pos < totalCells) {
            x = pos / totalY;
            y = pos % totalY;

            AB[x][y] = 0;
            for (int i = 0; i < totalInterm; i++) {
                AB[x][y] += A[x][i] * B[i][y];
            }

            cellLocks[x][y].unlock();
            pos += stepSize;
        }
    }

    private void computeMul2(Integer A[][], Integer B[][], Integer AB[][], int initialPos, int stepSize) {
        int x;
        int y;
        int pos = initialPos;
        int totalX = A.length;
        int totalY = A[0].length;
        int totalCells = totalX * totalY;

        while (pos < totalCells) {
            x = pos / totalY;
            y = pos % totalY;
            cellLocks[x][y].lock();


            for (int i = 0; i < B[0].length; i++) {
                AB[x][i] += A[x][y] * B[y][i];
            }

            cellLocks[x][y].unlock();
            pos += stepSize;
        }

        nrThreadsThatNeedToFinishMul2.decrementAndGet();
        synchronized (threadFinishedNotifier) {
            threadFinishedNotifier.notify();
        }
    }

    private void printMat(Integer mat[][]) {
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
    }
}
