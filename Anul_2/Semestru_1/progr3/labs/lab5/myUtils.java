import java.io.*;
import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;

public class myUtils {
	
	// Return employee from a file-like string
	
	static public Employee getEmployeeFromString(String lineRead){
		String[] newEmployee = lineRead.split(",");
		String name = newEmployee[0];
		Float number = Float.parseFloat(newEmployee[1]);
		Department department = Department.valueOf(newEmployee[2]);
		Employee finalEmployee = new Employee(name, number, department);
		return finalEmployee;
	}
	
	// Delete the contents for all output files
	
	static public void clearOutputFiles() {
		for(Department d: Department.values()){
			try{
				PrintWriter writer = new PrintWriter(d + ".txt");
				writer.print("");
				writer.close();
			}
			catch (IOException ex){
				ex.printStackTrace();
			}
		}
	}
	
	// Read the content of a company and create it
	
	static public Set<Employee> readCompany (String companyFile){
		Set<Employee> company = new TreeSet<Employee>();
		String lineRead = null;

		try {
		
			FileReader fileReader = new FileReader(companyFile);
			BufferedReader reader = new BufferedReader(fileReader);
			
			while((lineRead = reader.readLine()) != null) {
				company.add(myUtils.getEmployeeFromString(lineRead));
			}
			
			reader.close();
		
		} catch (FileNotFoundException ex) {
			ex.printStackTrace();
		} catch (IOException ex) {
			ex.printStackTrace();
		}
		
		return company;
	}
	
	// Print the employees of a company
	
	static public void printCompany (Set<Employee> company) {
		
		for(Employee employee : company) {
			System.out.println(employee);
		}
	}
	
	// Remove employees from a company with a salary bigger than e given maximum
	
	static public Set<Employee> removeWithWageAbove(Set<Employee> company, Float maximumWage){
		for(Iterator<Employee> iterator = company.iterator(); iterator.hasNext(); ){
			Employee currentEmpl = iterator.next();
			if(currentEmpl.getSalary() > maximumWage) {
				iterator.remove();
			}
		}
		return company;
	}
	
	// Add the employees of a company to files
	
	static public void addEmployeesToFile(Set<Employee> company){
		for(Employee employee : company) {
			try{
				FileWriter writer = new FileWriter(employee.getDepartment() + ".txt", true); // second argument for appending
				BufferedWriter bw = new BufferedWriter(writer);
				PrintWriter out = new PrintWriter(bw);
				out.println(employee.toFileString());
				out.close();
				bw.close();
				writer.close();
			}
			catch (IOException ex){
				ex.printStackTrace();
			}
		}
	}
}
