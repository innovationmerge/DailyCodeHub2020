// **************** "iNNovationMerge DailyCodeHub" ****************
// Visit https://www.innovationmerge.com/
// Theme : Pattern week with JAVA
// Print Pattern 12 using JAVA

/* Pattern 12 :- 
01 
02 03 
04 05 06 
07 08 09 10 
11 12 13 14 15 
16 17 18 19 
20 21 22 
23 24 
25 
*/

class Patterns {
	public static void main(String[] args) {
		int row, column;
		int num = 1;
		int n = 5;
		for (row = 1; row <= n; row++) {
			for (column = 1; column <= row; column++) {
				System.out.printf("%02d ", num++);
			}
			System.out.println();
		}

		for (row = n - 1; row >= 1; row--) {
			for (column = 1; column <= row; column++) {
				System.out.printf("%02d ", num++);
			}
			System.out.println();
		}	
	}
}









