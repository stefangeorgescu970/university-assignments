import java.util.Random;
import java.util.List;


public class Snake {

	/*
	 * Declarations needed for keeping the snake in memory
	 */
	int[] parts;
	char[][] body;
	int noRows;
	
	/*
	 * Constructor for class snake, gets an int array and then builds random letters as required
	 */
	public Snake (int[] parts) {
		this.noRows = parts.length;
		this.parts = new int[this.noRows];
		this.parts = parts;
		
		this.body = new char[this.noRows][];
		Random generator = new Random();

		for(int i=0; i<this.noRows; i++){
			this.body[i] = new char[this.parts[i]];
			for(int j=0; j<this.parts[i]; j++){
				int newValue = generator.nextInt(26) + 97; // Generate a value between 97 and 122 including
				this.body[i][j] = (char)newValue; // Get the character associated with the ASCII code
			}
		}
	}
	
	/*
	 * method called automatically when trying to print to the console, will build snake as required
	 */
	public String toString(){
		String result = "";
		for(int i=0; i<this.noRows; i++){
			result += "(";
			for(int j=0; j<this.parts[i]; j++){
				result += this.body[i][j];
			}
			result += ")";
			if(i!=this.noRows-1){
				result += "-";
			} else {
				result += "=";
			}
		}
		
		result += "(O)";
		
		return result;
	}
	
	
	/*
	 * Shuffle both parts and body, making sure to keep correlation between those, in case two body parts have an exact number of characters
	 */
	public void shuffle(){
		List<Integer> indexArray = MyUtils.getShuffledIndexList(this.noRows);

		// build shuffled parts and body
		int[] newParts = new int[this.noRows];
		char[][] newBody = new char[this.noRows][];
		
		for(int i=0; i<this.noRows; i++){
			newParts[i] = this.parts[indexArray.get(i)];
			newBody[i] = new char[newParts[i]];
			newBody[i] = this.body[indexArray.get(i)];
		}
		
		// Remember the newly constructed body parts
		this.parts = newParts;
		this.body = newBody;
	}
	
}
