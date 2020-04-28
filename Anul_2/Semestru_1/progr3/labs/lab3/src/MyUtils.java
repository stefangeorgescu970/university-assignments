import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MyUtils{
	/*
	 * Class for misc funcs
	 */
	
	
	/*
	 * Get a shuffling of indexes of a certain size
	 */
	static public List<Integer> getShuffledIndexList(int size) {
		List<Integer> indexArray = new ArrayList<Integer>();
		
		for(int i=0; i<size; i++){
			indexArray.add(i);
		}
		
		Collections.shuffle(indexArray);
		
		return indexArray;
	}
	
	
	/*
	 * Convert to int[]
	 */
	public static int[] convertIntegers(List<Integer> integers)
	{
	    int[] ret = new int[integers.size()];
	    for (int i=0; i < ret.length; i++)
	    {
	        ret[i] = integers.get(i).intValue();
	    }
	    return ret;
	}
}
