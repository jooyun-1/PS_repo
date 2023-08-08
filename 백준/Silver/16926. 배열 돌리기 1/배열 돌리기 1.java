import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int r = scanner.nextInt();
        
        int[][] data = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                data[i][j] = scanner.nextInt();
            }
        }

        for (int rotation = 0; rotation < r; rotation++) {
            for (int i = 0; i < Math.min(n, m) / 2; i++) {
                int x = i, y = i;
                int temp = data[x][y];

                for (int j = i + 1; j < n - i; j++) {  // Left
                    x = j;
                    int prevValue = data[x][y];
                    data[x][y] = temp;
                    temp = prevValue;
                }

                for (int j = i + 1; j < m - i; j++) {  // Down
                    y = j;
                    int prevValue = data[x][y];
                    data[x][y] = temp;
                    temp = prevValue;
                }

                for (int j = i + 1; j < n - i; j++) {  // Right
                    x = n - j - 1;
                    int prevValue = data[x][y];
                    data[x][y] = temp;
                    temp = prevValue;
                }

                for (int j = i + 1; j < m - i; j++) {  // Up
                    y = m - j - 1;
                    int prevValue = data[x][y];
                    data[x][y] = temp;
                    temp = prevValue;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(data[i][j] + " ");
            }
            System.out.println();
        }
    }
	
}