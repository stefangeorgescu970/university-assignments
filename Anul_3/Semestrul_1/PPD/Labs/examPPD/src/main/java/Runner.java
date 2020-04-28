public class Runner {
    public static void main(String[] args) {
        PrimeNumbers pn = new PrimeNumbers();
        MatrixMath mm = new MatrixMath();
        DiscreteConvolution dc = new DiscreteConvolution();

        try {

//            System.out.println(pn.generatePrimeNumbers(500));

//            mm.runMultiplication();

            System.out.println(dc.compute());

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
