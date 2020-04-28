package main;

import numadd.BigNumberSequenceAdder;
import numadd.NumberSequenceAdder;

import java.util.Random;

/**
 * Created by Sergiu on 17.11.2016.
 */
public class Engine {
    public static void main(String args[]) {
        (new Engine()).run();
    }

    private void run() {
//        performanceMeasurementsNumSeq();
//        performanceMeasurementsBigNum();
        someTests();
    }

    private int[] generateNumberSequence(int size, int maxValue) {
        Random rng = new Random();
        int sequence[] = new int[size];
        for (int i = 0; i < size; i++) {
            sequence[i] = rng.nextInt(maxValue);
        }
        return sequence;
    }

    private void printNumberSequence(int sequence[]) {
        for (int i : sequence) {
            System.out.print("" + i + " ");
        }
    }

    private void printBigNumber(int bigNumber[]) {
        for (int digit : bigNumber) {
            System.out.print(digit);
        }
    }

    private void performanceMeasurementsNumSeq() {
        int numbersOfNumbers[] = {2, 10, 16, 32, 50, 100, 150, 200, 256, 500};
        System.out.println("Brute Force, Sequential, Parallel");
        for (int numberOfNumbers : numbersOfNumbers) {
            int numbers[] = generateNumberSequence(numberOfNumbers, 10000);
            System.out.print(measureTime(() ->  NumberSequenceAdder.sequentialBruteForceAddNumbersSequence(numbers)) + " ");
            System.out.print(measureTime(() ->  NumberSequenceAdder.sequentialAddNumbersSequence(numbers)) + " ");
            System.out.print(measureTime(() ->  NumberSequenceAdder.paralellAddNumbersSequence(numbers)) + " ");
            System.out.println();
        }
    }

    private long measureTime(Runnable runnable) {
        long before = System.currentTimeMillis();
        runnable.run();
        return System.currentTimeMillis() - before;
    }

    private void performanceMeasurementsBigNum() {
        int numbersOfNumbers[] = {2, 50, 100, 150, 200, 256, 500, 1000, 2000, 10000};
        int maxNumbersOfDigits[] = {5, 100, 150, 200, 300, 400, 500, 1000, 2000, 10000};
        for (int numberOfNumbers : numbersOfNumbers) {
            for (int maxNumberOfDigits : maxNumbersOfDigits) {
                int numbers[][] = generateBigNumbers(numberOfNumbers, maxNumberOfDigits);
                System.out.print(measureTime(() ->  BigNumberSequenceAdder.parallelAddBigNumberSequence(numbers)) + " ");
            }
            System.out.println();
        }
    }

    private int[][] generateBigNumbers(int numberOfNumbers, int maxNumberOfDigits) {
        int numbers[][] = new int[numberOfNumbers][];
        Random rng = new Random();
        for (int i = 0; i < numberOfNumbers; i++) {
            int numberOfDigits = Math.max(maxNumberOfDigits / 2, rng.nextInt(maxNumberOfDigits));
            numbers[i] = new int[numberOfDigits];
            for (int j = 0; j < numberOfDigits - 1; j++) {
                numbers[i][j] = rng.nextInt(10);
            }
            numbers[i][numberOfDigits - 1] = 1 + rng.nextInt(9);
        }
        return numbers;
    }

    private void someTests() {

//        int numbers[] = generateNumberSequence(100, 100);
        int numbers[] = new int[] {
                12432,
                1234532,
                13123412,
                548994433,
                124243434,
                895397,
                124234231,
                1234321,
                98795657,
                587688987
        };
        printNumberSequence(NumberSequenceAdder.paralellAddNumbersSequence(numbers));
        System.out.println();
        printNumberSequence(NumberSequenceAdder.sequentialAddNumbersSequence(numbers));
        System.out.println();
        printNumberSequence(NumberSequenceAdder.sequentialBruteForceAddNumbersSequence(numbers));
        int bigNumbers[][] = new int[][] {
                new int[] {1, 2, 4, 3, 2},
                new int[] {1, 2, 3, 4, 5, 3, 2},
                new int[] {1,3,1,2,3,4,1,2},
                new int[] {5,4,8,9,9,4,4,3,3},
                new int[] {1,2,4,2,4,3,4,3,4},
                new int[] {8,9,5,3,9,7},
                new int[] {1,2,4,2,3,4,2,3,1},
                new int[] {1,2,3,4,3,2,1},
                new int[] {9,8,7,9,5,6,5,7},
                new int[] {5,8,7,6,8,8,9,8,7}
        };
        System.out.println();
        printBigNumber(BigNumberSequenceAdder.parallelAddBigNumberSequence(bigNumbers));
    }
}
