import java.util.Scanner;

public class Main {
    static int[][] arr;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int t = 0; t < T; t++) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();
            arr = new int[M + 1][N + 1];
            for (int i = 0; i <= M; i++) {
                for (int j = 0; j <= N; j++) {
                    arr[i][j] = 0;
                }
            }
            System.out.println(combiToDP(M, N));
        }
    }

    public static int combiToDP(int r, int c) {
        if (arr[r][c] != 0) {
            return arr[r][c];
        }
        if (r == c || c == 0) {
            return 1;
        } else {
            arr[r][c] = combiToDP(r - 1, c - 1) + combiToDP(r - 1, c);
            return arr[r][c];
        }
    }
}