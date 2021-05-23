// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 10 using JAVA

/* Pattern 10 :- 
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D 
A B C 
A B 
A
*/

class Patterns {
	public static void main(String[] args) {
		int row, column;
		int n = 5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.print((char) (64 + column) + " ");
			}
			System.out.println();
		}

		for (row = n - 1; row >= 1; row--) {
			for (column = 1; column <= row; column++) {
				System.out.print((char) (64 + column) + " ");
			}
			System.out.println();
		}
	}
}








