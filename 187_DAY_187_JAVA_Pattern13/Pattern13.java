// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 13 using JAVA

/* Pattern 13 :- 
         1
       2 3 4
     5 6 7 8 9
  10111213141516
171819202122232425 
*/

class Patterns {
	public static void main(String[] args) {
		int row, column;
		int num = 1;
		int n = 5;
		int ch = 1;
		for (row = 1; row <= n; row++) { // print the space
			for (int space = 1; space <= n - row; space++) {
				System.out.print("  ");
			}
			// print the star
			for (int star = 1; star <= (2 * row - 1); star++) {
				System.out.printf("%2d", ch++);

			} // print the next line
			System.out.println();
		}
	}
}











