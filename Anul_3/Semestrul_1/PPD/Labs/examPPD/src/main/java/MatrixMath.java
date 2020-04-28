import java.lang.reflect.Array;
import java.util.Random;
import java.util.function.BinaryOperator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class MatrixMath {

    private BinaryOperator<Integer> add = (a, b) -> a + b;
    private BinaryOperator<Integer> mul = (a, b) -> a * b;

    void runMultiplication() {
        Random rng = new Random();
        int x = rng.nextInt(100) + 1;
        int n = rng.nextInt(100) + 1;
        int y = rng.nextInt(100) + 1;
        Integer A[][] = (Integer[][]) Array.newInstance(Integer.class, x, n);
        Integer B[][] = (Integer[][]) Array.newInstance(Integer.class, n, y);
        int i, j;
        for (i = 0; i < x; i++) {
            for (j = 0; j < n; j++) {
                A[i][j] = rng.nextInt(100);
            }
        }
        for (i = 0; i < n; i++) {
            for (j = 0; j < y; j++) {
                B[i][j] = rng.nextInt(100);
            }
        }


        printMat(A, "Matrix A(" + x + ", " + n + "):");
        printMat(B, "Matrix B(" + n + ", " + y + "):");
        printMat(this.mulMatrices(A, B, 1), "Multiplication result(" + x + ", " + y + "):");

        int resultMatSize = x * y;
        long before;
        for (int noThr = 1; noThr <= resultMatSize; noThr++) {
            System.out.print("Multiply using " + noThr + " threads: ");
            before = System.currentTimeMillis();
            this.mulMatrices(A, B, noThr);
            System.out.println((System.currentTimeMillis() - before) + " milliseconds");
        }
    }

    private Integer[][] mulMatrices(Integer[][] A, Integer[][] B, int numberOfThreads) throws IllegalArgumentException, IllegalStateException {
        Integer[][] result = getZeroMatrix(A.length, B[0].length);
        Thread threads[] = new Thread[numberOfThreads];
        IntStream
                .range(0, numberOfThreads)
                .mapToObj(threadNumber -> new Thread(() -> {
                    mulCells(A, B, result, threadNumber, numberOfThreads);
                }))
                .collect(Collectors.toList())
                .toArray(threads);
        runThreads(threads);
        return result;
    }

    private void mulCells(Integer[][] A, Integer[][] B, Integer[][] result, int startCell, int step) {
        int sizeX = result.length;
        int sizeY = result[0].length;
        int n = B.length;
        int totalSize = sizeX * sizeY;
        int x, y;
        for (int cell = startCell; cell < totalSize; cell += step) {
            x = cell / sizeY;
            y = cell % sizeY;
            for (int i = 0; i < n; i++) {
                result[x][y] = add.apply(result[x][y], mul.apply(A[x][i], B[i][y]));
            }
        }
    }

    private void runThreads(Thread[] threads) {
        for (Thread thread : threads) {
            thread.start();
        }
        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private Integer[][] getZeroMatrix(int rows, int cols) {
        Integer[][] zeroMat = (Integer[][]) Array.newInstance(Integer.class, rows, cols);
        for (int i = 0; i < zeroMat.length; i++) {
            for (int j = 0; j < zeroMat[i].length; j++) {
                zeroMat[i][j] = 0;
            }
        }
        return zeroMat;
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
