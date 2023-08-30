import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] house;
    static int[] dx = {1, 0, 1}; // 아래, 오른쪽, 오른 대각선
    static int[] dy = {0, 1, 1};
    static int cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        house = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                house[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0, 1, 0);
        System.out.println(cnt);
    }

    static void dfs(int x, int y, int dir) {
        if (house[x][y] == 1) {
            return;
        }
        if (x == N - 1 && y == N - 1) {
            cnt++;
            return;
        }
        if (x + 1 < N && y + 1 < N) {
            if (house[x + 1][y + 1] == 0 && house[x + 1][y] == 0 && house[x][y + 1] == 0) {
                dfs(x + 1, y + 1, 2);
            }
        }
        if (dir == 0 || dir == 2) {
            if (y + 1 < N) {
                if (house[x][y + 1] == 0) {
                    dfs(x, y + 1, 0);
                }
            }
        }
        if (dir == 1 || dir == 2) {
            if (x + 1 < N) {
                if (house[x + 1][y] == 0) {
                    dfs(x + 1, y, 1);
                }
            }
        }
    }
}