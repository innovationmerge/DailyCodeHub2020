// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 8 using JAVA

/* Pattern 8 :- 
1,1 
2,1 2,2 
3,1 3,2 3,3 
4,1 4,2 4,3 4,4 
5,1 5,2 5,3 5,4 5,5 
4,1 4,2 4,3 4,4 
3,1 3,2 3,3 
2,1 2,2 
1,1
*/

class Patterns {
	public static void main(String[] args) {
		int row, column;
		int n = 5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.print(row + "," + column + " ");
			}
			System.out.println();
		}

		for (row = n - 1; row >= 1; row--) {
			for (column = 1; column <= row; column++) {
				System.out.print(row + "," + column + " ");
			}
			System.out.println();
		}
	}
}









