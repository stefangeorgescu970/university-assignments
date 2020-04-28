package ro.ubbcluj.ppd.lab2;

import ro.ubbcluj.ppd.lab2.model.MatrixMathUtil;

import java.lang.reflect.Array;
import java.util.Random;

public class Runner {

    public static void main(String[] args) {
        (new Runner()).run();
    }

    private static final int MAX_MAT_SIZE = 1000;
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
        MatrixMathUtil intMatArith = new MatrixMathUtil();

        printMat(A, "Matrix A(" + x + ", " + y + "):");
        printMat(B, "Matrix B(" + x + ", " + y + "):");
        printMat(intMatArith.addMatrices(A, B, 1), "Addition result(" + x + ", " + y + "):");

        int resultMatSize = x * y;
        long before;
        for (int noThr = 1; noThr <= resultMatSize; noThr++) {
            System.out.print("Add using " + noThr + " threads: ");
            before = System.currentTimeMillis();
            intMatArith.addMatrices(A, B, noThr);
            System.out.println((System.currentTimeMillis() - before) + " milliseconds");
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
        MatrixMathUtil intMatArith = new MatrixMathUtil();

        printMat(A, "Matrix A(" + x + ", " + n + "):");
        printMat(B, "Matrix B(" + n + ", " + y + "):");
        printMat(intMatArith.mulMatrices(A, B, 1), "Multiplication result(" + x + ", " + y + "):");

        int resultMatSize = x * y;
        long before;
        for (int noThr = 1; noThr <= resultMatSize; noThr++) {
            System.out.print("Multiply using " + noThr + " threads: ");
            before = System.currentTimeMillis();
            intMatArith.mulMatrices(A, B, noThr);
            System.out.println((System.currentTimeMillis() - before) + " milliseconds");
        }
    }

    private void printMat(Integer[][] mat, String message) {
        System.out.println(message);
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
    }
}
