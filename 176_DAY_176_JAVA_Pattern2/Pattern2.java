// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 2 using JAVA

/* Pattern 2 :- 
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
		for (row = n; row >= 1; row--) {
			for (column = 1; column <= row; column++) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}
}



