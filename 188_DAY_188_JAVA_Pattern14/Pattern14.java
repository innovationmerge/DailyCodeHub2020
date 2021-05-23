// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 14 using JAVA

/* Pattern 14 :- 
 *   *
  * * 
   *  
  * * 
 *   *
*/

class Patterns {
	public static void main(String[] args) {
		int row, column;
		int num = 1;
		int n = 5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= n; column++) {
				if (row == column || (row + column) == (n + 1)) {
					System.out.print("*");
				} else {
					System.out.print(" ");

				}
			} 
			System.out.println();
		}	
	}
}











