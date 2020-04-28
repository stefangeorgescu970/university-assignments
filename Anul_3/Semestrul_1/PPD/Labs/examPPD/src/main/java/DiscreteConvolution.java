import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class DiscreteConvolution {


    List<Integer> v1 = IntStream.range(0, 100).boxed().collect(Collectors.toList());
    List<Integer> v2 = IntStream.range(0, 100).boxed().collect(Collectors.toList());
    List<Integer> v3 = IntStream.range(0, 100).boxed().collect(Collectors.toList());


    public List<Integer> compute() throws InterruptedException{

        List<Thread> threads = new ArrayList<>();

        for(int i = 0; i < v1.size(); i ++) {
            int finalI = i;
            Thread t = new Thread(() -> computeCell(finalI));
            t.start();

            threads.add(t);
        }


        for (Thread t : threads) {
            t.join();
        }

        return v3;
    }

    private void computeCell(int i) {
        int sum = 0;

        for(int j = 0; j <= i; j++) {
            sum += v1.get(j) * v2.get(i-j);
        }

        v3.set(i, sum);
    }

}
