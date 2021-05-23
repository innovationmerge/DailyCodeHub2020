// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 11 using JAVA

/* Pattern 11 :- 
A 
B B 
C C C 
D D D D 
E E E E E 
D D D D 
C C C 
B B 
A
*/

class Patterns {
	public static void main(String[] args) {
		int row, column;
		int n=5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.print((char) (64 + row) + " ");
			}
			System.out.println();
		}

		for (row = n - 1; row >= 1; row--) {
			for (column = 1; column <= row; column++) {
				System.out.print((char) (64 + row) + " ");
			}
			System.out.println();
		}
	}
}








