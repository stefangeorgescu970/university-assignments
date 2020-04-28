package matrixarith;

import java.lang.reflect.Array;
import java.util.List;
import java.util.concurrent.*;
import java.util.function.BinaryOperator;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

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

    public T[][] addMatricesThreadPool(T[][] A, T[][] B, int numberOfThreads) throws IllegalArgumentException, IllegalStateException {
        if (add == null) {
            throw new IllegalStateException("No addition operation defined");
        }
        validateMatrix(A);
        validateMatrix(B);
        validateSameSizeMatrices(A, B);
        T[][] result = getZeroMatrix(A.length, A[0].length);
        List<Callable<Void>> callables = IntStream
                .range(0, numberOfThreads)
                .mapToObj(threadNumber -> (Callable<Void>) () -> {
                    addCells(A, B, result, threadNumber, numberOfThreads);
                    return null;
                })
                .collect(Collectors.toList());
        runThreadsInThreadPool(callables);
        return result;
    }


    public T[][] addMatricesFutures(T[][] A, T[][] B, int numberOfThreads) throws IllegalArgumentException, IllegalStateException {
        if (add == null) {
            throw new IllegalStateException("No addition operation defined");
        }
        validateMatrix(A);
        validateMatrix(B);
        validateSameSizeMatrices(A, B);
        T[][] result = getZeroMatrix(A.length, A[0].length);
        FutureTask<Void> futureTasks[] = new FutureTask[numberOfThreads];
        IntStream
                .range(0, numberOfThreads)
                .mapToObj(threadNumber -> new FutureTask<Void>(() -> {
                    addCells(A, B, result, threadNumber, numberOfThreads);
                    return null;
                }))
                .collect(Collectors.toList())
                .toArray(futureTasks);
        runFutureTasks(futureTasks);
        return result;
    }

    private void runThreadsInThreadPool(List<Callable<Void>> callables) {
        ExecutorService executor = Executors.newFixedThreadPool(callables.size());
        try {
            executor.invokeAll(callables);
            executor.shutdown();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
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

    public T[][] mulMatricesThreadPool(T[][] A, T[][] B, int numberOfThreads) throws IllegalArgumentException, IllegalStateException {
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
        FutureTask<Void> futureTasks[] = new FutureTask[numberOfThreads];
        IntStream
                .range(0, numberOfThreads)
                .mapToObj(threadNumber -> new FutureTask<Void>(() -> {
                    mulCells(A, B, result, threadNumber, numberOfThreads);
                    return null;
                }))
                .collect(Collectors.toList())
                .toArray(futureTasks);
        runFutureTasks(futureTasks);
        return result;
    }

    public T[][] mulMatricesFutures(T[][] A, T[][] B, int numberOfThreads) throws IllegalArgumentException, IllegalStateException {
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
        List<Callable<Void>> callables = IntStream
                .range(0, numberOfThreads)
                .mapToObj(threadNumber -> (Callable<Void>) () -> {
                    mulCells(A, B, result, threadNumber, numberOfThreads);
                    return null;
                })
                .collect(Collectors.toList());
        runThreadsInThreadPool(callables);
//        runThreads(threads);
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

    private void runFutureTasks(FutureTask<Void>[] futureTasks) {
        for (FutureTask<Void> futureTask : futureTasks) {
            (new Thread(futureTask)).start();
        }
        for (FutureTask<Void> futureTask : futureTasks) {
            try {
                futureTask.get();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }
        }
    }
}
