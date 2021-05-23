// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 4 using JAVA

/* Pattern 4 :- 
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
* 
*/

class Pattern {
	public static void main(String[] args) {
		int row, column;
		int n=5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.print(row + " ");
			}
			System.out.println();
		}
	}
}




