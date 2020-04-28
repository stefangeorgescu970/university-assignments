
import java.util.Random;


public class Car implements Comparable<Car> {
	
	Cargo cargoType;
	float quantity;
	
	public Car(){
		Random generator = new Random();
		int cargoType = generator.nextInt(1000) % 4; 
		this.cargoType = Cargo.values()[cargoType];
		float quantity = generator.nextFloat() * 1000;
		this.quantity = quantity;
	}

	public float getQuantity(){
		return this.quantity;
	}
	
	public Cargo getCargoType(){
		return this.cargoType;
	}
	
	public String toString(){
		return "This car carries " + this.quantity + " of " + this.cargoType;
	}
	
	@Override
	public int compareTo(Car arg0) {
		return this.cargoType.getValue() - arg0.getCargoType().getValue();
	}
}
