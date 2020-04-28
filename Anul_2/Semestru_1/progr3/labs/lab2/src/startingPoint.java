
import org.fusesource.jansi.AnsiConsole;
import java.util.Random;

public class startingPoint {

	/*
	 * Starting point of the application, initialisation of the Grid and call to see all states
	 */
	public static void main(String[] args) {
		Grid myGrid = new Grid();
		myGrid.seeEvolution();	
	}
}

class Grid {
	
	/*
	 * Declaring constants for the size of the matrix and the number of iterations for evolvement
	 */
	Integer numberOfColumns = 10;
	Integer numberOfRows = 10;
	Integer numberOfIterations = 1;
	Boolean[][] matrix;
	
	/*
	 * Initialiser for the Grid class, filling values in randomly
	 */
	public Grid() {
		Random generator = new Random();
		this.matrix = new Boolean[this.numberOfRows][this.numberOfColumns];
		for(int i=0; i<this.numberOfRows; i++){
			for(int j=0; j<this.numberOfColumns; j++) {
				this.matrix[i][j] = generator.nextBoolean();
			}
		}
	}
	
	/*
	 * Function used to print the matrix as required by the task
	 */
	public void print(int state) {
		AnsiConsole.systemInstall();
		
		String ANSI_RED = "\u001B[0;31m";
		String ANSI_GREEN = "\u001B[0;32m";
		String ANSI_WHITEONRED = "\u001b[37;41m";
		String ANSI_WHITEONGREEN = "\u001b[37;42m";
		String ANSI_NORMALBG = "\u001b[0m";
		String ANSI_WHITE = "\u001B[0;37m";
		
		AnsiConsole.out.print(ANSI_WHITE + "This is state number " + state + "\n" + ANSI_NORMALBG);

		for(int i=0; i<this.numberOfRows; i++){
			for(int j=0; j<this.numberOfColumns; j++) {
				if(this.matrix[i][j]){
					AnsiConsole.out.print(ANSI_WHITEONGREEN + " alive " + ANSI_GREEN);	
				} else {
					AnsiConsole.out.print(ANSI_WHITEONRED + " dead  " + ANSI_RED);
				}
			}
			AnsiConsole.out.print("\n");
		}
		AnsiConsole.out.print("\n");
		AnsiConsole.out.print(ANSI_WHITE + " " + ANSI_NORMALBG);
		AnsiConsole.systemUninstall();
	}
	
	/*
	 * Function used to get the number of live neighbors from the old state.
	 * PARAMS:
	 * oldMatrix - the old state of the population
	 * row and column - the position in the grid
	 */
	
	int getNumberOfLiveNeighbors(Boolean[][] oldMatrix, int row, int column) {
		int number = 0;
		
		if(row != 0 && column!=0 &&  oldMatrix[row-1][column-1]) number++;
		if(row != 0 && oldMatrix[row-1][column]) number++;
		if(row != 0 && column!=this.numberOfColumns-1 && oldMatrix[row-1][column+1]) number++;
		if(column!=0 && oldMatrix[row][column-1]) number++;
		if(column!=this.numberOfColumns-1 && oldMatrix[row][column+1]) number++;
		if(row != this.numberOfRows-1 && column!=0 && oldMatrix[row+1][column-1]) number++;
		if(row != this.numberOfRows-1 && oldMatrix[row+1][column]) number++;
		if(row != this.numberOfRows-1 && column!=this.numberOfColumns-1 && oldMatrix[row+1][column+1]) number++;

		return number;
	}
	
	/*
	 * Function used to start the evolution and print each state
	 */
	void seeEvolution(){
		int state = 1;
		this.print(state);
		for(int i=0;i<this.numberOfIterations; i++){
			this.evolve();
			this.print(++state);
		}
	}
	
	/*
	 * Function used to do one step of evolution
	 */
	void evolve() {
		
		
		// Copy the matrix
		Boolean[][] oldMatrix = new Boolean[this.numberOfRows][this.numberOfColumns];
		
		for(int i=0; i<this.numberOfRows; i++){
			for(int j=0; j<this.numberOfColumns; j++) {
				if(this.matrix[i][j]){
					oldMatrix[i][j] = true;
				} else {
					oldMatrix[i][j] = false;
				}
			}
		}
		
		// Evolve each cell depending on the state of its neighbors
		for(int i=0; i<this.numberOfRows; i++){
			for(int j=0; j<this.numberOfColumns; j++) {
				int noLiveNeigh = this.getNumberOfLiveNeighbors(oldMatrix, i, j);
				if(this.matrix[i][j]){
					if (noLiveNeigh < 2 || noLiveNeigh > 3){
						this.matrix[i][j]=false;	
					}
				} else {
					if(noLiveNeigh == 3) {
						this.matrix[i][j]=true;
					}
				}
			}
		}
	}
}
