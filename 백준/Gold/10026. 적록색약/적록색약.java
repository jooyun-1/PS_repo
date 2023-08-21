import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static char[][] grid;
    static int[][] visited;
    static int diffCnt, cnt;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static char flag;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        grid = new char[N][N];
        visited = new int[N][N];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                grid[i][j] = line.charAt(j);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                flag = grid[i][j];
                if (visited[i][j] == 0) {
                    diffCnt++;
                    dfs(i, j);
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 'R') {
                    grid[i][j] = 'G';
                }
            }
        }

        visited = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                flag = grid[i][j];
                if (visited[i][j] == 0) {
                    cnt++;
                    dfs(i, j);
                }
            }
        }

        System.out.println(diffCnt + " " + cnt);
    }

    static void dfs(int x, int y) {
        if (x >= N || x < 0 || y >= N || y < 0) {
            return;
        }

        if (flag == grid[x][y] && visited[x][y] == 0) {
            visited[x][y] = 1;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                dfs(nx, ny);
            }
        }
    }
}