import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class myMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {	
		List<Car> trainA = new ArrayList<Car>();
		List<Car> trainB = new ArrayList<Car>();
		
		for(int i=0; i<25; i++) {
			Car oneCar = new Car();
			trainA.add(oneCar);
			Car otherCar = new Car();
			trainB.add(otherCar);
		}
		
		for(int i=0; i<trainA.size(); i++) {
			System.out.println("Train A: " + trainA.get(i));
		}
		
		for(int i=0; i<trainB.size(); i++) {
			System.out.println("Train B: " + trainB.get(i));
		}
		
		List<Car> trainC = new ArrayList<Car>();
		
		for(int i=0; i<trainA.size(); i++) {
			trainC.add(trainA.get(i));
			trainC.add(trainB.get(i));
		}
		
		trainA.clear();
		trainB.clear();
		
		System.out.println("\n\nTrain A is now empty");
		System.out.println("Train B is now empty");
		
		for(int i=0; i<trainC.size(); i++) {
			System.out.println("Train C: " + trainC.get(i));
		}
		
		trainC.sort(null);
		
		System.out.println("\n\nAfter sorting: \n");
		
		for(int i=0; i<trainC.size(); i++) {
			System.out.println("Train C: " + trainC.get(i));
		}

		float[] totals = new float[Cargo.values().length];
		
		for( Car c : trainC ){
			totals[c.getCargoType().getValue()] += c.getQuantity();
		}
		
		for(int i=0; i< Cargo.values().length; i++){
			System.out.println("There is a total of " + totals[i] + " of " + Cargo.values()[i]);
		}
		
		int numberTry = 0;
		Scanner in = new Scanner(System.in);
		int num = Integer.MAX_VALUE;
		
		while(numberTry < 2) {
			System.out.println("\nPlease enter a natural number: ");
			num = in.nextInt();
			if(num < trainC.size()) {
				break;
			} else {
				numberTry++;
				System.out.println("Invalid input.");
			}
		}
		
		if(num < trainC.size()){
			int current = num;
			while(current < trainC.size()){
				trainC.remove(current - 1);
				current = current + num - 1;
			}
			for(int i=0; i<trainC.size(); i++) {
				System.out.println("Train C: " + trainC.get(i));
			}
			
		} else {
			System.out.println("Failed to provide good input.");
		}
		
		
	}

}
