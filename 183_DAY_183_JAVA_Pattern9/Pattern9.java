// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 9 using JAVA

/* Pattern 9 :- 
A 
A A 
A A A 
A A A A 
A A A A A 
A A A A 
A A A 
A A 
A
*/

class Patterns {
	public static void main(String[] args) {
		int row, column;
		int n=5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.print((char) 65 + " ");
			}
			System.out.println();
		}

		for (row = n - 1; row >= 1; row--) {
			for (column = 1; column <= row; column++) {
				System.out.print((char) 65 + " ");
			}
			System.out.println();
		}
	}
}








