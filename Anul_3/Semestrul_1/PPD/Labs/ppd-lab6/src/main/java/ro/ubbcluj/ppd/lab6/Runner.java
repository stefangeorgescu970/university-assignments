package ro.ubbcluj.ppd.lab6;

import ro.ubbcluj.ppd.lab6.multiplication.polynomial.KaratsubaMul;
import ro.ubbcluj.ppd.lab6.multiplication.polynomial.SimpleMul;

import java.util.Random;

public class Runner {
    public static void main(String args[]) {
        (new Runner()).run();
    }

    private void run() {
        runPerformanceMeasures();
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
        int degrees[] = new int[]{4};
        int results[][] = new int[12 ][];

        System.out.println("Simple seq, Simple par 1, Simple par 4, Simple par 8, Simple par 16, Simple par 64, Simple par 128, "
                + "Kara seq, Kara par 1, Kara par 4, Kara par 8, Kara par 16, Kara par 64, Kara par 128");

        for (int degree : degrees) {
            int a[] = generatePolynomial(degree, valueLimit);
            int b[] = generatePolynomial(degree, valueLimit);
            System.out.print(measureTime(() -> results[0] = SimpleMul.sequentialMultiplication(a, b)) + " ");
            System.out.print(measureTime(() -> results[1] = SimpleMul.parallelMultiplication(a, b, 1)) + " ");
            System.out.print(measureTime(() -> results[2] = SimpleMul.parallelMultiplication(a, b, 4)) + " ");
            System.out.print(measureTime(() -> results[3] = SimpleMul.parallelMultiplication(a, b, 8)) + " ");
            System.out.print(measureTime(() -> results[4] = SimpleMul.parallelMultiplication(a, b, 16)) + " ");
            System.out.print(measureTime(() -> results[4] = SimpleMul.parallelMultiplication(a, b, 64)) + " ");
            System.out.print(measureTime(() -> results[5] = SimpleMul.parallelMultiplication(a, b, 128)) + " ");
            System.out.print(measureTime(() -> results[6] = KaratsubaMul.sequentialMultiplication(a, b)) + " ");
            System.out.print(measureTime(() -> results[7] = KaratsubaMul.parallelMultiplication(a, b, 1)) + " ");
            System.out.print(measureTime(() -> results[8] = KaratsubaMul.parallelMultiplication(a, b, 4)) + " ");
            System.out.print(measureTime(() -> results[9] = KaratsubaMul.parallelMultiplication(a, b, 8)) + " ");
            System.out.print(measureTime(() -> results[4] = KaratsubaMul.parallelMultiplication(a, b, 16)) + " ");
            System.out.print(measureTime(() -> results[10] = KaratsubaMul.parallelMultiplication(a, b, 64)) + " ");
            System.out.print(measureTime(() -> results[11] = KaratsubaMul.parallelMultiplication(a, b, 128)) + " ");
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
