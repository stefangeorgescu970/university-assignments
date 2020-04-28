package main;

import bignummul.KaratsubaNumberMultiplication;
import polymul.KaratsubaMultiplication;
import polymul.SimplePolynomialsMultiplication;

import java.util.Random;

/**
 * Created by Sergiu on 12.11.2016.
 */
public class Engine {
    public static void main(String args[]) {
        (new Engine()).run();
    }

    private void run() {
//        System.out.println(polyToString(KaratsubaMultiplication.parallelMultiplication(new int[]{23, 2, 3}, new int[]{5, 8}, 1)));
        runPerformanceMeasures();
//        System.out.println(numberToString(KaratsubaNumberMultiplication.sequentialMultiplication(new int[]{1, 3, 5, 3, 2}, new int[]{1, 2, 3})));
//        int a[] = generatePolynomial(100, 10);
//        int b[] = generatePolynomial(100, 10);
//        polyToString(a);
//        polyToString(b);
//        int c[] = SimplePolynomialsMultiplication.
    }

    private String numberToString(int num[]) {
        String str = "";
        for (int i = num.length - 1; i >= 0; i--) {
            str += num[i];
        }
        return str;
    }

    private String polyToString(int poly[]) {
        String str = "";
        for (int i = 0; i < poly.length; i++) {
            str += (Math.signum(poly[i]) >= 0 ? "+ " : "- ") + Math.abs(poly[i]) + " * X^" + i + " ";
        }
        return str;
    }

    private void runPerformanceMeasures() {
        int valueLimit = 10;
//        int degrees[] = new int[]{1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 5000, 10000, 50000, 100000};
        int degrees[] = new int[]{4};
        int results[][] = new int[12 ][];

        System.out.println("Simple seq, Simple par 1, Simple par 4, Simple par 8, Simple par 16, Simple par 64, Simple par 128, "
                            + "Kara seq, Kara par 1, Kara par 4, Kara par 8, Kara par 16, Kara par 64, Kara par 128");

        for (int degree : degrees) {
            int a[] = generatePolynomial(degree, valueLimit);
            int b[] = generatePolynomial(degree, valueLimit);
            System.out.print(measureTime(() -> results[0] = SimplePolynomialsMultiplication.sequentialMultiplication(a, b)) + " ");
            System.out.print(measureTime(() -> results[1] = SimplePolynomialsMultiplication.parallelMultiplication(a, b, 1)) + " ");
            System.out.print(measureTime(() -> results[2] = SimplePolynomialsMultiplication.parallelMultiplication(a, b, 4)) + " ");
            System.out.print(measureTime(() -> results[3] = SimplePolynomialsMultiplication.parallelMultiplication(a, b, 8)) + " ");
            System.out.print(measureTime(() -> results[4] = SimplePolynomialsMultiplication.parallelMultiplication(a, b, 16)) + " ");
            System.out.print(measureTime(() -> results[4] = SimplePolynomialsMultiplication.parallelMultiplication(a, b, 64)) + " ");
            System.out.print(measureTime(() -> results[5] = SimplePolynomialsMultiplication.parallelMultiplication(a, b, 128)) + " ");
            System.out.print(measureTime(() -> results[6] = KaratsubaMultiplication.sequentialMultiplication(a, b)) + " ");
            System.out.print(measureTime(() -> results[7] = KaratsubaMultiplication.parallelMultiplication(a, b, 1)) + " ");
            System.out.print(measureTime(() -> results[8] = KaratsubaMultiplication.parallelMultiplication(a, b, 4)) + " ");
            System.out.print(measureTime(() -> results[9] = KaratsubaMultiplication.parallelMultiplication(a, b, 8)) + " ");
            System.out.print(measureTime(() -> results[4] = KaratsubaMultiplication.parallelMultiplication(a, b, 16)) + " ");
            System.out.print(measureTime(() -> results[10] = KaratsubaMultiplication.parallelMultiplication(a, b, 64)) + " ");
            System.out.print(measureTime(() -> results[11] = KaratsubaMultiplication.parallelMultiplication(a, b, 128)) + " ");
            System.out.print(checkSameValues(results));
            System.out.println();
            System.out.println(polyToString(a));
            System.out.println(polyToString(b));
            System.out.println(polyToString(results[0]));
        }
    }

    private String checkSameValues(int[][] results) {
        String res = polyToString(results[0]);
        for (int i = 1; i < results.length; i++) {
            if (!res.equals(polyToString(results[i]))) {
                return "results[0] != results[" + i + "]: " + res + " != " + polyToString(results[i]) + System.lineSeparator();
            }
        }
        return "";
    }

    private int[] generatePolynomial(int degree, int valueLimit) {
        Random rng = new Random();
        int poly[] = new int[degree + 1];
        for (int i = 0; i <= degree; i++) {
            poly[i] = rng.nextInt(valueLimit);
        }
        return poly;
    }

    private long measureTime(Runnable runnable) {
        long before = System.currentTimeMillis();
        runnable.run();
        return System.currentTimeMillis() - before;
    }
}
