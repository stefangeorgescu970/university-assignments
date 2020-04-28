package matrixarith;

import java.lang.reflect.Array;
import java.util.function.BinaryOperator;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Created by Sergiu on 14.10.2016.
 */
public final class MultiThreadMatrixArith<T> {
    private Class<T> clazz;
    private BinaryOperator<T> add;
    private BinaryOperator<T> mul;
    private Supplier<T> zero;

    public MultiThreadMatrixArith(Class<T> clazz, Supplier<T> zero) {
        this.clazz = clazz;
        this.zero = zero;
    }

    public void setAdd(BinaryOperator<T> add) {
        this.add = add;
    }

    public void setMul(BinaryOperator<T> mul) {
        this.mul = mul;
    }

    public T[][] addMatrices(T[][] A, T[][] B, int numberOfThreads) throws IllegalArgumentException, IllegalStateException {
        if (add == null) {
            throw new IllegalStateException("No addition operation defined");
        }
        validateMatrix(A);
        validateMatrix(B);
        validateSameSizeMatrices(A, B);
        T[][] result = getZeroMatrix(A.length, A[0].length);
        Thread threads[] = new Thread[numberOfThreads];
        IntStream
                .range(0, numberOfThreads)
                .mapToObj(threadNumber -> new Thread(() -> {
                    addCells(A, B, result, threadNumber, numberOfThreads);
                }))
                .collect(Collectors.toList())
                .toArray(threads);
        runThreads(threads);
        return result;
    }

    private void validateMatrix(T[][] mat) throws IllegalArgumentException {
        if (mat.length <= 0) {
            throw new IllegalArgumentException("Matrix must have at least one row");
        }
        int len = mat[0].length;
        if (len <= 0) {
            throw new IllegalArgumentException("Matrix must have at least one column");
        }
        for (int i = 1; i < mat.length; i++) {
            if (mat[i].length != len) {
                throw new IllegalArgumentException("A matrix must have the same number of columns on all rows");
            }
        }
    }

    private void validateSameSizeMatrices(T[][] A, T[][] B) {
        if (A.length != B.length) {
            throw new IllegalArgumentException("Matrices must have same number of rows");
        }
        if ((A.length > 0) && (A[0].length != B[0].length)) {
            throw new IllegalArgumentException("Matrices must have same number of columns");
        }
    }

    private T[][] getZeroMatrix(int rows, int cols) {
        T[][] zeroMat = (T[][]) Array.newInstance(clazz, rows, cols);
        for (int i = 0; i < zeroMat.length; i++) {
            for (int j = 0; j < zeroMat[i].length; j++) {
                zeroMat[i][j] = zero.get();
            }
        }
        return zeroMat;
    }

    private void addCells(T[][] A, T[][] B, T[][] result, int startCell, int step) {
        int sizeX = result.length;
        int sizeY = result[0].length;
        int totalSize = sizeX * sizeY;
        int x, y;
        for (int cell = startCell; cell < totalSize; cell += step) {
            x = cell / sizeY;
            y = cell % sizeY;
            result[x][y] = add.apply(A[x][y], B[x][y]);
        }
    }

    public T[][] mulMatrices(T[][] A, T[][] B, int numberOfThreads) throws IllegalArgumentException, IllegalStateException {
        if (add == null) {
            throw new IllegalStateException("No addition operation defined");
        }
        if (mul == null) {
            throw new IllegalStateException("No multiplication operation defined");
        }
        validateMatrix(A);
        validateMatrix(B);
        validateSizeForMulMatrices(A, B);
        T[][] result = getZeroMatrix(A.length, B[0].length);
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

    private void mulCells(T[][] A, T[][] B, T[][] result, int startCell, int step) {
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

    private void validateSizeForMulMatrices(T[][] A, T[][] B) throws IllegalArgumentException {
        if (A[0].length != B.length) {
            throw new IllegalArgumentException("The number of columns in the first matrix must be equal to the number of rows in the second");
        }
    }

    private void runThreads(Thread[] threads) {
        for (Thread thread: threads) {
            thread.start();
        }
        for (Thread thread: threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
