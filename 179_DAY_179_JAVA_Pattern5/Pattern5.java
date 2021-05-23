// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 5 using JAVA

/* Pattern 5 :- 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
*/

class Pattern {
	public static void main(String[] args) {
		int row, column;
		int n=5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.print(column + " ");
			}
			System.out.println();
		}
	}
}





