package ro.ubbcluj.ppd.lab7.numerical_addition;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class NumberSequenceAdder {
    private int[] results;
    private int[] numbers;
    private List<Future<Integer>> partialSumFutures;

    private NumberSequenceAdder() {
    }

    public static int[] paralellAddNumbersSequence(int numbers[]) {
        NumberSequenceAdder adder = new NumberSequenceAdder();
        adder.results = new int[numbers.length];
        adder.numbers = numbers;
        ExecutorService executorService = Executors.newFixedThreadPool(adder.results.length);
        try {
            adder.partialSumFutures = executorService.invokeAll(
                    IntStream
                            .range(0, adder.results.length)
                            .mapToObj(numberIndex -> new Callable<Integer>() {
                                @Override
                                public Integer call() throws Exception {
                                    return adder.computePartialSumUpToIndex(numberIndex);
                                }
                            })
                            .collect(Collectors.toList())
            );
            for (int i = 0; i < adder.results.length; i++) {
                adder.results[i] = adder.partialSumFutures.get(i).get();
            }
            executorService.shutdown();
            return adder.results;
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        return null;
    }

    private int computePartialSumUpToIndex(int index) {
        int numberOfNumbers = index + 1;
        List<Future<Integer>> futures;
        List<Callable<Integer>> callables = new ArrayList<>();
        int rangeSize = 1;
        int lastIndexProcessed = index + 1;
        while (numberOfNumbers > 0) {
            int finalLastIndexProcessed = lastIndexProcessed;
            int finalRangeSize = rangeSize;
            if ((numberOfNumbers & 1) != 0) {
                callables.add(() -> computeSumBetweenIndexes(finalLastIndexProcessed - finalRangeSize, finalLastIndexProcessed - 1));
                lastIndexProcessed -= finalRangeSize;
            }
            numberOfNumbers /= 2;
            rangeSize *= 2;
        }
        ExecutorService executorService = Executors.newFixedThreadPool(callables.size());
        try {
            futures = executorService.invokeAll(callables);
            int result = futures.stream()
                    .mapToInt(future -> {
                        try {
                            return future.get();
                        } catch (InterruptedException | ExecutionException e) {
                            e.printStackTrace();
                        }
                        return 0;
                    })
                    .sum();
            executorService.shutdown();
            return result;
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return 0;
    }

    private int computeSumBetweenIndexes(int begin, int end) {
        if (begin == end) {
            return numbers[begin];
        }
        ExecutorService executorService = Executors.newFixedThreadPool(2);
        try {
            List<Future<Integer>> futures = executorService.invokeAll(
                    Stream.of(
                            (Callable<Integer>) () -> computeSumBetweenIndexes(begin, (end + begin) / 2),
                            () -> computeSumBetweenIndexes((end + begin) / 2 + 1, end))
                            .collect(Collectors.toList())
            );
            int result = futures.stream()
                    .mapToInt(future -> {
                        try {
                            return future.get();
                        } catch (InterruptedException | ExecutionException e) {
                            e.printStackTrace();
                        }
                        return 0;
                    })
                    .sum();
            executorService.shutdown();
            return result;
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return 0;
    }

    public static int[] sequentialAddNumbersSequence(int numbers[]) {
        int result[] = new int[numbers.length];
        result[0] = numbers[0];
        for (int i = 1; i < result.length; i++) {
            result[i] = result[i - 1] + numbers[i];
        }
        return result;
    }

    public static int sequentialAddNumbersInRange(int numbers[], int beginIndex, int afterLastIndex) {
        int result = 0;
        for (int i = beginIndex; i < afterLastIndex; i++) {
            result += numbers[i];
        }
        return result;
    }

    public static int[] sequentialBruteForceAddNumbersSequence(int numbers[]) {
        int result[] = new int[numbers.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = sequentialAddNumbersInRange(numbers, 0, i + 1);
        }
        return result;
    }
}
