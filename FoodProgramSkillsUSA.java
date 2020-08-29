import java.util.Scanner;

public class FoodProgramSkillsUSA {

	private static double total;
	private static double customerTotal;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner userInput = new Scanner(System.in);
		
		int numHotDog;
		int numBrat;
		int numHamburger;
		int numFries;
		int numSoda;
		int numWater;
		String answerMenu;
		String answerOption;
		
		System.out.println("Contestant Number: 1024, Program #1, Food Program\n");
		//ask user if they want menu
		System.out.println("Input\nHello. Welcome to my food truck, "
				+ "would you like to view the menu?");
		answerMenu = userInput.nextLine();
		if (answerMenu.equalsIgnoreCase("yes"))
			System.out.print("Hot Dog: $2.50, Brat: $3.50, Hamburger: $5.00, "
							+ "Fries: $2.00, Soda: $2.00, Water: $0.00\n\n");
		
		//while loop until input "exit" is given by user
		do { 
			System.out.println("Input\nChoose one of the following options, Calculate Additional Food, "
					+ "Clear Previous Entry, Exit (Type in Calculate, Clear, or Exit): ");
			answerOption = userInput.nextLine();
			
			//this option will allow user to buy food and calculate their total
			//there is a running total for all sales throughout the day as well
			//as a customer total for each separate customer
			if (answerOption.equalsIgnoreCase("Calculate")) {
				customerTotal = 0;
				System.out.println("How many hot dogs would you like to purchase?");
				numHotDog = userInput.nextInt();
				if (numHotDog >= 0) {
					total += (numHotDog * 2.50);
					customerTotal += (numHotDog * 2.50);
				}
			
				System.out.println("How many brats would you like to purchase?");
				numBrat = userInput.nextInt();
				if (numBrat >= 0) {
					total += (numBrat * 3.50);
					customerTotal += (numBrat * 3.50);
				}
			
				System.out.println("How many hamburgers would you like to purchase?");
				numHamburger = userInput.nextInt();
				if (numHamburger >= 0) {
					total += (numHamburger * 5.00);
					customerTotal += (numHamburger * 5.00);
				}
			
				System.out.println("How many fries would you like to purchase?");
				numFries = userInput.nextInt();
				if (numFries >= 0) {
					total += (numFries * 2.00);
					customerTotal += (numFries * 2.00);
				}
			
				System.out.println("How many cans of soda would you like to purchase?");
				numSoda = userInput.nextInt();
				if (numSoda >= 0) {
					total += (numSoda * 2.00);
					customerTotal += (numSoda * 2.00);
				}
			
				System.out.println("How many bottles of water would you like to purchase?");
				numWater = userInput.nextInt();
			
				System.out.print("\nOutput" + "\nRunning Total: " + "$" + total + "0");
				System.out.println("\nCustomer Total: " + "$" + customerTotal + "0" + "\n");
			}
			//this option will clear the previous customer's total and return updated running total
			if (answerOption.equalsIgnoreCase("Clear")) {
				total = total - customerTotal;
				System.out.println("\nOutput" + "\nRunning Total: " + "$" + total + "0" + "\n");
			}
		
		} while (!(answerOption.equalsIgnoreCase("Exit")));
	}
}
