import java.util.Scanner;

public class ShapesCalcs1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner userInput = new Scanner(System.in);
		
		int number;
		
	do {
		System.out.print("Choose which shape you want to get the information of: "
				+ "\n 1. Rectangular Prism \n 2. Cylinder \n 3. Sphere "
				+ "\n 4. Cone \n 5. Pyramid \n Or \n 6. To Exit" + "\n" +
				"Enter the number (1, 2, 3, 4, 5, or 6) of the shape you want to get the info of: ");
		
		number = userInput.nextInt();
	
		if (number == 1) {
			System.out.println(rectPrism());
		}
		
		if (number == 2) {
			System.out.println(cyLinder());
		}
		
		if (number == 3) {
			System.out.println(spHere());
		}
		
		if (number == 4) {
			System.out.println(coNe());
		}
		
		if (number == 5) {
			System.out.println(pyrAmid());
		}
		if (number != 1 && number != 2 && number != 3 && number != 4 && number != 5 && number != 6) {
			System.out.println("\n" + "Try running the program again and enter an integer (1, 2, 3, 4. 5, or 6) when prompted \n");
		}
		
	} while (number != 6);
		
	}
	
	public static String rectPrism() 
	{
		Scanner userInput = new Scanner(System.in);
		
		System.out.print("Enter the length of the prism: ");
		double l = userInput.nextDouble();
		System.out.print("Enter the height of the prism: ");
		double h = userInput.nextDouble();
		System.out.print("Enter the weight of the prism: ");
		double w = userInput.nextDouble();
	
		return "\n" + "Volume: " + l * h * w + "\n" + "Surface Area: " + 2 * (w * l + h * l + h * w) 
				+ "\n" + "Space Diagonal: " + Math.sqrt(l * l + w * w * h * h);
	}
	
	public static String cyLinder()
	{
		Scanner userInput = new Scanner(System.in);
		
		System.out.print("Enter the height of the cylinder: ");
		double h = userInput.nextDouble();
		System.out.print("Enter the radius of the cylinder: ");
		double r = userInput.nextDouble();
		
		return "\n" + "Exact Lateral Surface Area: " + 2 * r * h + " pi"
		+ "\n" + "~ Lateral Surface Area: " + 2 * Math.PI * r * h
		+ "\n" + "Exact Volume: " + r * r * h + " pi"
		+ "\n" + "~ Volume: " + Math.PI * r * r * h
		+ "\n" + "Exact Surface Area: " + (2 * r * h + " pi") + " + " + (2 * r * r + " pi")
		+ "\n" + "~ Surface Area: " + ((2 * Math.PI * r * h) + (2 * Math.PI * r * r)) + "\n";
	}
	
	public static String spHere()
	{
		Scanner userInput = new Scanner(System.in);
		
		System.out.print("Enter the radius of the sphere: ");
		double r = userInput.nextDouble();
		
		return "\n" + "Exact Volume: " + 4.0 / 3.0 * r * r * r + " pi"
		+ "\n" + "~ Volume: " + 4.0 / 3.0 * Math.PI * r * r * r
		+ "\n" + "Exact Surface Area: " + 4 * r * r + " pi"
		+ "\n" + "~ Surface Area: " + 4 * Math.PI * r * r + "\n";
	}
	
	public static String coNe()
	{
		Scanner userInput = new Scanner(System.in);
		
		System.out.print("Enter the height of the cone: ");
		double h = userInput.nextDouble();
		System.out.print("Enter the radius of the cone: ");
		double r = userInput.nextDouble();
		
		return "\n" + "Exact Lateral Surface Area: " + (r + " pi * ") + (Math.sqrt(h * h + r * r)) 
		+ "\n" + "~ Lateral Surface Area: " + (r * Math.PI) * (Math.sqrt(h * h + r * r))
		+ "\n" + "Slant Height: " + Math.sqrt(r *r + h * h)
		+ "\n" + "Exact Volume: " + r * r * (h / 3.0) + " pi"
		+ "\n" + "~ Volume: " + Math.PI * r * r * (h / 3.0)
		+ "\n" + "Exact Surface Area: " + (r + " pi * ") + (r + (Math.sqrt(h * h + r * r)))
		+ "\n" + "~ Surface Area: " + (r * Math.PI) * (r + (Math.sqrt(h * h + r * r))) + "\n";
	}
	
	public static String pyrAmid()
	{
		Scanner userInput = new Scanner(System.in);
		
		System.out.print("Enter the base length of the pyramid: ");
		double l = userInput.nextDouble();
		System.out.print("Enter the base width of the pyramid: ");
		double w = userInput.nextDouble();
		System.out.print("Enter the height of the pyramid: ");
		double h = userInput.nextDouble();
		
		return "\n" + "Volume: " + (l * w * h) / 3.0
		+ "\n" + "Surface Area: " + ((l * w) + (l * (Math.sqrt((w / 2.0) * (w / 2.0) + h * h))) + 
		(w * (Math.sqrt((l / 2.0) * (l / 2.0) + h * h)))) + "\n";
	}
	

}




