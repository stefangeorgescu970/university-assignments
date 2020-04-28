package ro.ubbcluj.ppd.lab6.multiplication.polynomial;

import ro.ubbcluj.ppd.lab6.utils.Utils;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class SimpleMul {

    public static int[] sequentialMultiplication(int[] a, int[] b) {
        int result[] = new int[a.length + b.length - 1];
        for (int k = 0; k < result.length; k++) {
            int sum = 0;
            int begin = (k < b.length ? 0 : k - b.length + 1);
            int end = Math.min(a.length, k + 1);
            for (int i = begin; i < end; i++) {
                sum += a[i] * b[k - i];
            }
            result[k] = sum;
        }
        return Utils.noLeadingZeros(result);
    }

    public static int[] parallelMultiplication(int a[], int b[], int numberOfThreads) {
        int result[] = new int[a.length + b.length - 1];
        List<Thread> threads = IntStream
                .range(0, numberOfThreads)
                .mapToObj(i -> new Thread(() -> oneThreadMul(i, numberOfThreads, a, b, result)))
                .collect(Collectors.toList());
        threads.forEach(t -> t.start());
        threads.forEach(t -> {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        return Utils.noLeadingZeros(result);
    }

    private static void oneThreadMul(int cell, int step, int a[], int b[], int result[]) {
        while (cell < result.length) {
            int sum = 0;
            int begin = (cell < b.length ? 0 : cell - b.length + 1);
            int end = Math.min(a.length, cell + 1);
            for (int i = begin; i < end; i++) {
                sum += a[i] * b[cell - i];
            }
            result[cell] = sum;
            cell += step;
        }
    }
}
