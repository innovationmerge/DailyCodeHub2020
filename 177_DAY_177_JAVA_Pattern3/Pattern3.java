// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 3 using JAVA

/* Pattern 3 :- 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
*/

class Pattern {
	public static void main(String[] args) {
		int row, column;
		int n = 5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.print("* ");
				}
				System.out.println();
			}
		for (row = n - 1; row >= 1; row--) {
			for (column = 1; column <= row; column++) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}
}




