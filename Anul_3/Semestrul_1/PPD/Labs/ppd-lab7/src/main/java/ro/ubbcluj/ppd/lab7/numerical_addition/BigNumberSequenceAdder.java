package ro.ubbcluj.ppd.lab7.numerical_addition;

import ro.ubbcluj.ppd.lab7.util.Result;
import ro.ubbcluj.ppd.lab7.util.SyncQueue;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class BigNumberSequenceAdder {
    private int numbers[][];

    private BigNumberSequenceAdder(int numbers[][]) {
        this.numbers = numbers;
    }

    public static int[] parallelAddBigNumberSequence(int numbers[][]) {
        for (int i = 0; i < numbers.length; i++) {
            reverseArray(numbers[i]);
        }
        BigNumberSequenceAdder adder = new BigNumberSequenceAdder(numbers);
        List<Integer> result = new ArrayList<>();
        SyncQueue digitQueue = new SyncQueue();
        (new Thread(() -> adder.addAllBigNumbersInRange(numbers, 0, numbers.length - 1, digitQueue))).start();
        Result oneDigitResult;
        while (true) {
            oneDigitResult = digitQueue.dequeue();
            if (!oneDigitResult.isResultPresent()) {
                break;
            }
            result.add(oneDigitResult.getResult());
        }
        int arrayResult[] = new int[result.size()];
        int i = arrayResult.length;
        for (Iterator<Integer> it = result.iterator(); it.hasNext();) {
            arrayResult[--i] = it.next();
        }
        return arrayResult;
    }

    private void addAllBigNumbersInRange(int numbers[][], int beginIndex, int endIndex, SyncQueue digitQueue) {
        if (beginIndex == endIndex) {
            for (int i = 0; i < numbers[beginIndex].length; i++) {
                digitQueue.enqueue(numbers[beginIndex][i]);
            }
            digitQueue.close();
        } else if (endIndex - beginIndex == 1) {
            int carry = 0;
            int digitResult;
            int i;
            for (i = 0; i < numbers[beginIndex].length && i < numbers[endIndex].length; i++) {
                digitResult = numbers[beginIndex][i] + numbers[endIndex][i] + carry;
                carry = digitResult / 10;
                digitQueue.enqueue(digitResult % 10);
            }
            for (; i < numbers[beginIndex].length; i++) {
                digitResult = numbers[beginIndex][i] + carry;
                carry = digitResult / 10;
                digitQueue.enqueue(digitResult % 10);
            }
            for (; i < numbers[endIndex].length; i++) {
                digitResult = numbers[endIndex][i] + carry;
                carry = digitResult / 10;
                digitQueue.enqueue(digitResult % 10);
            }
            while (carry > 0) {
                digitQueue.enqueue(carry % 10);
                carry /= 10;
            }
            digitQueue.close();
        } else {
            int middle = (beginIndex + endIndex) / 2;
            SyncQueue lowerSequenceQueue = new SyncQueue();
            SyncQueue higherSequenceQueue = new SyncQueue();
            (new Thread(() -> addAllBigNumbersInRange(numbers, beginIndex, middle, lowerSequenceQueue))).start();
            (new Thread(() -> addAllBigNumbersInRange(numbers, middle + 1, endIndex, higherSequenceQueue))).start();
            Result lowResult;
            Result highResult;
            int carry = 0;
            int digitResult;
            while (true) {
                lowResult = lowerSequenceQueue.dequeue();
                highResult = higherSequenceQueue.dequeue();
                if (!lowResult.isResultPresent() || !highResult.isResultPresent()) {
                    break;
                }
                digitResult = lowResult.getResult() + highResult.getResult() + carry;
                carry = digitResult / 10;
                digitQueue.enqueue(digitResult % 10);
            }
            while (lowResult.isResultPresent()) {
                digitResult = lowResult.getResult() + carry;
                carry = digitResult / 10;
                digitQueue.enqueue(digitResult % 10);
                lowResult = lowerSequenceQueue.dequeue();
            }
            while (highResult.isResultPresent()) {
                digitResult = highResult.getResult() + carry;
                carry = digitResult / 10;
                digitQueue.enqueue(digitResult % 10);
                highResult = higherSequenceQueue.dequeue();
            }
            while (carry > 0) {
                digitQueue.enqueue(carry % 10);
                carry /= 10;
            }
            digitQueue.close();
        }
    }

    private static void reverseArray(int array[]) {
        int lim = array.length / 2;
        int aux;
        for (int i = 0; i < lim; i++) {
            aux = array[i];
            array[i] = array[array.length - i - 1];
            array[array.length - i - 1] = aux;
        }
    }
}
