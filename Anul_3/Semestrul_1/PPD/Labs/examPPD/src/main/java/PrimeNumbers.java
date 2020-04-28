import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class PrimeNumbers {

    //subject 1 problem 3

    List<Integer> primeNumbers = new ArrayList<>();

    List<Integer> generatePrimeNumbers(int n) throws InterruptedException {
        primeNumbers.clear();

        primeNumbers.add(2);
        for (int i = 3; i < Math.sqrt(n); i++) {
            if (this.isPrime(i))
                this.primeNumbers.add(i);
        }

        List<Integer> found = new ArrayList<>(this.primeNumbers);

        this.primeNumbers.addAll(IntStream.range((int) (Math.sqrt(n) + 1), n + 1).boxed().collect(Collectors.toList()));

        List<Thread> threads = new ArrayList<>();

        for (Integer prime : found) {
            Thread t = new Thread(() -> removeMultiplesOf(prime));
            t.start();
            threads.add(t);
        }

        for (Thread t : threads) {
            t.join();
        }

        return this.primeNumbers.stream().filter(num -> num != -1).collect(Collectors.toList());

    }

    private void removeMultiplesOf(int base) {
        for (int i = 0; i < this.primeNumbers.size(); i++) {
            Integer current = this.primeNumbers.get(i);
            if (current == base) {
                continue;
            }

            if (current % base == 0) {
                this.primeNumbers.set(i, -1);
            }
        }
    }

    private boolean isPrime(Integer n) {
        for (int d = 2; d <= Math.sqrt(n); d++) {
            if (n % d == 0)
                return false;
        }
        return true;
    }
}
