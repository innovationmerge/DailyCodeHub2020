// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 7 using JAVA

/* Pattern 7 :- 
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
*/

class Patterns {
	public static void main(String[] args) {
		int row, column;
		int n=5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.print(row + " ");
			}
			System.out.println();
		}

		for (row = n - 1; row >= 1; row--) {
			for (column = 1; column <= row; column++) {
				System.out.print(row + " ");
			}
			System.out.println();
		}
	}
}








