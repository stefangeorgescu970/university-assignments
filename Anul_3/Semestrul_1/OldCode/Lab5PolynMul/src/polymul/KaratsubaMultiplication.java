package polymul;

import util.Utils;

import java.util.Arrays;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.FutureTask;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created by Sergiu on 12.11.2016.
 */
public class KaratsubaMultiplication {
    private KaratsubaMultiplication() {}

    public static int[] sequentialMultiplication(int[] a, int[] b) {
        int result[] = internalSequentialMultiplication(a, b);
        return Utils.noLeadingZeros(result);
    }

    private static int[] internalSequentialMultiplication(int a[], int b[]) {
        if (a.length < 2 || b.length < 2) {
            return SimplePolynomialsMultiplication.sequentialMultiplication(a, b);
        }
        int m = Math.max(a.length, b.length);
        int halfPoint = m / 2;

        int highA[] = Arrays.copyOfRange(a, halfPoint, a.length);
        int lowA[] = Arrays.copyOfRange(a, 0, halfPoint);
        int highB[] = Arrays.copyOfRange(b, halfPoint, a.length);
        int lowB[] = Arrays.copyOfRange(b, 0, halfPoint);

        int p[] = sequentialMultiplication(lowA, lowB);
        int q[] = sequentialMultiplication(polyAdd(lowA, highA), polyAdd(lowB, highB));
        int r[] = sequentialMultiplication(highA, highB);

        return polyAdd(polyAdd(polyShift(r, 2 * halfPoint), polyShift(polySub(polySub(q, r), p), halfPoint)), p);
    }

    public static int[] parallelMultiplication(int[] a, int[] b, int numberOfThreads) {
        AtomicInteger numberOfremainingThreads = new AtomicInteger(numberOfThreads);
        int result[] = internalParallelMultiplication(a, b, numberOfremainingThreads);
        return Utils.noLeadingZeros(result);
    }

    private static int[] internalParallelMultiplication(int a[], int b[], AtomicInteger numberOfRemainingThreads) {
        if (a.length < 2 || b.length < 2) {
            return SimplePolynomialsMultiplication.sequentialMultiplication(a, b);
        }
        int m = Math.max(a.length, b.length);
        int halfPoint = m / 2;

        int highA[] = Arrays.copyOfRange(a, halfPoint, a.length);
        int lowA[] = Arrays.copyOfRange(a, 0, halfPoint);
        int highB[] = Arrays.copyOfRange(b, halfPoint, a.length);
        int lowB[] = Arrays.copyOfRange(b, 0, halfPoint);

        FutureTask<int[]> pf = null, qf = null, rf = null;
        if (numberOfRemainingThreads.get() > 0) {
            numberOfRemainingThreads.decrementAndGet();
            pf = new FutureTask<int[]>(new Callable<int[]>() {
                @Override
                public int[] call() throws Exception {
                    return internalParallelMultiplication(lowA, lowB, numberOfRemainingThreads);
                }
            });

            (new Thread(pf)).start();
        }

        if (numberOfRemainingThreads.get() > 0) {
            numberOfRemainingThreads.decrementAndGet();
            qf = new FutureTask<int[]>(new Callable<int[]>() {
                @Override
                public int[] call() throws Exception {
                    return internalParallelMultiplication(polyAdd(lowA, highA), polyAdd(lowB, highB), numberOfRemainingThreads);
                }
            });

            (new Thread(qf)).start();
        }

        if (numberOfRemainingThreads.get() > 0) {
            numberOfRemainingThreads.decrementAndGet();
            rf = new FutureTask<int[]>(new Callable<int[]>() {
                @Override
                public int[] call() throws Exception {
                    return internalParallelMultiplication(highA, highB, numberOfRemainingThreads);
                }
            });

            (new Thread(rf)).start();
        }

        int p[] = null, q[] = null, r[] = null;

        if (pf == null) {
            p = internalParallelMultiplication(lowA, lowB, numberOfRemainingThreads);
        }
        if (qf == null) {
            q = internalParallelMultiplication(polyAdd(lowA, highA), polyAdd(lowB, highB), numberOfRemainingThreads);
        }
        if (rf == null) {
            r = internalParallelMultiplication(highA, highB, numberOfRemainingThreads);
        }

        try {
            if (pf != null) {
                p = pf.get();
                numberOfRemainingThreads.incrementAndGet();
            }
            if (qf != null) {
                q = qf.get();
                numberOfRemainingThreads.incrementAndGet();
            }
            if (rf != null) {
                r = rf.get();
                numberOfRemainingThreads.incrementAndGet();
            }

        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }


        return polyAdd(polyAdd(polyShift(r, 2 * halfPoint), polyShift(polySub(polySub(q, r), p), halfPoint)), p);
    }

    private static int[] polyAdd(int a[], int b[]){
        int limit = Math.max(a.length, b.length);
        int result[] = new int[limit];
        if (a.length == limit) {
            while (limit > b.length) {
                result[limit - 1] = a[limit - 1];
                limit--;
            }
        } else {
            while (limit > a.length) {
                result[limit - 1] = b[limit - 1];
                limit--;
            }
        }
        for (int i = 0; i < limit; i++) {
            result[i] = a[i] + b[i];
        }
        return result;
    }



    private static int[] polyShift(int a[], int positions) {
        int result[] = new int[a.length + positions];
        for (int i = result.length - 1; i >= positions; i--) {
            result[i] = a[i - positions];
        }
        return result;
    }

    private static int[] polySub(int a[], int b[]) {
        int limit = Math.max(a.length, b.length);
        int result[];
        if (a.length == b.length) {
            while (limit > 1 && a[limit - 1] == b[limit - 1]) {
                limit--;
            }
            result = new int[limit];
        } else {
            result = new int[limit];
            if (a.length == limit) {
                while (limit > b.length) {
                    result[limit - 1] = a[limit - 1];
                    limit--;
                }
            } else {
                while (limit > a.length) {
                    result[limit - 1] = b[limit - 1];
                    limit--;
                }
            }
        }
        for (int i = limit - 1; i >= 0; i--) {
            result[i] = a[i] - b[i];
        }
        return result;
    }

}
