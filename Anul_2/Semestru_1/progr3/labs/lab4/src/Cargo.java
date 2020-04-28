
public enum Cargo {
	COAL(0), COPPER(1), TIN(2), MAGNESIUM(3);
	
	private final int value;
	
	private Cargo(int value){
		this.value = value;
	}
	
	public int getValue(){
		return this.value;
	}
}
