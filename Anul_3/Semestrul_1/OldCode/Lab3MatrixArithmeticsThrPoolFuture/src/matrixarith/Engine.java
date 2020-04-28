package matrixarith;

import java.lang.reflect.Array;
import java.util.Random;

/**
 * Created by Sergiu on 14.10.2016.
 */
public class Engine {
    public static void main(String args[]) {
        (new Engine()).run();
    }

    private static final int MAX_MAT_SIZE = 100;
    private static final int MAX_ADD_SIZE = 100;
    private static final int MAX_MUL_SIZE = 10;

    private void run() {
        runAddition();
        runMultiplication();
    }

    private void runAddition() {
        Random rng = new Random();
        int x = rng.nextInt(MAX_MAT_SIZE) + 1;
        int y = rng.nextInt(MAX_MAT_SIZE) + 1;
        Integer A[][] = (Integer[][]) Array.newInstance(Integer.class, x, y);
        Integer B[][] = (Integer[][]) Array.newInstance(Integer.class, x, y);
        int i, j;
        for (i = 0; i < x; i++) {
            for (j = 0; j < y; j++) {
                A[i][j] = rng.nextInt(MAX_ADD_SIZE);
                B[i][j] = rng.nextInt(MAX_ADD_SIZE);
            }
        }
        MultiThreadMatrixArith<Integer> intMatArith = new MultiThreadMatrixArith<>(Integer.class, () -> 0);
        intMatArith.setAdd((a, b) -> a + b);

        printMat(A, "Matrix A(" + x + ", " + y + "):");
        printMat(B, "Matrix B(" + x + ", " + y + "):");
        printMat(intMatArith.addMatricesThreadPool(A, B, 1), "Addition result(" + x + ", " + y + "):");

        int resultMatSize = x * y;
        long before;
//        int noThr = rng.nextInt(resultMatSize) + 1;
        for (int noThr = 1; noThr <= resultMatSize; noThr++) {
            System.out.print("Add using " + noThr + " threads in a thread pool: ");
            before = System.currentTimeMillis();
            intMatArith.addMatricesThreadPool(A, B, noThr);
            System.out.println("" + (System.currentTimeMillis() - before) + " milliseconds");
            System.out.print("Add using " + noThr + " threads using future: ");
            before = System.currentTimeMillis();
            intMatArith.addMatricesFutures(A, B, noThr);
            System.out.println("" + (System.currentTimeMillis() - before) + " milliseconds");
        }
    }

    private void runMultiplication() {
        Random rng = new Random();
        int x = rng.nextInt(MAX_MAT_SIZE) + 1;
        int n = rng.nextInt(MAX_MAT_SIZE) + 1;
        int y = rng.nextInt(MAX_MAT_SIZE) + 1;
        Integer A[][] = (Integer[][]) Array.newInstance(Integer.class, x, n);
        Integer B[][] = (Integer[][]) Array.newInstance(Integer.class, n, y);
        int i, j;
        for (i = 0; i < x; i++) {
            for (j = 0; j < n; j++) {
                A[i][j] = rng.nextInt(MAX_MUL_SIZE);
            }
        }
        for (i = 0; i < n; i++) {
            for (j = 0; j < y; j++) {
                B[i][j] = rng.nextInt(MAX_MUL_SIZE);
            }
        }
        MultiThreadMatrixArith<Integer> intMatArith = new MultiThreadMatrixArith<>(Integer.class, () -> 0);
        intMatArith.setAdd((a, b) -> a + b);
        intMatArith.setMul((a, b) -> a * b);

        printMat(A, "Matrix A(" + x + ", " + n + "):");
        printMat(B, "Matrix B(" + n + ", " + y + "):");
//        printMat(intMatArith.mulMatrices(A, B, 1), "Multiplication result(" + x + ", " + y + "):");

        int resultMatSize = x * y;
        long before;
//        int noThr = rng.nextInt(resultMatSize) + 1;
        for (int noThr = 1; noThr <= resultMatSize; noThr++) {
            System.out.print("Multiply using " + noThr + " threads in a thread pool: ");
            before = System.currentTimeMillis();
            intMatArith.mulMatricesThreadPool(A, B, noThr);
            System.out.println("" + (System.currentTimeMillis() - before) + " milliseconds");
            System.out.print("Multiply using " + noThr + " threads using future: ");
            before = System.currentTimeMillis();
            intMatArith.mulMatricesFutures(A, B, noThr);
            System.out.println("" + (System.currentTimeMillis() - before) + " milliseconds");
        }
    }

    private <T>void printMat(T[][] mat, String message) {
        System.out.println(message);
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
    }
}
