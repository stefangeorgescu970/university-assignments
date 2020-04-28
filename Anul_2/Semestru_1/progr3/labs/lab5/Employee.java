import java.util.Locale;


public class Employee implements Comparable<Employee> {
	private String name;
	private Float salary;
	private Department department;
	private Integer id;
	static Integer currentId = 0;
	
	// Constructor for employee
	
	public Employee(String name, Float salary, Department department){
		this.name = name;
		this.salary = salary;
		this.department = department;
		this.id = Employee.currentId;
		Employee.currentId++; 
	}
	
	// Required getters
	
	public Integer getId(){
		return this.id;
	}
	
	public Float getSalary(){
		return this.salary;
	}
	
	public Department getDepartment(){
		return this.department;
	}
	
	// To string methods for file and for printing
	
	public String toString(){
		return this.id + ", " + this.name + ", " + String.format("%.2f", this.salary ) + ", " + this.department;
	}
	
	public String toFileString(){
		return this.name + "," + String.format(Locale.US, "%.2f", this.salary ) + "," + this.department;
	}
	
	// Required to use the set collection
	
	@Override
	public int compareTo(Employee arg0) {
		return this.id - arg0.getId();
	}
	
}
