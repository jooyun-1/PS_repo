import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = Integer.parseInt(scanner.nextLine());
        int[][] arr = new int[101][101];
        for (int n = 0; n < N; n++) {
            String[] input = scanner.nextLine().split(" ");
            int left = Integer.parseInt(input[0]);
            int top = Integer.parseInt(input[1]);

            for (int i = left; i < left + 10; i++) {
                for (int j = top; j < top + 10; j++) {
                    arr[i][j] = 1;
                }
            }
        }
        
        int sum = 0;
        for (int[] row : arr) {
            for (int cell : row) {
                if (cell == 1) {
                    sum++;
                }
            }
        }
        System.out.println(sum);
    }
}
