import java.util.Collections;
import java.util.List;



public class myMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		List<Integer> lenArray = MyUtils.getShuffledIndexList(10); // Reusing this method here, not designed for this, so we will add 1 later
		Snake[] mySnakes = new Snake[10];
		
		// Building 10 snakes
		for(int i=0; i<9; i++){
			Collections.shuffle(lenArray);
			mySnakes[i] = new Snake(MyUtils.convertIntegers(lenArray));
		}
		
		// Printing and shuffling snakes
		for(int i=0;i<9;i++){
			System.out.println("Snake before shuffle");
			System.out.println(mySnakes[i]);
			mySnakes[i].shuffle();
			System.out.println("Snake after shuffle");
			System.out.print(mySnakes[i]+"\n\n\n");
		}
	}

}
