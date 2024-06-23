import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int answer = 0;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int[][] board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        ArrayList<int[]> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0) {
                    arr.add(new int[]{i, j});
                }
            }
        }

        ArrayList<ArrayList<int[]>> combinations = getCombinations(arr, 3);

        for (ArrayList<int[]> comb : combinations) {
            for (int[] c : comb) {
                int i = c[0];
                int j = c[1];
                board[i][j] = 1;
            }

            bfs(board);
            
            for (int[] c : comb) {
                int i = c[0];
                int j = c[1];
                board[i][j] = 0;
            }
        }

        System.out.println(answer);
    }

    static void bfs(int[][] board) {
        int[][] visited = new int[N][M];
        int[][] temp = new int[N][M];
        for (int i = 0; i < N; i++) {
            System.arraycopy(board[i], 0, temp[i], 0, M);
        }

        ArrayList<int[]> queue = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (temp[i][j] == 2) {
                    queue.add(new int[]{i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] pos = queue.remove(0);
            int x = pos[0];
            int y = pos[1];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                    if (visited[nx][ny] == 0 && temp[nx][ny] == 0) {
                        temp[nx][ny] = 2;
                        visited[nx][ny] = 1;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (temp[i][j] == 0) {
                    result++;
                }
            }
        }

        answer = Math.max(result, answer);
    }

    static ArrayList<ArrayList<int[]>> getCombinations(ArrayList<int[]> arr, int r) {
        ArrayList<ArrayList<int[]>> result = new ArrayList<>();
        int[] data = new int[r];
        combinationUtil(arr, data, 0, arr.size() - 1, 0, r, result);
        return result;
    }

    static void combinationUtil(ArrayList<int[]> arr, int[] data, int start, int end, int index, int r, ArrayList<ArrayList<int[]>> result) {
        if (index == r) {
            ArrayList<int[]> combination = new ArrayList<>();
            for (int i = 0; i < r; i++) {
                combination.add(arr.get(data[i]));
            }
            result.add(combination);
            return;
        }

        for (int i = start; i <= end && end - i + 1 >= r - index; i++) {
            data[index] = i;
            combinationUtil(arr, data, i + 1, end, index + 1, r, result);
        }
    }
}