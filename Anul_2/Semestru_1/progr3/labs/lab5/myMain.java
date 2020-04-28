import java.util.Set;

public class myMain {
	
	
	public static void main(String[] args) {
		
		// Set constants for the project
		final String fileNameCompanyA = "CompanyA.txt";
		final String fileNameCompanyB = "CompanyB.txt";
		final Float maximumWage = Float.parseFloat("3000.00");
		
		// First task
		
		// Read the 2 company files
		Set<Employee> companyA = myUtils.readCompany(fileNameCompanyA);
		Set<Employee> companyB = myUtils.readCompany(fileNameCompanyB);
		
		System.out.println("Company A: ");
		myUtils.printCompany(companyA);
		System.out.println("\n\nCompany B: ");
		myUtils.printCompany(companyB);
		
		//Second task
		companyA = myUtils.removeWithWageAbove(companyA, maximumWage);
		companyB = myUtils.removeWithWageAbove(companyB, maximumWage);

		System.out.println("Company A: ");
		myUtils.printCompany(companyA);
		System.out.println("\n\nCompany B: ");
		myUtils.printCompany(companyB);
		
		// Last task
		myUtils.clearOutputFiles();
		myUtils.addEmployeesToFile(companyA);
		myUtils.addEmployeesToFile(companyB);
	}
}
